import pygame
from pygame.locals import *

from info.pokemon import Pokemon as Pokemon
from info.typechart import type_chart as type_chart

pygame.init()

# create game window
game = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Python Monsters Battle Simulator')

# colors
black = (0, 0, 0)
white = (255, 255, 255)

iv = {'hp': 31, 'attack': 24, 'defense': 10, 'special-attack': 20, 'special-defense': 10, 'speed': 3}
ev = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}

# create Pokémon
## name, level, nature, iv, ev, x_pos, y_pos
lapras = Pokemon('Lapras', 25, 'hasty', iv, ev, 100, 100)
lucario = Pokemon('Lucario', 20, 'modest', iv, ev, 150, 400)
bulbasaur = Pokemon('Bulbasaur', 20, 'docile', iv, ev, 250, 500)
eevee = Pokemon('Eevee', 20, 'quiet', iv, ev, 200, 400)

player_team = [lapras, bulbasaur]
rival_team = [lucario, eevee]

def draw(self, alpha=255):
    sprite = self.image.copy()
    transparency = (255, 255, 255, alpha)
    sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
    game.blit(sprite, (self.x_pos, self.y_pos))

# game loop
game_status = 'select'
game.fill(white)

pygame.display.update()

while game_status != 'quit':
    for event in pygame.event.get():
        # QUIT ACTION
        if event.type == QUIT:
            game_status = 'quit'
        
        # KEY ACTION
        if event.type == KEYDOWN:
            if event.key == K_y:
                lapras = Pokemon('Lapras', 25, 'hasty', iv, ev, 100, 100)
                lucario = Pokemon('Lucario', 20, 'modest', iv, ev, 150, 400)
                bulbasaur = Pokemon('Bulbasaur', 20, 'docile', iv, ev, 250, 500)
                eevee = Pokemon('Eevee', 20, 'quiet', iv, ev, 200, 400)
            elif event.key == K_n:
                game_status == 'quit'
        
        # CLICK ACTION
        '''if event.type == MOUSEBUTTONDOWN:
            mouse_click = event.pos # position of mouse click
            if game_status == 'select':
                for i in range(len(player_team)):
                    if player_team[i].get_rect().collidepoint(mouse_click):'''
                        
                        
pygame.quit()