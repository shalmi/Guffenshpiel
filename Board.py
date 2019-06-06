import random as r
class board:
    """Represents the game's status and abilities\n
    Apparently this game is actually Goofspiel:\n
    https://en.wikipedia.org/wiki/Goofspiel"""

    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.alreadPlayed = []
        self.currentCard = None
        self.commentary = False

    def flipCard(self):
        """Flips a card and returns it\n
            Also prints commentary if self.commentary
            is turned to True."""
        choice = r.randint(0,len(self.deck)-1)
        self.currentCard = self.deck.pop(choice)
        self.alreadPlayed.append(self.currentCard)
        if self.commentary:
            print("Round: {}".format(self.__whichRound()))
            print("Card flipped over: {}".format(self.currentCard))
        return self.currentCard

    
    def __whichRound(self):
        return 14-len(self.deck)