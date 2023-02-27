import pygame
from pygame.locals import *
import math
from collections import namedtuple
import requests
from urllib.request import urlopen
import io

from info.natures import nature_chart as nature_chart

pokeAPI_url = 'https://pokeapi.co/api/v2'
Stats = namedtuple('Stats', ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed'])

class Move():
    def __init__(self, url):
        req = requests.get(url)
        self.json = req.json()

        self.name = self.json['name']
        self.power = self.json['power']
        self.type - self.json['type']['name']

class Pokemon(pygame.sprite.Sprite):
    _base_stats = Stats(0, 0, 0, 0, 0, 0) # hp, attack, defense, sp_atk, sp_def, speed

    def __init__(self, name, level, nature, iv, ev, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        # connect to PokéAPI
        req = requests.get(f'{pokeAPI_url}/pokemon/{name.lower()}')
        self.json = req.json()

        # set information
        self.name = name
        self.level = level
        self.nature = nature
        self.iv = iv
        self.ev = ev

        # set sprite position
        self.x_pos = x_pos
        self.y_pos = y_pos

        # set Pokémon's types
        self.types = []
        for i in range(len(self.json['types'])):
            type = self.json['types'][i]
            self.types.append(type['type']['name'])

        # set sprite info
        self.size = 200
        self.set_sprite('front_default')
    
    def _set_stat(self, stat):
        ev = self.ev
        iv = self.iv
        level = self.level
        stats = self.json['stats']

        if stats['stat']['name'] == 'hp':
            return math.floor((2 * stats['base stat'] + iv[0] + math.floor(ev[0] / 4) * level) / 100) + level + 10

        return math.floor((math.floor((2 * stats['base stat'] + iv + math.floor(ev[0] / 4)))) * nature_chart[self.nature, stat]) # TODO: fix i (implement EV structure using switches?)
        
    @property
    def max_hp(self):
        return self._set_stat('hp')
        
    @property
    def attack(self):
        return self._set_stat('attack')
    
    @property  
    def defense(self):
        return self._set_stat('defense')
    
    @property
    def spatk(self):
        return self._set_stat('sp_atk')
    
    @property
    def spdef(self):
        return self._set_stat('sp_def')
    
    @property
    def speed(self):
        return self._set_stat('speed')
    
    def _set_level_up_moves(self):
        self.moves = []

        for i in range(len(self.json['moves'])):
            versions = self.json['moves'][i]['version_group_details']
            for j in range(len(versions)):
                game_ver = versions[j]

                # only get moves from Platinum (TODO: fix to be changed by user)
                if game_ver['version_group']['name'] != 'platinum':
                    continue
                
                # only add level-up moves (no TM moves, etc.)
                if game_ver['move_learn_method']['name'] != 'level-up':
                    continue
                
                # only add moves if the level is high enough
                if self.level >= game_ver['level_learned_at']:
                    continue
                
                # remove oldest move if more than 4 moves
                if len(self.moves) > 4:
                    self.moves.pop(0)
                
                self.moves.append(Move(self.json['moves'][i]['move']['url']))

    def set_sprite(self, direction):
        # set sprite
        image = self.json['sprites'][direction]
        image_stream = urlopen(image).read()
        image_file = io.BytesIO(image_stream)
        self.image = pygame.image.load(image_file).convert_alpha()

        # scale image
        scale = self.size / self.image.get_width()
        new_w = self.image.get_width() * scale
        new_h = self.image.get_height() * scale
        self.image = pygame.transform.scale(self.image, (new_w, new_h))