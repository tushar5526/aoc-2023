from functools import reduce
class Card:
    def __init__(self, card_info):
        self.card_info = card_info
        self.card_id = -1
        self.winning_nos = []
        self.card_nos = []
        self._parse_card_info()

    def _parse_card_info(self):
        card, numbers = self.card_info.split(':')
        self.card_id = card.strip().split(' ')[1]
        self.winning_nos = [int(n) for n in numbers.split('|')[0].strip().split(' ') if n]
        self.card_nos = [int(n) for n in numbers.split('|')[1].strip().split(' ') if n]

    def points(self):
        intersection_set_len = len(set(self.card_nos).intersection(self.winning_nos))
        return pow(2, intersection_set_len - 1) if intersection_set_len else 0

    def __repr__(self):
        return f"Card(card_id={repr(self.card_id)}, winning_nos={repr(self.winning_nos)}, card_nos={repr(self.card_nos)})"


def solve():
    s = 0
    for card_raw in cards_raw:
        card = Card(card_raw)
        s += card.points()
    return s

if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        for line in file:
            cards_raw.append(line.strip())
    print(solve())
