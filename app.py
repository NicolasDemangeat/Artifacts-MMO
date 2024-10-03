"""The application controller"""
from hero import Hero


class ApplicationController:
    """Main controller, called when the app start"""

    def __init__(self):
        self.controller = None

    def start(self):
        """define your gameplay loop here"""
        hero = Hero('Darwin')
        hero.make_action('bank/deposit', {"code": "copper", "quantity": 10})
