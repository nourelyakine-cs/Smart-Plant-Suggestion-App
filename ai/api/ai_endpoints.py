"""
╔══════════════════════════════════════════════════════╗
║           🌿  SMART PLANT AI  —  v3.0               ║
║     Gemini AI · Plant Database · Weather Service     ║
╚══════════════════════════════════════════════════════╝
"""

# ── Standard Library ──────────────────────────────────
import sys
import os
from datetime import datetime

# ── Third-Party ───────────────────────────────────────
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# ── Internal Modules ──────────────────────────────────
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.plant_database import PlantDatabase
from services.weather_service import WeatherService


# ══════════════════════════════════════════════════════
#  APP SETUP
# ══════════════════════════════════════════════════════

app = Flask(__name__)
app.secret_key = "smart_plant_ai_secret_key_2024"
CORS(app, origins=["*"])
load_dotenv()


# ── Gemini Initialization ─────────────────────────────

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_model = None

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel("gemma-3-27b-it")
        print("✅ Gemini model loaded: gemma-3-27b-it")
    except Exception as e:
        print(f"⚠️  Could not load Gemini model: {e}")
else:
    print("⚠️  No GEMINI_API_KEY found. Chat will not work. Add it to ai/.env")


# ── Services ──────────────────────────────────────────

db              = PlantDatabase()
weather_service = WeatherService()
conversations   = {}


# ══════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════

def get_or_create_conversation(session_id: str) -> dict:
    """Return existing conversation or initialise a fresh one."""
    if session_id not in conversations:
        conversations[session_id] = {
            "history":      [],
            "last_city":    None,
            "last_weather": None,
        }
    return conversations[session_id]


def calculate_match_score(plant: dict, weather: dict) -> int:
    """
    Score a plant against current weather conditions.
    Max score: 100  (season 40 · temperature 40 · humidity 20)
    """
    score    = 0
    season   = weather.get("season", "")
    temp     = weather.get("temperature", 20)
    humidity = weather.get("humidity", 60)

    # ── Season match (40 pts) ─────────────────────────
    if season in plant.get("seasons", []):
        score += 40

    # ── Temperature match (40 pts) ────────────────────
    t_opt = plant.get("temp_optimal", [15, 25])
    t_min = plant.get("temp_min", 0)
    t_max = plant.get("temp_max", 40)

    if t_opt[0] <= temp <= t_opt[1]:
        score += 40
    elif t_min <= temp <= t_max:
        score += 20

    # ── Humidity match (20 pts) ───────────────────────
    h_opt = plant.get("humidity_optimal", [50, 70])
    h_min = plant.get("humidity_min", 20)
    h_max = plant.get("humidity_max", 90)

    if h_opt[0] <= humidity <= h_opt[1]:
        score += 20
    elif h_min <= humidity <= h_max:
        score += 10

    return score


# ══════════════════════════════════════════════════════
#  ROUTES
# ══════════════════════════════════════════════════════

# ── Health Check ──────────────────────────────────────

@app.route("/")
def home():
    return jsonify({
        "name":               "Smart Plant AI",
        "version":            "3.0",
        "plants_count":       db.get_plants_count(),
        "ai_chat_available":  gemini_model is not None,
        "status":             "running",
    })


# ── Weather ───────────────────────────────────────────

@app.route("/api/weather/<city>", methods=["GET"])
def get_weather(city):
    """Fetch real-time weather for a city. No Gemini required."""
    try:
        return jsonify(weather_service.get_weather(city))
    except Exception as e:
        return jsonify({"error": str(e), "city": city}), 500


# ── Plant Suggestions ─────────────────────────────────

