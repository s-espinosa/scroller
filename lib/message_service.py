import requests

class MessageService:
    def __init__(self):
        self.URL = "https://stormy-tundra-72797.herokuapp.com/api/v1/messages"
        self.r = requests.get(url = self.URL)
        self.data = self.r.json()

    def text(self):
        """docstring for text"""
        return self.data["text"]

