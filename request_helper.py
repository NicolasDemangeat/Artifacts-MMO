"""This module contains the RequestHelper class for interacting with the Artifacts MMO API."""
import json
import base64
from typing import Dict, List, Any
from time import sleep
import requests

from config import BEARER_TOKEN, TIMEOUT, API_URL #https://api.artifactsmmo.com

class RequestHelper:
    """A helper class for making API requests to the Artifacts MMO API.

    This class provides two static methods for interacting with the API:
    - post_action: For sending POST requests to perform actions on heroes.
    - get_infos: For sending GET requests to retrieve information.

    Both methods handle authentication, URL construction, and error checking internally.

    Raises:
        ValueError: When an invalid HTTP method is specified.
        requests.RequestException: When the API response status code is not 200.

    Note:
        This class uses configuration variables (BEARER_TOKEN, TIMEOUT, API_URL) 
        imported from a config module.
    """
    @staticmethod
    def __make_url(uri: str) -> str:
        return f"{API_URL}{uri}"

    @staticmethod
    def __request(uri: str, method: str, data: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        url = RequestHelper.__make_url(uri)
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {BEARER_TOKEN}'
        }
        if method == "POST":
            headers['Content-Type'] = 'application/json'
            response = requests.post(url, headers=headers, data=json.dumps(data), timeout=TIMEOUT)
        elif method == "GET":
            response = requests.get(url, headers=headers, params=json.dumps(data), timeout=TIMEOUT)
        else:
            raise ValueError(f"Invalid method: {method}")

        if response.status_code != 200:
            return response.status_code

        data = response.json()
        sleep(data['data']['cooldown']['total_seconds'])
        return data['data']

    @staticmethod
    def __post(uri: str, data: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        return RequestHelper.__request(uri, "POST", data)

    @staticmethod
    def __get(uri: str, data: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        return RequestHelper.__request(uri, "GET", data)

    @staticmethod
    def post_action(hero_name: str, action: str, data: Dict[str, Any]=None) -> List[Dict[str, Any]]:
        """send a POST request to make an action

        Args:
            hero_name (str): one of your hero name
            action (str): the action verb
                (visit : https://api.artifactsmmo.com/docs for the end point)
            data (Dict, optional): the data neded for some request. Defaults to None.

        Returns:
            List: contain the response data
        """
        return RequestHelper.__post(f'/my/{hero_name}/action/{action}', data)

    @staticmethod
    def get_infos(info: str, subinfos: str='', data: Dict[str, Any]=None) -> List[Dict[str, Any]]:
        """send a GET request to get infos

        Args:
            info (str): The keyword of the info you want
            subinfos (str, optional): The keyword for the infos. Defaults to ''.

        Returns:
            List: contain the response data
        """
        return (RequestHelper.__get(f'/my/{info}/{subinfos}', data)
                if subinfos != ''
                else RequestHelper.__get(f'/my/{info}', data))

    @staticmethod
    def get_map_tile_coord(content_code: str):
        """This method return the coord of a tile on the map
        The first parameter is the exact code of what you want
        The second parameter is this type of what you want

        Args:
            content_code (_string_): Match pattern: ^[a-zA-Z0-9_-]+$
            content_type (_string_): Type of content on the map.

        Returns:
            _dict_: {'x':item['x'], 'y':item['y']}
        """

        url = "https://api.artifactsmmo.com/maps"
        querystring = {"content_code": content_code, "size": 100}
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers, params=querystring, timeout=TIMEOUT)

        data = response.json()['data']
        return {'x': data[0]['x'], 'y': data[0]['y']}

    @staticmethod
    def create_account(username: str, password: str, email: str):
        """This method create an account, generate token, and return the token

        Args:
            username (_string_): the username for the account
            password (_string_): Password for the account
            email (_string_): user email

        Returns:
            _string_: Bearrer token
        """

        url = "https://api.artifactsmmo.com/accounts/create"
        payload = {
            "username": username,
            "password": password,
            "email": email
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)

        url = "https://api.artifactsmmo.com/token"
        # Encodage des identifiants en Base64 pour l'authentification Basic
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Basic {encoded_credentials}"
        }

        # Vérification de la réponse
        if response.status_code == 200:
            token = response.json()["token"]
            print(f"Token généré avec succès : {token}")
            return token
        else:
            print(f"Erreur lors de la génération du token : {response.status_code}")
            print(response.json())
