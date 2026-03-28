"""
API Conversationnelle - Gemini Agent avec RAG
Utilise gemma-3-27b-it (sans system_instruction)
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
CORS(app)

# ============================================
# CONFIGURATION
# ============================================

import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Utiliser gemma-3-27b-it (sans system_instruction)
# Ce modèle fonctionne bien et ne supporte pas system_instruction
gemini_model = genai.GenerativeModel('gemma-3-27b-it')
print("✅ Modèle chargé: gemma-3-27b-it")

db = PlantDatabase()
weather_service = WeatherService()

# Stockage des conversations
conversations = {}

def get_or_create_conversation(session_id):
    if session_id not in conversations:
        conversations[session_id] = {
            'history': [],
            'last_city': None,
            'last_weather': None
        }
    return conversations[session_id]

# ============================================
# ENDPOINTS
# ============================================

@app.route('/')
def home():
    return jsonify({
        'name': 'Smart Plant AI - Agent Conversationnel',
        'version': '3.0',
        'description': 'Assistant jardinier intelligent',
        'plants_count': db.get_plants_count(),
        'model': 'gemma-3-27b-it',
        'status': 'running'
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': 'Message vide'}), 400
        
        conv = get_or_create_conversation(session_id)
        
        # ==========================================
        # ÉTAPE 1: Vérifier si c'est une question de jardinage
        # ==========================================
        is_gardening_prompt = f"""
        Question: "{user_message}"
        Est-ce que cette question concerne le jardinage ou les plantes ?
        Réponds uniquement par "oui" ou "non".
        """
        
        try:
            is_gardening_response = gemini_model.generate_content(is_gardening_prompt)
            is_gardening = is_gardening_response.text.strip().lower() == "oui"
        except:
            is_gardening = True
        
        if not is_gardening:
            return jsonify({
                'response': "🌿 Je suis un assistant jardinier spécialisé. Je ne peux répondre qu'aux questions sur les plantes, le jardinage, et les conseils de culture. Posez-moi une question sur les plantes !",
                'context': {'gardening_only': True}
            })
        
        # ==========================================
        # ÉTAPE 2: Extraire la ville
        # ==========================================
        extract_city_prompt = f"""
        Message: "{user_message}"
        Extrais le nom de la ville dans ce message.
        Si aucune ville n'est mentionnée, réponds "aucune".
        """
        
        try:
            city_response = gemini_model.generate_content(extract_city_prompt)
            city = city_response.text.strip().lower()
        except:
            city = "aucune"
        
        # ==========================================
        # ÉTAPE 3: Récupérer la météo
        # ==========================================
        weather = None
        if city and city != "aucune":
            weather = weather_service.get_weather(city)
            if 'error' not in weather:
                conv['last_city'] = city
                conv['last_weather'] = weather
        elif conv['last_weather']:
            weather = conv['last_weather']
        
        # ==========================================
        # ÉTAPE 4: Récupérer TOUTES les plantes
        # ==========================================
        all_plants_info = db.get_plants_info_for_gemini()
        
        # ==========================================
        # ÉTAPE 5: Construire le contexte
        # ==========================================
        context = ""
        if weather and 'error' not in weather:
            context = f"""
CONTEXTE MÉTÉO ACTUEL:
- Ville: {weather['city']}
- Température: {weather['temperature']}°C
- Humidité: {weather['humidity']}%
- Saison: {weather['season']}
"""
        
        history = ""
        if conv['history']:
            history = "HISTORIQUE DE LA CONVERSATION:\n"
            for h in conv['history'][-3:]:
                history += f"User: {h['user']}\nAssistant: {h['assistant'][:100]}...\n"
        
        # ==========================================
        # ÉTAPE 6: Générer la réponse
        # ==========================================
        prompt = f"""
{context}

{history}

🌿 MA BASE DE DONNÉES ({db.get_plants_count()} plantes):
{all_plants_info}

👤 QUESTION DE L'UTILISATEUR: {user_message}

🎯 INSTRUCTIONS:
1. Tu es un assistant jardinier expert.
2. Utilise  les plantes de MA base de données en prioritaires et aprés tu peux suggerer des autres plantes.
3. Si l'utilisateur demande une plante spécifique, vérifie si elle est dans la base sinon tu peux aussi repondre.
4. Utilise la météo si disponible pour contextualiser.
5. Donne des conseils précis et chaleureux.
6. Réponds EN FRANÇAIS.
7. Si la question est vague, propose des suggestions.
8. Ne dit jamais aux utilsateurs si des données figure dans la bdd ou nom
9.ne dit pas au utilsateurs les phrase selon mon base de données
10.ne dit pas au utilsateur si la plante figure ou nom repond diretement
11.en réponse utilises des émojies de plantes


RÉPONSE EN FRANÇAIS:
"""
        
        response = gemini_model.generate_content(prompt)
        
        # Sauvegarder l'historique
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
                'temperature': weather['temperature'] if weather and 'error' not in weather else None,
                'humidity': weather['humidity'] if weather and 'error' not in weather else None,
                'season': weather['season'] if weather and 'error' not in weather else None,
                'plants_in_db': db.get_plants_count(),
                'model': 'gemma-3-27b-it'
            }
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear_conversation():
    data = request.json
    session_id = data.get('session_id', 'default')
    
    if session_id in conversations:
        conversations[session_id] = {
            'history': [],
            'last_city': None,
            'last_weather': None
        }
    
    return jsonify({'success': True, 'message': 'Conversation effacée'})

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
    return jsonify({'error': 'Plante non trouvée'}), 404

if __name__ == '__main__':
    print("=" * 60)
    print("🌱 SMART PLANT AI - AGENT CONVERSATIONNEL")
    print("=" * 60)
    print(f"📊 {db.get_plants_count()} plantes dans la base")
    print(f"🤖 Modèle: gemma-3-27b-it (sans system_instruction)")
    print(f"💬 Mode: Conversationnel avec RAG")
    print(f"🚀 Serveur: http://localhost:5001")
    print("=" * 60)
    print("\n🎯 Exemples de questions:")
    print("   - 'Je suis à Paris, que puis-je planter ?'")
    print("   - 'La tomate pousse-t-elle ici ?'")
    print("   - 'Conseils pour mon basilic ?'")
    print("   - 'Quelle plante résiste à la sécheresse ?'")
    print("=" * 60)
    app.run(debug=True, port=5001)