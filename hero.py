"""Module providing a class to instance a character."""

from config import BEARER_TOKEN, TIMEOUT, API_URL
import requests

class Hero:
    """Character base class.

    This class can be extand.

    Attributes:
        name (string): The name of the character the player want to play.

    Methods:
        methode1(param1, param2): Brève description de methode1.
        methode2(param): Brève description de methode2.
    """
    URL = API_URL
    TOKEN = BEARER_TOKEN
    TIMEOUT = TIMEOUT
    def __init__(self, name):
        """Init of Character.

        Args:
            name (string): The name of the character the player want to play.
        """
        self.name = name
