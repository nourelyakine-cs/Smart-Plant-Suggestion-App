"""
Smart Plant AI - Flask Service
Gemini AI + plant DB + weather (no Gemini key needed for suggestions/weather)
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import google.generativeai as genai
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.plant_database import PlantDatabase
from services.weather_service import WeatherService

app = Flask(__name__)
app.secret_key = "smart_plant_ai_secret_key_2024"
CORS(app, origins=["*"])

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
gemini_model = None

if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        gemini_model = genai.GenerativeModel('gemma-3-27b-it')
        print("✅ Gemini model loaded: gemma-3-27b-it")
    except Exception as e:
        print(f"⚠️ Could not load Gemini model: {e}")
else:
    print("⚠️ No GEMINI_API_KEY found. Chat will not work. Add it to ai/.env")

db = PlantDatabase()
weather_service = WeatherService()
conversations = {}


def get_or_create_conversation(session_id):
    if session_id not in conversations:
        conversations[session_id] = {
            'history': [],
            'last_city': None,
            'last_weather': None
        }
    return conversations[session_id]


def calculate_match_score(plant, weather):
    """Score a plant against current weather (max 100)"""
    score = 0
    season = weather.get('season', '')
    temp = weather.get('temperature', 20)
    humidity = weather.get('humidity', 60)

    # Season match (40 pts)
    if season in plant.get('seasons', []):
        score += 40

    # Temperature match (40 pts)
    t_opt = plant.get('temp_optimal', [15, 25])
    t_min = plant.get('temp_min', 0)
    t_max = plant.get('temp_max', 40)
    if t_opt[0] <= temp <= t_opt[1]:
        score += 40
    elif t_min <= temp <= t_max:
        score += 20

    # Humidity match (20 pts)
    h_opt = plant.get('humidity_optimal', [50, 70])
    h_min = plant.get('humidity_min', 20)
    h_max = plant.get('humidity_max', 90)
    if h_opt[0] <= humidity <= h_opt[1]:
        score += 20
    elif h_min <= humidity <= h_max:
        score += 10

    return score


# ============================================================
# ENDPOINTS
# ============================================================

@app.route('/')
def home():
    return jsonify({
        'name': 'Smart Plant AI',
        'version': '3.0',
        'plants_count': db.get_plants_count(),
        'ai_chat_available': gemini_model is not None,
        'status': 'running'
    })


@app.route('/api/weather/<city>', methods=['GET'])
def get_weather(city):
    """Get real weather for a city (no Gemini needed)"""
    try:
        weather = weather_service.get_weather(city)
        return jsonify(weather)
    except Exception as e:
        return jsonify({'error': str(e), 'city': city}), 500


@app.route('/api/suggest', methods=['GET'])
def suggest_plants():
    """Rule-based plant suggestions from weather (no Gemini needed)"""
    city = request.args.get('city', '').strip()
    if not city:
        return jsonify({'error': 'city parameter is required'}), 400

    try:
        weather = weather_service.get_weather(city)
        if 'error' in weather:
            return jsonify({'error': f'Could not get weather for {city}'}), 400

        all_plants = db.get_all_plants()
        scored = []

        for key, plant in all_plants.items():
            score = calculate_match_score(plant, weather)
            if score > 0:
                scored.append({
                    'key': key,
                    'name': plant['name'],
                    'scientific_name': plant.get('scientific_name', ''),
                    'category': plant.get('category', ''),
                    'difficulty': plant.get('difficulty', ''),
                    'water_needs': plant.get('water_needs', ''),
                    'sun_needs': plant.get('sun_needs', ''),
                    'seasons': plant.get('seasons', []),
                    'temp_min': plant.get('temp_min', 0),
                    'temp_max': plant.get('temp_max', 40),
                    'temp_optimal': plant.get('temp_optimal', [15, 25]),
                    'description': plant.get('description', ''),
                    'care_tips': plant.get('care_tips', []),
                    'match_score': score
                })

        scored.sort(key=lambda x: x['match_score'], reverse=True)
        top = scored[:6]

        return jsonify({
            'city': weather.get('city', city),
            'weather': weather,
            'plants': top,
            'total_matched': len(scored),
            'showing': len(top)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    if not gemini_model:
        return jsonify({
            'success': False,
            'response': '⚠️ AI chat is not configured. Please add your GEMINI_API_KEY to ai/.env and restart the AI server.'
        }), 503

    try:
        data = request.json
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        conv = get_or_create_conversation(session_id)

        # Check if gardening-related
        try:
            check = gemini_model.generate_content(
                f'Question: "{user_message}"\nIs this about gardening or plants? Answer only "oui" or "non".'
            )
            is_gardening = check.text.strip().lower() == "oui"
        except:
            is_gardening = True

        if not is_gardening:
            return jsonify({
                'success': True,
                'response': "🌿 I'm a specialized gardening assistant. I can only answer questions about plants and gardening. Ask me about plants!"
            })

        # Extract city
        try:
            city_resp = gemini_model.generate_content(
                f'Message: "{user_message}"\nExtract the city name. If none, answer "aucune".'
            )
            city = city_resp.text.strip().lower()
        except:
            city = "aucune"

        # Get weather
        weather = None
        if city and city != "aucune":
            weather = weather_service.get_weather(city)
            if 'error' not in weather:
                conv['last_city'] = city
                conv['last_weather'] = weather
        elif conv['last_weather']:
            weather = conv['last_weather']

        all_plants_info = db.get_plants_info_for_gemini()

        context = ""
        if weather and 'error' not in weather:
            context = f"""CURRENT WEATHER:
