"""craft
"""
import time
import math
import requests
from config import BEARER_TOKEN, TIMEOUT, PERSONNAGE, API_URL

def craft(item_code):
    """craft item
    Args:
        item_code (string) : the name of what you want to craft
    """
# we search the data of the item to craft
    url_item       = f"https://api.artifactsmmo.com/items/{item_code}"
    headers_item   = {"Accept": "application/json"}
    response_item  = requests.get(url_item, headers=headers_item, timeout=TIMEOUT)
    data_item      = response_item.json()
    craft_item_qty = data_item['data']['item']['craft']['items'][0]['quantity']
    craft_item_code = data_item['data']['item']['craft']['items'][0]['code']


    url_perso      = "https://api.artifactsmmo.com/characters/Darwin"
    response_perso = requests.get(url_perso, headers=headers_item, timeout=TIMEOUT)
    data_perso = response_perso.json()
    inventory_list = data_perso['data']['inventory']
    for el in inventory_list:
        if el['code'] == craft_item_code:
            nb_item_craft_inventory = el['quantity']

    action_url   = f"{API_URL}/my/{PERSONNAGE}/action/crafting"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    item = {
    "code": f"{item_code}",
    "quantity": math.floor(nb_item_craft_inventory / craft_item_qty)
    }

    response = requests.post(action_url, json=item, headers=headers, timeout=TIMEOUT)
    data = response.json()
    time.sleep(data['data']['cooldown']['total_seconds'])
