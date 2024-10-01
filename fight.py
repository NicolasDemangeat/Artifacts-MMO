"""_summary_
    """
import time
import requests
from config import BEARER_TOKEN, TIMEOUT

def fight():
    """fight mob on tile
    """
    url = "https://api.artifactsmmo.com/my/Darwin/action/fight"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    response = requests.post(url, headers=headers, timeout=TIMEOUT)
    if response.status_code == 200:
        data = response.json()
        print(f"Vous avez {data['data']['fight']['result']} le combat !")
        print(f"Vous avez gagné {data['data']['fight']['xp']} points d'experience")
        print(f"Vous avez gagné {data['data']['fight']['gold']} d'or")
        for item in data['data']['fight']['drops']:
            print(f"Vous avez trouvé {item['quantity']} {item['code']}")
        time.sleep(data['data']['cooldown']['total_seconds'])
        fight()
    else:
        print(f'erreur : {response.status_code}')
fight()
