import pygame
from pygame.locals import *
import math
from collections import namedtuple
import requests
from urllib.request import urlopen
import io

from info.natures import nature_chart as nature_chart

pokeAPI_url = 'https://pokeapi.co/api/v2'

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
        
    def print(self):
        print(f'Move name: {self.name}')
        print(f'Move power: {self.power}')
        print(f'Move type: {self.type}')

class Pokemon(pygame.sprite.Sprite):
    _stats = {
        "hp": 0,
        "attack": 0,
        "defense": 0,
        "special-attack": 0,
        "special_defense": 0,
        "speed": 0}

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

        # set Pokémon's stats
        base_stats = self.json['stats']
        for stat in base_stats:
            self._set_stat(stat)
            
        # set Pokémon's moves
        self._set_level_up_moves()    
        
        # set sprite info
        self.size = 200
        self.set_sprite('front_default')
    
    def _set_stat(self, stat):
        ev = self.ev
        iv = self.iv
        level = self.level
        stats = self._stats
        stat_name = stat['stat']['name']

        if stat_name == 'hp':
            stats[stat_name] = math.floor(((2 * stat['base_stat'] + iv[stat_name] + math.floor(ev[stat_name] / 4)) * level) / 100) + level + 10
        else:
            stats[stat_name] = math.floor((math.floor(((2 * stat['base_stat'] + iv[stat_name] + math.floor(ev[stat_name] / 4)) * level) / 100) + 5) * float(nature_chart.loc[self.nature, stat_name]))
        
        # print(f'{self.name}\'s {stat_name}: {stats[stat_name]}')
    
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
                if self.level < game_ver['level_learned_at']:
                    continue
                
                # remove oldest move if more than 4 moves
                if len(self.moves) >= 4:
                    self.moves.pop(0)
                
                self.moves.append(Move(self.json['moves'][i]['move']['url'])) # use a queue to overwrite moves once hitting the move limit

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