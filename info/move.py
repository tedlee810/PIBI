import requests

class Move():
    def __init__(self, url):
        req = requests.get(url)
        self.json = req.json()

        self.name = self.json['name']
        self.power = self.json['power']
        self.accuracy = self.json['accuracy']
        self.type = self.json['type']['name']
        self.damage_class = self.json['damage_class']
        self.priority = self.json['priority']
        self.pp = self.json['pp']
        self.effect_chance = self.json['effect_chance']
        self.meta = self.json['meta']
    
    # debugging purposes
    def print(self):
        print(f'Move name: {self.name}')
        print(f'Move power: {self.power}')
        print(f'Move type: {self.type}')
        print(f'Move damage class: {self.damage_class}')
        print(f'Move priority: {self.priority}')
        print(f'Move PP: {self.pp}')
        print(f'Move effect chance: {self.effect_chance}')
        print(f'Move meta: {self.meta}')