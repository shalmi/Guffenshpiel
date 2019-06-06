import random as r

class Player:
    """Represents a player in Guffenshpiel"""

    def __init__(self):
        self.hand = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.discard = []
        self.points = []

    def autoBets(self,flippedCard):
        """Computer should make a smart decision but now just plays randomly"""
        choiceIndex = r.randint(0,len(self.hand)-1)
        cardToBet = self.hand.pop(choiceIndex)
        self.discard.append(cardToBet)
        # print(cardToBet)
        return cardToBet
    
    def askBet(self):
        choice = input("Which card do you want to play?")
        print("you chose {}".format(choice))