"""move
"""
import time
import requests
from config import BEARER_TOKEN, TIMEOUT, PERSONNAGE, API_URL
from get_map_tile_coord import get_map_tile_coord
from request_helper import RequestHelper

def move(coord):
    """move the perso at the coord

    Args:
        coord (dict): dict with x and y at key 
    """
    action_url   = f"{API_URL}/my/{PERSONNAGE}/action/move"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    response = requests.post(action_url, json=coord, headers=headers, timeout=TIMEOUT)
    print(response.status_code)
    data = response.json()
    destination = data['data']['destination']['content']['code']
    print(f'Vous êtes arrivez a {destination}')
    time.sleep(data['data']['cooldown']['total_seconds'])

def move_hero_to(hero: str, x: int, y: int) -> object:
    result = RequestHelper.post_action(hero.name, 'move', {'x': x, 'y': y})
    if result is not None:
        hero.update_hero(result['character'])
    return hero

move(get_map_tile_coord())
