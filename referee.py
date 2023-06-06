import random
from info.move import Move
from info.typechart import type_chart

class Referee():
    def __init__(self, player_team, rival_team):
        self.player_team = player_team
        self.rival_team = rival_team
        self.curr_player = player_team[0]
        self.curr_rival = rival_team[0]
        
        self.message_to_display = [] # other helper functions will return a string to be displayed if successful; should be a STACK (with .pop())
        self.first = 'player'
        
        # TODO: add more features
    
    def calc_damage(self, attacking, defending, move):
        if defending.is_protected:
            return
        
        # calculate damage here
        # TODO: type effectiveness, STAB,  etc.
        damage = move.power
        defending.curr_hp -= damage
        
        if defending.curr_hp < 0:
            defending.curr_hp = 0
    
    def deduct_hp(self, game):
        self.calc_damage()
        
        # blit HP deduction animation on screen
        # game.blit(...)
        
    def protect(self, pokemon_name):
        self.message_to_display.append[f'{pokemon_name} protected itself!']
    
    def move_failed(self):
        self.message_to_display.append['But it failed!']
        
    def move_missed(self, pokemon_name):
        self.message_to_display.append[f'{pokemon_name}\'s move missed!']
    
    def did_the_move_land(self, pokemon, move):
        random.seed()
        rand = random.randint(1, 100)
        if rand > move.accuracy:
            self.move_missed(pokemon.name)
            return False
        return True
    
    def who_goes_first(self):
        fastest = None
        if self.curr_player.priority < self.curr_rival.priority:
            return self.curr_rival
        elif self.curr_player.priority > self.curr_rival.priority:
            return self.curr_player
        
        if self.curr_player.speed > self.curr_rival.speed:
            return self.curr_player
        elif self.curr_player.speed < self.curr_rival.speed:
            return self.curr_rival
        
        random.seed()
        if random.randint(1, 50) > 50:
            return self.curr_player
        
        return self.curr_rival
    
    def switch(self):
        pass
    
    def reset(agent):
        agent.priority = 0
        agent.is_protected = False
    
    def perform_move(self, pokemon, move):
        the_move_landed = None
        if move.accuracy == 'null':
            the_move_landed = True
        else:
            the_move_landed = self.did_the_move_land(pokemon, move)
            
        if the_move_landed:
            self.message_to_display.append(f'{pokemon.name} used {move.name}!')