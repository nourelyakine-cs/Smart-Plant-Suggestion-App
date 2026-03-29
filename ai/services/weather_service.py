"""
Service météo - Version robuste avec fallback
"""

import requests
from datetime import datetime

class WeatherService:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.nominatim_url = "https://nominatim.openstreetmap.org/search"
    
    def get_weather(self, city):
        """Récupère la météo réelle avec fallback"""
        try:
            # Essayer Open-Meteo d'abord
            geo_response = requests.get(
                self.geo_url,
                params={'name': city, 'count': 1},
                timeout=10
            )
            geo_data = geo_response.json()
            
            lat = None
            lon = None
            city_name = city
            
            if geo_data.get('results'):
                lat = geo_data['results'][0]['latitude']
                lon = geo_data['results'][0]['longitude']
                city_name = geo_data['results'][0]['name']
            else:
                # Fallback sur Nominatim
                nominatim_response = requests.get(
                    self.nominatim_url,
                    params={'q': city, 'format': 'json', 'limit': 1},
                    timeout=10,
                    headers={'User-Agent': 'SmartPlantAI/1.0'}
                )
                nominatim_data = nominatim_response.json()
                if nominatim_data:
                    lat = float(nominatim_data[0]['lat'])
                    lon = float(nominatim_data[0]['lon'])
                    city_name = nominatim_data[0]['display_name'].split(',')[0]
                else:
                    return self._simulate_weather(city)
            
            # Récupérer la météo
            weather_response = requests.get(
                self.base_url,
                params={
                    'latitude': lat,
                    'longitude': lon,
                    'current_weather': True,
                    'hourly': ['temperature_2m', 'relativehumidity_2m']
                },
                timeout=10
            )
            weather_data = weather_response.json()
            
            # Saison
            month = datetime.now().month
            if month in [3, 4, 5]:
                season = "printemps"
            elif month in [6, 7, 8]:
                season = "été"
            elif month in [9, 10, 11]:
                season = "automne"
            else:
                season = "hiver"
            
            return {
                'city': city_name,
                'temperature': weather_data['current_weather']['temperature'],
                'humidity': weather_data['hourly']['relativehumidity_2m'][0],
                'season': season
            }
            
        except Exception:
            return self._simulate_weather(city)
    
    def _simulate_weather(self, city):
        """Données simulées si l'API échoue"""
        month = datetime.now().month
        if month in [3, 4, 5]:
            season = "printemps"
            temp = 20
            humidity = 65
        elif month in [6, 7, 8]:
            season = "été"
            temp = 30
            humidity = 50
        elif month in [9, 10, 11]:
            season = "automne"
            temp = 18
            humidity = 70
        else:
            season = "hiver"
            temp = 10
            humidity = 75
        
        return {
            'city': city,
            'temperature': temp,
            'humidity': humidity,
            'season': season,
            'simulated': True
        }