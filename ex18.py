from random import randint

class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def get_suit(self):
        self.suit = randint (0, 3)
        if self.suit == 0:
            return 'Clubs'
        elif self.suit == 1:
            return 'Hearts'
        elif self.suit == 2:
            return 'Diamonds'
        elif self.suit == 3:
            return 'Spades'

        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 2 3 4 5 6 7 8 9 J Q K  A
    def get_value(self):

        if self.value < 8:
            return str(self.value + 2)
        elif self.value == 8:
            return 'Jack'
        elif self.value == 9:
            return 'Queen'
        elif self.value == 10:
            return 'King'
        elif self.value == 11:
            return 'Ace'

    def __str__(self):
        return self.get_value() + ' of ' + self.get_suit()

    class Deck(object):
        def __init__(self):
            self.cards = []
            for suit in range(4):
                for value in range(13):
                    self.cards.append(Card(suit, value))

    def shuffle(self):
        pass

    def deal_hand(self):
        pass

deck = Deck()
my_card = deck.cards[randint(0,51)]
print(my_card)
