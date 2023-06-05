import pygame
import pygame.locals
import math
from collections import namedtuple
import requests
from urllib.request import urlopen
import io

from info.move import Move
from info.natures import nature_chart

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, name, level, nature, iv, ev, is_player):
        pygame.sprite.Sprite.__init__(self)

        # connect to PokéAPI
        req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        self.json = req.json()

        # set information
        self.name = name
        self.level = level
        self.nature = nature
        self.iv = iv
        self.ev = ev
        self.stats = {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special-attack": 0,
            "special-defense": 0,
            "speed": 0}

        # set sprite position depending on if the Pokémon belongs to the player or opponent
        if is_player:
            self.x_pos, self.y_pos = 100, 200
        else:
            self.x_pos, self.y_pos = 600, 600

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
        self.moves = []
        self._set_level_up_moves()    
        
        # set sprite info
        self.size = 400
        if is_player:
            self._set_sprite('back_default')
        else:
            self._set_sprite('front_default')
    
    def _set_stat(self, stat):
        ev = self.ev
        iv = self.iv
        level = self.level
        stat_name = stat['stat']['name']

        if stat_name == 'hp':
            self.stats[stat_name] = math.floor(
                ((2 * stat['base_stat'] + iv[stat_name] + math.floor(ev[stat_name] / 4)) 
                 * level) / 100) + level + 10
        else:
            self.stats[stat_name] = math.floor(
                (math.floor(((2 * stat['base_stat'] + iv[stat_name]+ math.floor(ev[stat_name] / 4)) 
                 * level) / 100) + 5) * float(nature_chart.loc[self.nature, stat_name]))
    
    def _set_level_up_moves(self):
        possible_moves = {}

        for i in range(len(self.json['moves'])): # traverse through the moves
            versions = self.json['moves'][i]['version_group_details']
            for j in range(len(versions)): # in each move, get the right details
                game_ver = versions[j]

                # only get moves from Platinum (TODO: to be changed by user)
                if game_ver['version_group']['name'] != 'platinum':
                    continue
                
                # only add level-up moves (no TM moves, etc.)
                if game_ver['move_learn_method']['name'] != 'level-up':
                    continue
                
                # only add moves if the level is high enough
                if self.level < game_ver['level_learned_at']:
                    continue
                
                possible_moves[Move(self.json['moves'][i]['move']['url'])] = game_ver['level_learned_at']
        
        possible_moves = sorted(possible_moves.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(4):
            self.moves.append(possible_moves[i][0])  

    def _set_sprite(self, direction):
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
        
    def draw(self, game, alpha=255):
        sprite = self.image.copy()
        transparency = (255, 255, 255, alpha)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        game.blit(sprite, (self.x_pos, self.y_pos))
    
    # debugging
    def print_moves(self):
        for move in self.moves:
            print(move.name)