- City: {weather['city']}
- Temperature: {weather['temperature']}°C
- Humidity: {weather['humidity']}%
- Season: {weather['season']}
"""

        history = ""
        if conv['history']:
            history = "CONVERSATION HISTORY:\n"
            for h in conv['history'][-3:]:
                history += f"User: {h['user']}\nAssistant: {h['assistant'][:120]}...\n"

        prompt = f"""{context}
{history}
🌿 PLANT DATABASE ({db.get_plants_count()} plants):
{all_plants_info}

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

        conv['history'].append({
            'user': user_message,
            'assistant': response.text,
            'timestamp': datetime.now().isoformat()
        })
        if len(conv['history']) > 10:
            conv['history'] = conv['history'][-10:]

        return jsonify({
            'success': True,
            'response': response.text,
            'context': {
                'city': weather['city'] if weather and 'error' not in weather else conv['last_city'],
                'temperature': weather.get('temperature') if weather and 'error' not in weather else None,
                'season': weather.get('season') if weather and 'error' not in weather else None,
            }
        })

    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500


@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    data = request.json
    session_id = data.get('session_id', 'default')
    if session_id in conversations:
        conversations[session_id] = {'history': [], 'last_city': None, 'last_weather': None}
    return jsonify({'success': True})


@app.route('/api/plants', methods=['GET'])
def list_plants():
    plants = db.get_all_plants()
    return jsonify({
        'count': len(plants),
        'plants': list(plants.keys()),
        'categories': list(set(p['category'] for p in plants.values()))
    })


@app.route('/api/plant/<name>', methods=['GET'])
def get_plant(name):
    plant = db.get_plant(name)
    if plant:
        return jsonify(plant)
    return jsonify({'error': 'Plant not found'}), 404


if __name__ == '__main__':
    print("=" * 55)
    print("🌱 SMART PLANT AI SERVICE")
    print("=" * 55)
    print(f"📊 {db.get_plants_count()} plants in database")
    print(f"🤖 AI Chat: {'✅ Ready' if gemini_model else '❌ No GEMINI_API_KEY'}")
    print(f"🚀 Running at: http://localhost:5001")
    print("=" * 55)
    app.run(debug=True, port=5001)