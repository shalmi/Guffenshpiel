from Player import Player
from Board import  board

me = Player()
enemy = Player()
board = board()
board.commentary=True

# print(me.hand)

for x in range(14):
    flippedCard = board.flipCard()
    print("Opponent bets: {}".format(enemy.autoBets(flippedCard)))
    me.askBet()