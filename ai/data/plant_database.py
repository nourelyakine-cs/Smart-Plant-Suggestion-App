"""
Base de données complète - 50 plantes
"""

PLANT_DATABASE = {
    # ========== LÉGUMES (15) ==========
    "tomate": {
        "name": "Tomate", "scientific_name": "Solanum lycopersicum", "category": "légume",
        "temp_min": 15, "temp_max": 30, "temp_optimal": [20, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Tuteurer dès la plantation", "💧 Arroser au pied", "✂️ Supprimer les gourmands"],
        "description": "Plante fruitière populaire, riche en vitamines"
    },
    "laitue": {
        "name": "Laitue", "scientific_name": "Lactuca sativa", "category": "légume",
        "temp_min": 5, "temp_max": 25, "temp_optimal": [10, 20],
        "humidity_min": 50, "humidity_max": 90, "humidity_optimal": [70, 80],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "élevé", "sun_needs": "mi-ombre",
        "care_tips": ["💧 Sol toujours frais", "🌿 Pailler", "📅 Semis échelonnés"],
        "description": "Légume-feuille à croissance rapide"
    },
    "carotte": {
        "name": "Carotte", "scientific_name": "Daucus carota", "category": "légume",
        "temp_min": 10, "temp_max": 25, "temp_optimal": [15, 20],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol léger sans cailloux", "📏 Éclaircir", "💧 Arrosage régulier"],
        "description": "Légume-racine riche en vitamines"
    },
    "courgette": {
        "name": "Courgette", "scientific_name": "Cucurbita pepo", "category": "légume",
        "temp_min": 15, "temp_max": 35, "temp_optimal": [20, 28],
        "humidity_min": 50, "humidity_max": 85, "humidity_optimal": [65, 75],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "élevé", "sun_needs": "plein soleil",
        "care_tips": ["💧 Arroser abondamment", "🌾 Pailler", "🍽️ Récolter régulièrement"],
        "description": "Légume d'été très productif"
    },
    "poivron": {
        "name": "Poivron", "scientific_name": "Capsicum annuum", "category": "légume",
        "temp_min": 18, "temp_max": 30, "temp_optimal": [22, 28],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol riche", "💧 Arrosage régulier", "☀️ Beaucoup de soleil"],
        "description": "Légume fruitier coloré, riche en vitamines"
    },
    "aubergine": {
        "name": "Aubergine", "scientific_name": "Solanum melongena", "category": "légume",
        "temp_min": 18, "temp_max": 32, "temp_optimal": [22, 28],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol chaud", "💧 Arroser régulièrement", "🌿 Pailler"],
        "description": "Légume méditerranéen, idéal pour la ratatouille"
    },
    "haricot": {
        "name": "Haricot vert", "scientific_name": "Phaseolus vulgaris", "category": "légume",
        "temp_min": 12, "temp_max": 28, "temp_optimal": [18, 25],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Arrosage modéré", "📏 Espacer 40cm"],
        "description": "Légume facile, riche en fibres"
    },
    "petit_pois": {
        "name": "Petit pois", "scientific_name": "Pisum sativum", "category": "légume",
        "temp_min": 5, "temp_max": 20, "temp_optimal": [10, 18],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis tôt", "🌿 Tuteurer", "💧 Arrosage régulier"],
        "description": "Légume printanier sucré"
    },
    "radis": {
        "name": "Radis", "scientific_name": "Raphanus sativus", "category": "légume",
        "temp_min": 5, "temp_max": 22, "temp_optimal": [10, 18],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis rapide", "💧 Arrosage régulier", "📏 Récolte 4 semaines"],
        "description": "Légume racine à croissance ultra-rapide"
    },
    "navet": {
        "name": "Navet", "scientific_name": "Brassica rapa", "category": "légume",
        "temp_min": 5, "temp_max": 22, "temp_optimal": [10, 18],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol riche", "💧 Arrosage régulier", "📏 Espacer 20cm"],
        "description": "Légume racine d'automne"
    },
    "poireau": {
        "name": "Poireau", "scientific_name": "Allium porrum", "category": "légume",
        "temp_min": 5, "temp_max": 25, "temp_optimal": [10, 20],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Repiquage", "🌿 Butter", "💧 Arrosage régulier"],
        "description": "Légume d'hiver rustique"
    },
    "oignon": {
        "name": "Oignon", "scientific_name": "Allium cepa", "category": "légume",
        "temp_min": 5, "temp_max": 28, "temp_optimal": [12, 24],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["printemps"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Bulbes", "💧 Peu d'eau", "🌿 Sol drainé"],
        "description": "Bulbe indispensable en cuisine"
    },
    "ail": {
        "name": "Ail", "scientific_name": "Allium sativum", "category": "légume",
        "temp_min": 0, "temp_max": 28, "temp_optimal": [10, 25],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["automne", "printemps"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Planter les gousses", "💧 Arrosage modéré", "🌿 Sol drainé"],
        "description": "Condiment essentiel et plante médicinale"
    },
    "epinard": {
        "name": "Épinard", "scientific_name": "Spinacia oleracea", "category": "légume",
        "temp_min": 5, "temp_max": 20, "temp_optimal": [10, 15],
        "humidity_min": 60, "humidity_max": 90, "humidity_optimal": [70, 80],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "élevé", "sun_needs": "mi-ombre",
        "care_tips": ["💧 Sol frais", "🌱 Sol riche", "📅 Semis échelonnés"],
        "description": "Légume-feuille riche en fer"
    },
    "betterave": {
        "name": "Betterave", "scientific_name": "Beta vulgaris", "category": "légume",
        "temp_min": 10, "temp_max": 25, "temp_optimal": [15, 20],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "📏 Éclaircir", "💧 Arrosage régulier"],
        "description": "Légume-racine coloré et sucré"
    },
    
    # ========== AROMATIQUES (15) ==========
    "basilic": {
        "name": "Basilic", "scientific_name": "Ocimum basilicum", "category": "aromatique",
        "temp_min": 18, "temp_max": 30, "temp_optimal": [22, 26],
        "humidity_min": 50, "humidity_max": 85, "humidity_optimal": [65, 75],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Pincer régulièrement", "❄️ Protéger du froid", "💧 Arroser le matin"],
        "description": "Herbe aromatique parfumée"
    },
    "menthe": {
        "name": "Menthe", "scientific_name": "Mentha spicata", "category": "aromatique",
        "temp_min": 5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 50, "humidity_max": 90, "humidity_optimal": [70, 80],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "élevé", "sun_needs": "mi-ombre",
        "care_tips": ["🌱 Planter en pot", "💧 Arrosage abondant", "✂️ Tailler régulièrement"],
        "description": "Herbe aromatique fraîche"
    },
    "persil": {
        "name": "Persil", "scientific_name": "Petroselinum crispum", "category": "aromatique",
        "temp_min": 10, "temp_max": 25, "temp_optimal": [15, 20],
        "humidity_min": 50, "humidity_max": 85, "humidity_optimal": [65, 75],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "mi-ombre",
        "care_tips": ["🌱 Germination lente", "💧 Sol frais", "✂️ Récolter extérieur"],
        "description": "Herbe aromatique riche en vitamines"
    },
    "romarin": {
        "name": "Romarin", "scientific_name": "Rosmarinus officinalis", "category": "aromatique",
        "temp_min": -5, "temp_max": 35, "temp_optimal": [15, 28],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Arrosage espacé", "🌿 Sol bien drainé", "✂️ Tailler après floraison"],
        "description": "Herbe méditerranéenne très résistante"
    },
    "thym": {
        "name": "Thym", "scientific_name": "Thymus vulgaris", "category": "aromatique",
        "temp_min": -5, "temp_max": 35, "temp_optimal": [15, 28],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Sol calcaire", "✂️ Tailler après floraison"],
        "description": "Herbe aromatique médicinale"
    },
    "ciboulette": {
        "name": "Ciboulette", "scientific_name": "Allium schoenoprasum", "category": "aromatique",
        "temp_min": 5, "temp_max": 25, "temp_optimal": [10, 20],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Division des touffes", "💧 Arrosage régulier", "✂️ Couper les fleurs"],
        "description": "Herbe au goût d'oignon doux"
    },
    "estragon": {
        "name": "Estragon", "scientific_name": "Artemisia dracunculus", "category": "aromatique",
        "temp_min": 5, "temp_max": 28, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["printemps", "été"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Multiplication par bouture", "💧 Arrosage modéré", "❄️ Protéger l'hiver"],
        "description": "Herbe aromatique pour vinaigrettes"
    },
    "cerfeuil": {
        "name": "Cerfeuil", "scientific_name": "Anthriscus cerefolium", "category": "aromatique",
        "temp_min": 5, "temp_max": 20, "temp_optimal": [10, 18],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "mi-ombre",
        "care_tips": ["🌱 Semis direct", "💧 Sol frais", "📅 Semis échelonnés"],
        "description": "Herbe aromatique délicate"
    },
    "aneth": {
        "name": "Aneth", "scientific_name": "Anethum graveolens", "category": "aromatique",
        "temp_min": 10, "temp_max": 25, "temp_optimal": [15, 22],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Arrosage régulier", "🌿 Support si vent"],
        "description": "Herbe au goût anisé"
    },
    "coriandre": {
        "name": "Coriandre", "scientific_name": "Coriandrum sativum", "category": "aromatique",
        "temp_min": 10, "temp_max": 25, "temp_optimal": [15, 22],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Arrosage régulier", "📅 Semis échelonnés"],
        "description": "Herbe parfumée pour cuisine asiatique"
    },
    "sauge": {
        "name": "Sauge", "scientific_name": "Salvia officinalis", "category": "aromatique",
        "temp_min": -5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Sol drainé", "✂️ Tailler après floraison"],
        "description": "Herbe médicinale et aromatique"
    },
    "origan": {
        "name": "Origan", "scientific_name": "Origanum vulgare", "category": "aromatique",
        "temp_min": -5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Sol calcaire", "✂️ Tailler régulièrement"],
        "description": "Herbe méditerranéenne parfumée"
    },
    "laurier": {
        "name": "Laurier sauce", "scientific_name": "Laurus nobilis", "category": "aromatique",
        "temp_min": -5, "temp_max": 35, "temp_optimal": [10, 28],
        "humidity_min": 30, "humidity_max": 70, "humidity_optimal": [40, 60],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌿 Arbuste", "💧 Peu d'eau", "✂️ Tailler pour la forme"],
        "description": "Arbuste aromatique aux feuilles persistantes"
    },
    "sarriette": {
        "name": "Sarriette", "scientific_name": "Satureja hortensis", "category": "aromatique",
        "temp_min": 10, "temp_max": 28, "temp_optimal": [15, 25],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Peu d'eau", "✂️ Tailler après floraison"],
        "description": "Herbe aromatique pour les grillades"
    },
    
    # ========== FLEURS (10) ==========
    "lavande": {
        "name": "Lavande", "scientific_name": "Lavandula angustifolia", "category": "fleur",
        "temp_min": -5, "temp_max": 35, "temp_optimal": [15, 28],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Tailler après floraison", "💧 Laisser sécher", "🌿 Sol calcaire"],
        "description": "Plante méditerranéenne parfumée"
    },
    "rosier": {
        "name": "Rosier", "scientific_name": "Rosa", "category": "fleur",
        "temp_min": -10, "temp_max": 35, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [55, 70],
        "seasons": ["printemps", "été", "automne"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Tailler en fin d'hiver", "🌱 Engrais spécial", "💧 Arroser au pied"],
        "description": "Reine des fleurs"
    },
    "souci": {
        "name": "Souci", "scientific_name": "Calendula officinalis", "category": "fleur",
        "temp_min": 5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [55, 70],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "🌸 Supprimer les fleurs fanées", "💡 Repousse naturelle"],
        "description": "Fleur médicinale et décorative"
    },
    "capucine": {
        "name": "Capucine", "scientific_name": "Tropaeolum majus", "category": "fleur",
        "temp_min": 10, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [55, 70],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol pauvre", "🌸 Fleurs comestibles", "🐞 Repousse les pucerons"],
        "description": "Fleur grimpante comestible"
    },
    "oeillet": {
        "name": "Œillet", "scientific_name": "Dianthus caryophyllus", "category": "fleur",
        "temp_min": 5, "temp_max": 28, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 70, "humidity_optimal": [50, 60],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol drainé", "💧 Peu d'eau", "🌸 Supprimer fleurs fanées"],
        "description": "Fleur parfumée aux couleurs vives"
    },
    "pensee": {
        "name": "Pensée", "scientific_name": "Viola tricolor", "category": "fleur",
        "temp_min": 5, "temp_max": 22, "temp_optimal": [10, 18],
        "humidity_min": 50, "humidity_max": 80, "humidity_optimal": [60, 70],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "mi-ombre",
        "care_tips": ["🌱 Sol frais", "🌸 Supprimer les fleurs fanées", "📅 Fleurit longtemps"],
        "description": "Fleur rustique aux couleurs variées"
    },
    "coquelicot": {
        "name": "Coquelicot", "scientific_name": "Papaver rhoeas", "category": "fleur",
        "temp_min": 5, "temp_max": 28, "temp_optimal": [10, 25],
        "humidity_min": 30, "humidity_max": 70, "humidity_optimal": [40, 60],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Peu d'eau", "🌸 Laissez monter en graines"],
        "description": "Fleur sauvage emblématique"
    },
    "tournesol": {
        "name": "Tournesol", "scientific_name": "Helianthus annuus", "category": "fleur",
        "temp_min": 15, "temp_max": 35, "temp_optimal": [20, 30],
        "humidity_min": 30, "humidity_max": 70, "humidity_optimal": [40, 60],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Semis direct", "💧 Arrosage régulier", "🌿 Tuteurer si grand vent"],
        "description": "Fleur géante qui suit le soleil"
    },
    "gazania": {
        "name": "Gazania", "scientific_name": "Gazania rigens", "category": "fleur",
        "temp_min": 5, "temp_max": 35, "temp_optimal": [15, 30],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol drainé", "💧 Peu d'eau", "🌸 Fleurs colorées"],
        "description": "Fleur résistante à la sécheresse"
    },
    "verveine": {
        "name": "Verveine", "scientific_name": "Verbena officinalis", "category": "fleur",
        "temp_min": 5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [55, 70],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["🌱 Sol riche", "💧 Arrosage régulier", "🌸 Fleurit longtemps"],
        "description": "Plante médicinale et ornementale"
    },
    
    # ========== PLANTES GRASSES (5) ==========
    "aloe_vera": {
        "name": "Aloe vera", "scientific_name": "Aloe barbadensis", "category": "plante_grasse",
        "temp_min": 10, "temp_max": 35, "temp_optimal": [20, 30],
        "humidity_min": 20, "humidity_max": 50, "humidity_optimal": [30, 40],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Arrosage espacé", "🌿 Sol sablonneux", "🏠 Rentrer l'hiver"],
        "description": "Plante médicinale au gel cicatrisant"
    },
    "cactus": {
        "name": "Cactus", "scientific_name": "Cactaceae", "category": "plante_grasse",
        "temp_min": 5, "temp_max": 40, "temp_optimal": [20, 35],
        "humidity_min": 10, "humidity_max": 40, "humidity_optimal": [20, 30],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "très faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Très peu d'eau", "🌿 Sol très drainant", "❄️ Protéger du gel"],
        "description": "Plante du désert ultra-résistante"
    },
    "crassula": {
        "name": "Crassula", "scientific_name": "Crassula ovata", "category": "plante_grasse",
        "temp_min": 5, "temp_max": 35, "temp_optimal": [15, 28],
        "humidity_min": 20, "humidity_max": 50, "humidity_optimal": [30, 40],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Laisser sécher", "🌿 Bouturage facile", "🏠 Intérieur en hiver"],
        "description": "Plante grasse d'intérieur"
    },
    "sedum": {
        "name": "Sedum", "scientific_name": "Sedum spectabile", "category": "plante_grasse",
        "temp_min": -10, "temp_max": 35, "temp_optimal": [10, 28],
        "humidity_min": 20, "humidity_max": 60, "humidity_optimal": [30, 50],
        "seasons": ["printemps", "été", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Très rustique", "🌸 Fleurs automnales"],
        "description": "Plante grasse de plein air"
    },
    "echeveria": {
        "name": "Echeveria", "scientific_name": "Echeveria", "category": "plante_grasse",
        "temp_min": 5, "temp_max": 30, "temp_optimal": [15, 25],
        "humidity_min": 20, "humidity_max": 50, "humidity_optimal": [30, 40],
        "seasons": ["printemps", "été"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Laisser sécher", "🌿 Sol drainant", "🏠 Intérieur l'hiver"],
        "description": "Rostte décorative aux couleurs pastel"
    },
    
    # ========== ARBRES FRUITIERS (5) ==========
    "pommier": {
        "name": "Pommier", "scientific_name": "Malus domestica", "category": "arbre_fruitier",
        "temp_min": -15, "temp_max": 35, "temp_optimal": [10, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [50, 70],
        "seasons": ["printemps", "automne"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Tailler en hiver", "🌱 Sol riche", "🐛 Traiter contre les maladies"],
        "description": "Arbre fruitier classique"
    },
    "poirier": {
        "name": "Poirier", "scientific_name": "Pyrus communis", "category": "arbre_fruitier",
        "temp_min": -15, "temp_max": 35, "temp_optimal": [10, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [50, 70],
        "seasons": ["printemps", "automne"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Tailler en hiver", "🌱 Sol profond", "💧 Arrosage régulier"],
        "description": "Arbre aux fruits juteux"
    },
    "cerisier": {
        "name": "Cerisier", "scientific_name": "Prunus avium", "category": "arbre_fruitier",
        "temp_min": -15, "temp_max": 30, "temp_optimal": [10, 25],
        "humidity_min": 40, "humidity_max": 80, "humidity_optimal": [50, 70],
        "seasons": ["printemps", "automne"], "difficulty": "moyen",
        "water_needs": "moyen", "sun_needs": "plein soleil",
        "care_tips": ["✂️ Tailler après récolte", "🌱 Sol drainé", "🌸 Fleurs printanières"],
        "description": "Arbre aux fleurs magnifiques"
    },
    "figuier": {
        "name": "Figuier", "scientific_name": "Ficus carica", "category": "arbre_fruitier",
        "temp_min": -5, "temp_max": 40, "temp_optimal": [15, 35],
        "humidity_min": 30, "humidity_max": 70, "humidity_optimal": [40, 60],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Sol pauvre", "✂️ Tailler en mars"],
        "description": "Arbre méditerranéen aux fruits sucrés"
    },
    "olivier": {
        "name": "Olivier", "scientific_name": "Olea europaea", "category": "arbre_fruitier",
        "temp_min": -5, "temp_max": 40, "temp_optimal": [15, 30],
        "humidity_min": 30, "humidity_max": 60, "humidity_optimal": [40, 50],
        "seasons": ["printemps", "automne"], "difficulty": "facile",
        "water_needs": "faible", "sun_needs": "plein soleil",
        "care_tips": ["💧 Peu d'eau", "🌿 Sol drainé", "✂️ Tailler après récolte"],
        "description": "Arbre millénaire méditerranéen"
    }
}

class PlantDatabase:
    def __init__(self):
        self.plants = PLANT_DATABASE
    
    def get_all_plants(self):
        return self.plants
    
    def get_plant(self, name):
        return self.plants.get(name.lower())
    
    def get_plants_info_for_gemini(self):
        """Formate toutes les plantes pour Gemini (RAG)"""
        info = ""
        for name, plant in self.plants.items():
            info += f"""
🌿 **{plant['name']}** ({plant['scientific_name']})
   - Catégorie: {plant['category']}
   - Température: {plant['temp_min']}°C à {plant['temp_max']}°C (optimal: {plant['temp_optimal'][0]}-{plant['temp_optimal'][1]}°C)
   - Humidité: {plant['humidity_min']}% à {plant['humidity_max']}% (optimal: {plant['humidity_optimal'][0]}-{plant['humidity_optimal'][1]}%)
   - Saisons: {', '.join(plant['seasons'])}
   - Difficulté: {plant['difficulty']}
   - Eau: {plant['water_needs']}
   - Soleil: {plant['sun_needs']}
   - Description: {plant['description']}
   - Conseils: {', '.join(plant['care_tips'])}
"""
        return info
    
    def get_plants_count(self):
        return len(self.plants)