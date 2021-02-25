import random


class Player:
    def __init__(self, name, turn, pos):
        self.name = name
        self.turn = turn
        self.pos = pos


class Dice:
    def __init__(self):
        self.value = random.randint(1, 6)


class SnakesLadders:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.isFinished = False
        self.winner = None
        self.ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 78: 98, 71: 91, 87: 94}
        self.snakes = {99: 80, 95: 75, 92: 88, 89: 68, 74: 53, 64: 60, 62: 19, 46: 25, 49: 11, 16: 6}

    def play(self, die1, die2):
        sumDices = die1.value + die2.value
        sentenceToReturn = ""


        if self.player1.turn:
            self.player1.pos += sumDices

            if self.player1.pos > 100:
                self.player1.pos = 100 - (self.player1.pos - 100)
            for k, v in self.ladders.items():
                if self.player1.pos == k:
                    self.player1.pos = v
            for k, v in self.snakes.items():
                if self.player1.pos == k:
                    self.player1.pos = v
            sentenceToReturn = "Player 1 is on square " + str(self.player1.pos)
            if die1.value != die2.value:
                self.player1.turn = False
                self.player2.turn = True
        else:
            self.player2.pos += sumDices

            if self.player2.pos > 100:
                self.player2.pos = 100 - (self.player2.pos - 100)
            for k, v in self.ladders.items():
                if self.player2.pos == k:
                    self.player2.pos = v
            for k, v in self.snakes.items():
                if self.player2.pos == k:
                    self.player2.pos = v
            sentenceToReturn = "Player 2 is on square " + str(self.player2.pos)
            if die1.value != die2.value:
                self.player2.turn = False
                self.player1.turn = True

        if self.player2.pos == 100 or self.player1.pos == 100:
            self.isFinished = True
            if self.player1.pos == 100:
                self.winner = self.player1
            else:
                self.winner = self.player2
            return self.winner.name + " Wins!"
        return sentenceToReturn

    def get_winner(self):
        if not self.isFinished:
            raise Exception('you can not get the winner until the game is finished')
        return self.winner


game = SnakesLadders(
    Player("Player 1", True, 0),
    Player("Player 2", False, 0)
)

while not game.isFinished:
    print(game.play(Dice(), Dice()))

winner = game.get_winner()
print(winner.name)