@app.route("/api/suggest", methods=["GET"])
def suggest_plants():
    """Rule-based plant suggestions derived from live weather. No Gemini required."""
    city = request.args.get("city", "").strip()
    if not city:
        return jsonify({"error": "city parameter is required"}), 400

    try:
        weather = weather_service.get_weather(city)
        if "error" in weather:
            return jsonify({"error": f"Could not get weather for {city}"}), 400

        scored = []
        for key, plant in db.get_all_plants().items():
            score = calculate_match_score(plant, weather)
            if score > 0:
                scored.append({
                    "key":             key,
                    "name":            plant["name"],
                    "scientific_name": plant.get("scientific_name", ""),
                    "category":        plant.get("category", ""),
                    "difficulty":      plant.get("difficulty", ""),
                    "water_needs":     plant.get("water_needs", ""),
                    "sun_needs":       plant.get("sun_needs", ""),
                    "seasons":         plant.get("seasons", []),
                    "temp_min":        plant.get("temp_min", 0),
                    "temp_max":        plant.get("temp_max", 40),
                    "temp_optimal":    plant.get("temp_optimal", [15, 25]),
                    "description":     plant.get("description", ""),
                    "care_tips":       plant.get("care_tips", []),
                    "match_score":     score,
                })

        scored.sort(key=lambda x: x["match_score"], reverse=True)
        top = scored[:6]

        return jsonify({
            "city":          weather.get("city", city),
            "weather":       weather,
            "plants":        top,
            "total_matched": len(scored),
            "showing":       len(top),
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── AI Chat ───────────────────────────────────────────

@app.route("/api/chat", methods=["POST"])
def chat():
    if not gemini_model:
        return jsonify({
            "success":  False,
            "response": "⚠️ AI chat is not configured. Please add your GEMINI_API_KEY to ai/.env and restart the AI server.",
        }), 503

    try:
        data         = request.json
        user_message = data.get("message", "").strip()
        session_id   = data.get("session_id", "default")

        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        conv = get_or_create_conversation(session_id)

        # ── Gardening relevance check ─────────────────
        try:
            check = gemini_model.generate_content(
                f'Question: "{user_message}"\n'
                f'Is this about gardening, plants, flowers, trees, soil, or nature? '
                f'Answer only "oui" or "non".'
            )
            is_gardening = check.text.strip().lower().startswith("oui")
        except Exception:
            is_gardening = True

        if not is_gardening:
            return jsonify({
                "success":  True,
                "response": "🌿 I'm a specialized gardening assistant. I can only answer questions about plants and gardening. Ask me about plants!",
            })

        # ── City extraction ───────────────────────────
        try:
            city_resp = gemini_model.generate_content(
                f'Message: "{user_message}"\n'
                f'Extract the city name only. If no city mentioned, answer exactly "aucune". Nothing else.'
            )
            city = city_resp.text.strip().lower().split("\n")[0]
        except Exception:
            city = "aucune"

        # ── Weather context ───────────────────────────
        weather = None
        if city and city != "aucune":
            weather = weather_service.get_weather(city)
            if "error" not in weather:
                conv["last_city"]    = city
                conv["last_weather"] = weather
        elif conv["last_weather"]:
            weather = conv["last_weather"]

        # ── Build prompt ──────────────────────────────
        weather_block = ""
        if weather and "error" not in weather:
            weather_block = (
                f"CURRENT WEATHER:\n"
                f"- City:        {weather['city']}\n"
                f"- Temperature: {weather['temperature']}°C\n"
                f"- Humidity:    {weather['humidity']}%\n"
                f"- Season:      {weather['season']}\n"
            )

        history_block = ""
        if conv["history"]:
            history_block = "CONVERSATION HISTORY:\n"
            for h in conv["history"][-3:]:
                history_block += f"User:      {h['user']}\nAssistant: {h['assistant'][:120]}...\n"

        prompt = f"""{weather_block}
{history_block}
🌿 PLANT DATABASE ({db.get_plants_count()} plants):
{db.get_plants_info_for_gemini()}

User question: {user_message}

Instructions:
- You are an expert gardening assistant.
- Use the plant database as primary reference.
- Use weather context if available.
- Give precise, warm advice.
- Respond in the same language as the user's question (French if French, English if English).
- Use plant emojis 🌱🌿🌸.
- Never mention the database to the user.

RESPONSE:
"""

        response = gemini_model.generate_content(prompt)

        # ── Update conversation history ────────────────
        conv["history"].append({
            "user":      user_message,
            "assistant": response.text,
            "timestamp": datetime.now().isoformat(),
        })
        if len(conv["history"]) > 10:
            conv["history"] = conv["history"][-10:]

        return jsonify({
            "success":  True,
            "response": response.text,
            "context": {
                "city":        weather["city"] if weather and "error" not in weather else conv["last_city"],
                "temperature": weather.get("temperature") if weather and "error" not in weather else None,
                "season":      weather.get("season")      if weather and "error" not in weather else None,
            },
        })

    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500


# ── Conversation Reset ────────────────────────────────

@app.route("/api/clear", methods=["POST"])
def clear_conversation():
    session_id = request.json.get("session_id", "default")
    if session_id in conversations:
        conversations[session_id] = {
            "history":      [],
            "last_city":    None,
            "last_weather": None,
        }
    return jsonify({"success": True})


# ── Plant Catalogue ───────────────────────────────────

@app.route("/api/plants", methods=["GET"])
def list_plants():
    plants = db.get_all_plants()
    return jsonify({
        "count":      len(plants),
        "plants":     list(plants.keys()),
        "categories": list({p["category"] for p in plants.values()}),
    })


@app.route("/api/plant/<name>", methods=["GET"])
def get_plant(name):
    plant = db.get_plant(name)
    if plant:
        return jsonify(plant)
    return jsonify({"error": "Plant not found"}), 404


# ══════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════

if __name__ == "__main__":
    print("═" * 55)
    print("🌱  SMART PLANT AI SERVICE")
    print("═" * 55)
    print(f"📊  {db.get_plants_count()} plants in database")
    print(f"🤖  AI Chat : {'✅ Ready' if gemini_model else '❌ No GEMINI_API_KEY'}")
    print(f"🚀  Running at : http://localhost:5001")
    print("═" * 55)
    app.run(debug=True, port=5001)