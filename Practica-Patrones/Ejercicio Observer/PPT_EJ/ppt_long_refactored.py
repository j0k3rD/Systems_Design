from random import *

class Scissor():

    type = 'Scissor'

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
        attack_list = [Paper(),Scissor(),Rock()]
        p1_choice = choice(attack_list)
        print(p1_choice)
        p1_play = self._player1.select_atack(p1_choice.type)

        p2_choice = choice(attack_list)
        print(p2_choice)
        p2_play = self._player2.select_atack(p2_choice.type)
    
        options = {
            'Scissor': {
                'Paper': 'Player1 win the round.',
                'Scissor': 'Its a TIE.',
                'Rock': 'Player2 win the round.',
            },
            'Paper': {
                'Paper': 'Its a TIE.',
                'Scissor': 'Player2 win the round.',
                'Rock': 'Player1 win the round.',
            },
            'Rock': {
                'Paper': 'Player2 win the round.',
                'Rock': 'Its a TIE.',
                'Scissor': 'Player1 win the round.'
            }
        }        

        print(options[p1_play][p2_play])

if __name__=="__main__":
    game = Game()
    game.create_player()
    game.fight()