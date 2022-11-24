from random import choice, random, seed

class Sissor():

    tipo = "tijera"
    def fight(self, player, enemy_attack):
        if enemy_attack == "piedra":
            return(player, " loose the round")
        elif enemy_attack == "papel":
            return(player, " win the round")
        elif enemy_attack == "tijera":
            print("Its a TIE")

class Paper():

    tipo = "papel"
    def fight(self, player, enemy_attack):
        if enemy_attack == "piedra":
            return(player, " win the round")
        elif enemy_attack == "tijera":
            return(player, " loose the round")
        elif enemy_attack == "papel":
            return('Its a TIE')

class Rock():

    tipo = "piedra"
    def fight(self, player, enemy_attack):
        if enemy_attack == "papel":
            return(player, " loose the round")
        elif enemy_attack == "tijera":
            return(player, " win the round")
        elif enemy_attack == "piedra":
            return('Its a TIE')


class Player():

    def __init__(self, name) -> None:
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

    def round(self):
        seed()
        attack_list = [Sissor(), Paper(), Rock()]
        p1_election = choice(attack_list)
        print(p1_election)
        p1_play = self._player1.select_atack(p1_election.tipo)

        seed()
        p2_election = choice(attack_list)
        print(p2_election)
        p2_play = self._player2.select_atack(p2_election.tipo)

        print(p1_election.fight(self._player1.get_name(),p2_play))


if __name__=="__main__":
    game = Game()
    game.create_player()
    game.round()