import requests

class Move():
    def get_description(self, version):
        texts = self.json['flavor_text_entries']
        description = ''
        for i in range(len(texts)):
            # make sure to check for correct version
            if texts[i]['version_group']['name'] != version:
                continue
            
            # make sure to check for correct language
            if texts[i]['language']['name'] != 'en':
                continue
            
            description = texts[i]['flavor_text']
            
        return description.replace('\n', ' ')
    
    def __init__(self, move_name, version):
        req = requests.get(f'https://pokeapi.co/api/v2/move/{move_name}')
        self.json = req.json()

        self.name = self.json['name']
        self.power = self.json['power']
        self.accuracy = self.json['accuracy']
        self.type = self.json['type']['name']
        self.damage_class = self.json['damage_class']['name']
        self.priority = self.json['priority']
        self.pp = self.json['pp']
        self.effect_chance = self.json['effect_chance']
        self.meta = self.json['meta']
        self.target = self.json['target']['name']
        self.description = self.get_description(version)
    
    # debugging purposes
    def print_move_data(self):
        print(f'Move name: {self.name}')
        print(f'Move power: {self.power}')
        print(f'Move type: {self.type}')
        print(f'Move damage class: {self.damage_class}')
        print(f'Move priority: {self.priority}')
        print(f'Move PP: {self.pp}')
        print(f'Move effect chance: {self.effect_chance}')
        print(f'Move description: {self.description}')

# test_move = Move('first-impression', 'ultra-sun-ultra-moon')
# test_move.print_move_data()