# rock papers scissors
# rock beats scissors
# scissors beats paper
# paper beats rock

import random

class Game:
    choices = ["R", "P", "S"]

    def __init__(self):
        self.player1 = Player("CPU" )
        self.player2 = Player("Player")

    def play(self):
        self.player1.choose()
        self.player2.choose()
        self.player1.compare(self.player2)
        self.player1.display(self.player2)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self):
        if(self.name == "CPU"):
            self.choice = random.choice(Game.choices)
        else:
            self.choice = input("Choose R, P, or S: ")
            while self.choice not in Game.choices:
                print ("Invalid choice")
                self.choice = input("Choose R, P, or S: ")
             
   
    def compare(self, other):
        if self.choice == other.choice:
            pass
        elif self.choice == "R" and other.choice == "S":
            self.score += 1
        elif self.choice == "S" and other.choice == "P":
            self.score += 1
        elif self.choice == "P" and other.choice == "R":
            self.score += 1
        else:
            other.score += 1

    def display(self, other):
        print("CPU ({}) : Player ({})".format(self.choice, other.choice))
        print("{} score: {}: {} score: {}".format(self.name, self.score, other.name, other.score))
        # print winner
        if self.score > other.score:
            print("{} wins!".format(self.name))
        elif self.score < other.score:
            print("{} wins!".format(other.name))
        else:
            print("Tie!")
            # restart game
            game.play()

game = Game()
game.play()
   

