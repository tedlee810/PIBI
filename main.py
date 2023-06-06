import pygame
import pygame.locals

from info.pokemon import Pokemon
from referee import Referee

pygame.init()

# create game window
game = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Python-Based Interactive Battle Interface')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

# constants
ZERO_IV = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}
ZERO_EV = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}
IV = {'hp': 31, 'attack': 24, 'defense': 10, 'special-attack': 20, 'special-defense': 10, 'speed': 3}
EV = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}
LEVEL = 50

# instantiate teams
dummy = Pokemon('Bidoof', 100, 'adamant', ZERO_IV, ZERO_EV, True)
player_team = [dummy, dummy, dummy, dummy, dummy, dummy]
rival_team  = [dummy, dummy, dummy, dummy, dummy, dummy]

# create Pokémon
## name, level, nature, iv, ev, is_player
p1 = Pokemon('Giratina-origin', LEVEL, 'hasty', IV, EV, True)
p2 = Pokemon('Shroomish', LEVEL, 'modest', IV, EV, True)

r1 = Pokemon('Bulbasaur', LEVEL, 'docile', IV, EV, False)
r2 = Pokemon('Eevee', LEVEL, 'quiet', IV, EV, False)

player_team = [p1, p2]
rival_team = [r1, r2]

def display_message(message):
    # draw a black box with white border
    box_dim = lambda l, w: ((1280 - l) / 2, 720 - w - ((1280 - l) / 2))
    
    sw_l, sw_w = 1200, 200
    sw = pygame.Surface((sw_l, sw_w))
    sw.fill(WHITE)
    sw.set_alpha(128)
    game.blit(sw, box_dim(sw_l, sw_w))
    
    sb_l, sb_w = 1185, 185
    sb = pygame.Surface((sb_l, sb_w))
    sb.set_alpha(200)
    sb.fill(BLACK)
    game.blit(sb, box_dim(sb_l, sb_w))
    
    # display the message
    font = pygame.font.Font(pygame.font.get_default_font(), 40)
    text = font.render(message, True, WHITE)
    font_s = pygame.font.Font(pygame.font.get_default_font(), 40)
    text_s = font_s.render(message, True, BLACK)
    
    text_rect = text.get_rect()
    text_s_rect = text_s.get_rect()
    
    text_rect.x, text_rect.y = box_dim(sb_l, sb_w)
    text_rect.x += 25
    text_rect.y += 25
    text_s_rect.x, text_s_rect.y = box_dim(sb_l, sb_w)
    text_s_rect.x += 27
    text_s_rect.y += 27
    
    game.blit(text_s, text_s_rect)
    game.blit(text, text_rect)
    
    pygame.display.update()

# game loop
game_status = 'select'

game.fill(RED)
p1.draw(game)
r1.draw(game)
display_message(f'{p1.name} used Shadow Force!') 

pygame.display.update()

while game_status != 'quit':
    for event in pygame.event.get():
        # QUIT ACTION
        if event.type == pygame.QUIT:
            game_status = 'quit'
        
        # KEY ACTION
        if event.type == pygame.KEYDOWN:
            pass
        
        # CLICK ACTION
        '''if event.type == MOUSEBUTTONDOWN:
            mouse_click = event.pos # position of mouse click
            if game_status == 'select':
                for i in range(len(player_team)):
                    if player_team[i].get_rect().collidepoint(mouse_click):'''
                        
                        
pygame.quit()