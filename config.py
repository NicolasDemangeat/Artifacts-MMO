"""config file with all the constante
"""
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Définir les constantes
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
API_URL      = os.getenv('API_URL')
ACTION       = os.getenv('ACTION')
PERSONNAGE   = os.getenv('PERSONNAGE')
# Autres constantes qui ne sont pas dans .env
TIMEOUT = 10
MAX_RETRIES = 3
