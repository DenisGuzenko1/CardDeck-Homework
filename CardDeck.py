import random


def cards():
    list_suits = ['пика', 'крести', 'бубны', 'черви']
    list_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король']
    list_cards = []
    for elem in range(52):
        shuffle_suits = random.choice(list_suits)
        shuffle_numbers = random.choice(list_numbers)
        card = f'{shuffle_suits + " " + shuffle_numbers}'
        list_cards.append(card)
    return list_cards


card_ = cards()
# print(card_)


class CardDeck:
    def __init__(self, card):
        self.card = card

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count >= 52:
            raise StopIteration
        self.count += 1
        try:
            self.this_card = self.card[self.count]
        except IndexError:
            pass
        return self.this_card


card_deck = CardDeck(card_)
elem = iter(card_deck)
for i in elem:
    print(i)
