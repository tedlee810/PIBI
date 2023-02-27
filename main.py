import pygame
from pygame.locals import *

from info.pokemon import Pokemon as Pokemon
from info.typechart import type_chart as type_chart

pygame.init()

# create game window
game = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pythonmon Battle Simulator')

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# create Pokémon
## name, level, nature, iv, ev, x_pos, y_pos
iv = (31, 24, 10, 20, 10, 3)
ev = (0, 0, 0, 0, 0, 0, 0)

lapras = Pokemon('Lapras', 25, 'hasty', iv, ev, 100, 100)
lucario = Pokemon('Lucario', 20, 'modest', iv, ev, 150, 400)
monferno = Pokemon('Monferno', 20, 'jolly', iv, ev, 200, 300)
bulbasaur = Pokemon('Bulbasaur', 20, 'docile', iv, ev, 250, 500)
eevee = Pokemon("Eevee", 20, 'quiet', iv, ev, 200, 400)

player_team = [lapras, bulbasaur]
rival_team = [lucario, monferno]

def draw(self, alpha=255):
    sprite = self.image.copy()
    transparency = (255, 255, 255, alpha)
    sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
    game.blit(sprite, (self.x_pos, self.y_pos))

# game loop
game_status = 'select'
game.fill(white)
draw(lapras)
draw(lucario)
draw(monferno)
draw(bulbasaur)
draw(eevee)

pygame.display.update()

while game_status != 'quit':
    for event in pygame.event.get():
        # quit action
        if event.type == QUIT:
            game_status = 'quit'
        
        # click action
        '''if event.type == MOUSEBUTTONDOWN:
            mouse_click = event.pos # position of mouse click
            if game_status == 'select':
                for i in range(len(player_team)):
                    if player_team[i].get_rect().collidepoint(mouse_click):'''
                        
                        
pygame.quit()