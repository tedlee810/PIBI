import pygame
import pygame.locals

from info.pokemon import Pokemon

pygame.init()

# create game window
game = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Python Monsters Battle Simulator')

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# constants
IV = {'hp': 31, 'attack': 24, 'defense': 10, 'special-attack': 20, 'special-defense': 10, 'speed': 3}
EV = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}
LEVEL = 50

# create Pokémon
## name, level, nature, iv, ev, is_player
lapras = Pokemon('Lapras', LEVEL, 'hasty', IV, EV, True)
lucario = Pokemon('Lucario', LEVEL, 'modest', IV, EV, True)
bulbasaur = Pokemon('Bulbasaur', LEVEL, 'docile', IV, EV, False)
eevee = Pokemon('Eevee', LEVEL, 'quiet', IV, EV, False)

player_team = [lapras, lucario]
rival_team = [bulbasaur, eevee]

def display_message(message):
    # draw a white box with black border
    pygame.draw.rect(game, WHITE, (10, 350, 480, 140))
    pygame.draw.rect(game, BLACK, (10, 350, 480, 140), 3)
    
    # display the message
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game.blit(text, text_rect)
    
    pygame.display.update()

# game loop
game_status = 'select'

game.fill(WHITE)
lapras.draw(game)
lucario.draw(game)
bulbasaur.draw(game)
eevee.draw(game)
display_message('Lapras!') 

lapras.print_moves()

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