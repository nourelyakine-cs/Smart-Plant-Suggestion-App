"""
Test de l'agent conversationnel
"""

import requests
import uuid

# Créer une session unique
session_id = str(uuid.uuid4())

print("=" * 60)
print("🌱 SMART PLANT AI - AGENT CONVERSATIONNEL")
print("=" * 60)
print("Posez vos questions sur les plantes !")
print("Tapez 'clear' pour effacer l'historique")
print("Tapez 'quit' pour quitter")
print("=" * 60)

while True:
    user_input = input("\n🌿 Vous: ")
    
    if user_input.lower() == 'quit':
        break
    elif user_input.lower() == 'clear':
        requests.post('http://localhost:5001/api/clear', json={'session_id': session_id})
        print("✅ Conversation effacée")
        continue
    
    response = requests.post(
        'http://localhost:5001/api/chat',
        json={'message': user_input, 'session_id': session_id}
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n🤖 Assistant: {data['response']}")
        
        if data['context'].get('city'):
            print(f"\n📍 Contexte: {data['context']['city']}, {data['context']['temperature']}°C")
    else:
        print(f"❌ Erreur: {response.status_code}")
        print(response.text)

print("\n👋 Au revoir ! Bon jardinage !")