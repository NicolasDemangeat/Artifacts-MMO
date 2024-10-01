"""Module providing gathering loop function."""
import time
import requests
from get_map_tile_coord import get_map_tile_coord
from move import move
from craft import craft
from config import BEARER_TOKEN, TIMEOUT, PERSONNAGE, API_URL, ACTION

def perform_gathering():
    """This function loop gathering
    you can modify the move function to go when you want when full
    """

    action_url   = f"{API_URL}/my/{PERSONNAGE}/action/{ACTION}"

    # Utiliser les variables dans votre code
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    response = requests.post(action_url, headers=headers, timeout=TIMEOUT)

    if response.status_code == 498:
        print('The character cannot be found on your account.')
        return
    if response.status_code == 497:
        print("Your character's inventory is full.")
        move(get_map_tile_coord('workshop', 'mining'))
        return
    if response.status_code == 499:
        print('Your character is in cooldown.')
        data = response.json()
        time.sleep(data['data']['cooldown']['total_seconds'])
        perform_gathering()
    if response.status_code == 493:
        print('The resource is too high-level for your character.')
        move(get_map_tile_coord('resource', 'copper_rocks'))
        perform_gathering()
    if response.status_code == 598:
        print('No resource on this map.')
        move(get_map_tile_coord('resource', 'copper_rocks'))
        perform_gathering()
    if response.status_code != 200:
        print('An error occurred while gathering the resource.')
        return

    if response.status_code == 200:
        data = response.json()
        print('Your character successfully gathered the resource.')
        for item in data['data']['details']['items']: 
            print(f"Vous avez trouvé {item['quantity']} {item['code']}")
        time.sleep(data['data']['cooldown']['total_seconds'])
        perform_gathering()

perform_gathering()
craft('copper')
