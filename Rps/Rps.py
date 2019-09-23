import random as rnd


class Rps:
    def __init__(self, first_to):
        self.playerCount = 0
        self.computerCount = 0
        self.first_to = first_to
        self.options = ['rock', 'paper', 'scissors']

    def player_wins(self):
        self.playerCount += 1
        print('Player wins')

    def comp_wins(self):
        self.computerCount += 1
        print('Computer wins')

    @staticmethod
    def draw():
        print('Draw!')

    def choice_rock(self, comp_choice):
        if comp_choice == 'scissors':
            self.player_wins()
        elif comp_choice == 'paper':
            self.comp_wins()

    def choice_paper(self, comp_choice):
        if comp_choice == 'rock':
            self.player_wins()
        elif comp_choice == 'scissors':
            self.comp_wins()

    def choice_scissors(self, comp_choice):
        if comp_choice == 'paper':
            self.player_wins()
        elif comp_choice == 'rock':
            self.comp_wins()

    def run_game(self):
        while self.playerCount < self.first_to and self.computerCount < self.first_to:
            print('Make a choice between rock, paper, scissors')
            player_choice = input()
            computer_choice = rnd.choice(self.options)

            print(player_choice + " - " + computer_choice)

            if player_choice == computer_choice:
                self.draw()
            else:
                if player_choice == 'rock':
                    self.choice_rock(computer_choice)
                elif player_choice == 'paper':
                    self.choice_paper(computer_choice)
                elif player_choice == 'scissors':
                    self.choice_scissors(computer_choice)
                else:
                    print('Not a valid input')

            print('player: ' + str(self.playerCount) + ' vs computer: ' + str(self.computerCount))

        print('Game is over ' + 'player wins' if self.playerCount >= self.first_to else 'computer wins')


def run():
    game_to = int(input('Game to? '))

    t = Rps(game_to)
    t.run_game()
