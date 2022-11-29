
import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass


player_score = 0
player_last_move = 'rock'
player_move = 0
game_loop = True
replay_loop = True
replay_choice = "y"
round_repeat = True
total_rounds = 0
round_num = 0
round_history = [[]]
cpu_choices = []
cpu_move = ""
computer_score = 0


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def move(self):
        pass


class RandomPlayer(Player):
    def move(self):
        randomChoice = random.choice(moves)
        return randomChoice


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class ReflectPlayer(Player):
    def move(self):
        global player_last_move
        return player_last_move


class CyclePlayer(Player):
    def move(self):
        for i in range(3):
            methods = [Player(), RandomPlayer(), ReflectPlayer()]
            return methods[i]
            i += 1


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def beats(self):
        if (player_move == "paper" and cpu_move == "rock"
           or player_move == "rock"
           and cpu_move == "scissors" or player_move == "scissors"
           and cpu_move == "paper"):
            return True

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        global computer_score
        global player_score
        global player_last_move
        global round_num
        round_repeat = True
        randomChoice = random.choice(moves)
        cpu_move = randomChoice

        while (round_repeat):
            print("\nROUND ", round_num+1, ": \n")
            player_move = input("What's your move?"
                                " 'Paper', 'Scissors' or 'Rock'? ")
            player_move = player_move.lower()
            player_last_move = player_move

            if (player_move == "paper" or player_move == "rock"
               or player_move == "scissors"):
                print("\nHere we go! You chose ", player_move,
                      " The CPU chose ", cpu_move, ".")
                if beats(player_move, cpu_move):

                    player_score += 2
                    print("Good work! You won this round!")
                elif player_move == cpu_move:
                    player_score += 1
                    computer_score += 1
                    print("Looks like both of you had"
                          " the same idea! It's a tie!")
                else:
                    computer_score += 2
                    print("\nYou lose this round!"
                          " He beat you with ", cpu_move, ".")

                print("\nYour score is", player_score)
                print("\nComputer's score is", computer_score)

                round_num += 1
                round_repeat = False
            else:
                print("\nThat input is wrong. Please"
                      "type either 'Paper', 'Scissors' or 'Rock'\n\n")

    def play_game(self):
        global player_score
        global computer_score
        print("\nGame start!")
        for round in range(3):

            self.play_round()
        if (player_score > computer_score):
            print("\nCongratulations! You won the game!")
            print("\nThe general score was: ", player_score,
                  " - ", computer_score, ".")
        elif computer_score > player_score:
            print("\nSorry, the computer won this time.\n")
            print("\nThe general score was: ", computer_score,
                  " - ", player_score, ".")
        else:
            print("\nThis is a tie.\n")
        print("Game over.\n\n")


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
