from random import *

class Sissor():
    type = 'Sissor'

class Paper():
    type = 'Paper'

class Rock():
    type = 'Rock'


class Player():

    def __init__(self, name):
        self.__name = name
    
    def select_atack(self, attack):
        self.attack = attack
        return self.attack

    def get_name(self):
        return self.__name

class Game():

    def create_player(self):
        self._player1 = Player("Player1")
        self._player2 = Player("Player2")

    def fight(self):
        attack_list = [Paper(),Sissor(),Rock()]
        p1_choice = choice(attack_list)
        print(p1_choice)
        p1_play = self._player1.select_atack(p1_choice.type)

        p2_choice = choice(attack_list)
        print(p2_choice)
        p2_play = self._player2.select_atack(p2_choice.type)
    

        if p1_play == 'Sissor' and p2_play == 'Paper':
            print(self._player1.get_name(), 'win the round.')
        elif p1_play == 'Sissor' and p2_play == 'Rock':
            print(self._player2.get_name(), 'win the round.')
        elif p1_play == 'Sissor' and p2_play == 'Sissor':
            print('Its a TIE')
        elif p1_play == 'Rock' and p2_play == 'Paper':
            print(self._player2.get_name(), 'win the round.')
        elif p1_play == 'Rock' and p2_play == 'Rock':
            print('Its a TIE')    
        elif p1_play == 'Rock' and p2_play == 'Sissor':
            print(self._player1.get_name(), 'win the round.')
        elif p1_play == 'Paper' and p2_play == 'Paper':
            print('Its a TIE')    
        elif p1_play == 'Paper' and p2_play == 'Rock':
            print(self._player1.get_name(), 'win the round.')    
        elif p1_play == 'Paper' and p2_play == 'Sissor':
            print(self._player2.get_name(), 'win the round.')                     

if __name__=="__main__":
    game = Game()
    game.create_player()
    game.fight()