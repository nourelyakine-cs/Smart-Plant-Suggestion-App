import json
import os
import requests
import re
from datetime import datetime
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Chargement des variables d'environnement
load_dotenv()

# Configuration du client Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# -----------------------------
# EXTRACTION VILLE 
# -----------------------------
def extract_intent_ai(user_message):
    prompt = f"Analyse : '{user_message}'. Réponds UNIQUEMENT ce JSON : {{\"ville\": \"nom\", \"type\": \"catégorie\"}}. Si pas de ville, ville='NON'. Types possibles: fruits, légumes, fleurs, aromates, TOUT."
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.0)
        )
        # On extrait le JSON même s'il y a du texte autour
        match = re.search(r"\{.*\}", response.text, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {"ville": "NON", "type": "TOUT"}
    except:
        return {"ville": "NON", "type": "TOUT"}



# -----------------------------
# LOGIQUE MÉTÉO & SAISON
# -----------------------------
def get_saison():
    m = datetime.now().month
    if m in [3, 4, 5]:     return "printemps"
    elif m in [6, 7, 8]:   return "été"
    elif m in [9, 10, 11]: return "automne"
    else:                  return "hiver"

def get_weather_forecast(city):
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "fr"
    }
    try:
        # Météo actuelle
        now_res = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params, timeout=5)
        now = now_res.json()
        
        # Prévisions
        forecast_res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=params, timeout=5)
        forecast_data = forecast_res.json()

        jours = []
        for i in range(0, min(40, len(forecast_data["list"])), 8):
            item = forecast_data["list"][i]
            jours.append({
                "date": item["dt_txt"][:10],
                "temperature": round(item["main"]["temp"]),
                "description": item["weather"][0]["description"]
            })

        return {
            "ville": city,
            "maintenant": {"temperature": round(now["main"]["temp"]), "description": now["weather"][0]["description"], "humidite": now["main"]["humidity"]},
            "previsions_5_jours": jours,
            "temp_min_semaine": min(j["temperature"] for j in jours),
            "temp_max_semaine": max(j["temperature"] for j in jours),
            "saison": get_saison()
        }
    except Exception as e:
        # ROUE DE SECOURS (SIMULATION)
        return {
            "ville": city + " (Simulé)",
            "maintenant": {"temperature": 18, "description": "ensoleillé", "humidite": 60},
            "previsions_5_jours": [{"date": "2026-03-29", "temperature": 19, "description": "beau temps"}],
            "temp_min_semaine": 12, "temp_max_semaine": 22, "saison": get_saison()
        }

# -----------------------------
# GÉNÉRATION DE RÉPONSES (IA)
# -----------------------------
def get_general_advice(user_message):
    prompt = f"""
    En tant qu'expert PlantAI, réponds à : "{user_message}".
    Donne des conseils pour 3 plantes en format JSON uniquement.
    Si une ville est mentionnée dans la question, adapte les conseils à son climat.
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.0)
    )
    return response.text



def build_prompt_weather(weather, plante_type):
    return f"""
    Tu es PlantAI, expert botaniste mondial. 
    L'utilisateur veut des {plante_type} adaptés au climat de {weather['ville']}.
    
    DONNÉES MÉTÉO RÉELLES À {weather['ville']} :
    - Température actuelle : {weather['maintenant']['temperature']}°C
    - Saison : {weather['saison']}
    - Minima de la semaine : {weather['temp_min_semaine']}°C
    
    RÈGLES STRICTES :
    1. Propose UNIQUEMENT des {plante_type}.
    2. Les plantes DOIVENT pouvoir survivre aux températures de {weather['ville']} citées plus haut.
    3. Si pluie prévue ({weather['maintenant']['description']}), adapte le conseil.
    4. Réponds STRICTEMENT en JSON (liste de 3 objets).

    Format JSON :
    [
      {{"nom":"...","emoji":"...","pourquoi":"...","conseil":"...","difficulte":"Facile"}},
      {{"nom":"...","emoji":"...","pourquoi":"...","conseil":"...","difficulte":"Moyen"}},
      {{"nom":"...","emoji":"...","pourquoi":"...","conseil":"...","difficulte":"Expert"}}
    ]
    """



# -----------------------------
# VALIDATION JSON
# -----------------------------
def parse_and_validate_growth(raw_text):
    try:
        clean_text = re.sub(r"```json|```", "", raw_text).strip()
        return json.loads(clean_text)
    except:
        return [{"nom": "Erreur format", "emoji": "⚠️", "pourquoi": "L'IA a mal répondu.", "conseil": "Réessayez.", "difficulte": "N/A"}]

# -----------------------------
# AGENT PRINCIPAL
# -----------------------------


# -----------------------------
# 🚀 AGENT PRINCIPAL (VERSION FINALE)
# -----------------------------
def run_agent(user_message):
    try:
        # 1. Extraction intelligente de l'intention (Ville + Type de plante)
        intent = extract_intent_ai(user_message)
        
        # Nettoyage des données extraites
        city_raw = str(intent.get('ville', 'NON')).strip()
        city_clean = city_raw.replace(".", "").replace("!", "")
        plante_type = intent.get('type', 'TOUT')

        # 2. AIGUILLAGE : Ville détectée ou Question Générale ?
        if "NON" in city_clean.upper() or not city_clean:
            # --- CAS A : Question sans ville (ou ville non reconnue) ---
            print(f"💡 Mode Conseil Général (Type demandé : {plante_type})")
            
            # On passe l'intention complète à l'IA pour qu'elle sache de quoi on parle
            raw_response = get_general_advice(user_message)
            final_data = parse_and_validate_growth(raw_response)
        
        else:
            # --- CAS B : Question avec Ville (Logique Météo) ---
            print(f"🌍 Analyse météo pour : {city_clean} (Recherche de : {plante_type})")
            
            # Récupération des données météo réelles
            meteo = get_weather_forecast(city_clean)
            
            # Construction du prompt ultra-spécifique (Ville + Météo + Type)
            prompt = build_prompt_weather(meteo, plante_type)
            
            # Appel Gemini avec température 0 pour un JSON stable
            response = client.models.generate_content(
                model="gemini-2.5-flash", 
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.0,
                    response_mime_type="application/json" # Force le format JSON si supporté
                )
            )
            
            # Validation et nettoyage du JSON reçu
            final_data = parse_and_validate_growth(response.text)

        # 3. Retour du résultat final formaté proprement
        return json.dumps(final_data, indent=2, ensure_ascii=False)

    except Exception as e:
        # En cas d'erreur critique, on renvoie un message JSON propre pour ne pas crash le front
        error_msg = [{"error": f"Désolé, une erreur est survenue : {str(e)}"}]
        return json.dumps(error_msg, indent=2, ensure_ascii=False)



# -----------------------------
# TEST INTERACTIF
# -----------------------------
if __name__ == "__main__":
    print("🌿 PlantAI prêt ! (Tapez 'exit' pour quitter)")
    while True:
        query = input("\n👤 Vous : ")
        if query.lower() in ["exit", "quitter"]: break
        print(run_agent(query))