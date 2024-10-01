"""This file give you access to get_map_title_coord function

    Returns:
        _type_: _description_
"""
import requests

from dotenv import load_dotenv

def get_map_tile_coord(content_type = 'bank', content_code = 'bank'):
    """The first parameter is this type of what you want
    The second parameter is the exact code of what you want

    Args:
        content_type (string): Type of content on the map.
        Allowed values:
        monster
        resource
        workshop
        bank
        grand_exchange
        tasks_master
        content_code (_string_): Match pattern: ^[a-zA-Z0-9_-]+$
        You can pass a key word (eg: copper, iron, )

    Returns:
        _dict_: {'x':item['x'], 'y':item['y']}
    """
    # Charger les variables d'environnement depuis le fichier .env
    load_dotenv()

    url = "https://api.artifactsmmo.com/maps"

    querystring = {"content_type":content_type,"content_code":content_code,"size":"100"}

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring, timeout=10)
    data = response.json()['data']
    return {'x': data[0]['x'], 'y': data[0]['y']}
