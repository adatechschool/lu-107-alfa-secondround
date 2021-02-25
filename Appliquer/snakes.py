import random

class Player():
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
        self.pos = 0

class Dice():
    def __init__(self):
        self.value =  random.randint(1,6)

ladders = { 2:38,7:14,8:31,15:26,21:42,28:84,36:44,51:67,78:98,71:91,87:94 }
snakes = { 99:80,95:75,92:88,89:68,74:53,64:60,62:19,46:25,49:11,16:6 }
player1 = Player("Player 1", True)
player2 = Player("Player 2", False)

class SnakesLadders():
    def __init__(self):
        board = []
        for i in range(101):
            board.append(i)

    # def turn(self,player: Player,dice: tuple):
    #     if player.name == 'Player 1':
    #         sname = 'p1'
    #     else:
    #         sname = 'p2'
    #
    #
    #
    #     pass

    def play(self, die1=Dice(), die2=Dice()):

        if player1.turn == True:
            if player2.pos == 100:
                return "Game over!"
            player1.pos += die1.value+die2.value
            if player1.pos == 100:
                return "Player 1 Wins!"
            if player1.pos > 100:
                player1.pos = 100 - (player1.pos-100)
            for k,v in ladders.items():
                if player1.pos == k:
                    player1.pos = v

            for k,v in snakes.items():
                if player1.pos == k:
                    player1.pos = v

            if (die1.value != die2.value):
                player1.turn = False
                player2.turn = True

            return "Player 1 is on square "+str(player1.pos)

        if player2.turn == True:
            if player1.pos == 100:
                return "Game over!"
            player2.pos += die1.value+die2.value
            if player2.pos == 100:
                return "Player 2 Wins!"
            if player2.pos > 100:
                player2.pos = 100 - (player2.pos-100)
            for k,v in ladders.items():
                if player2.pos == k:
                    player2.pos = v

            for k,v in snakes.items():
                if player2.pos == k:
                    player2.pos = v

            if (die1.value != die2.value):
                player2.turn = False
                player1.turn = True

            return "Player 2 is on square "+str(player2.pos)




game = SnakesLadders()
for i in range(40):
    print(game.play(Dice(), Dice()))
