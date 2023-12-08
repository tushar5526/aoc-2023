import typing
import re


class Card:
    def __init__(self, card_info):
        self.card_info = card_info
        self.card_id = -1
        self.winning_nos = []
        self.card_nos = []
        self._parse_card_info()
        # -1 means not processed, for good old recursion + memo
        self.child_cards_won = -1

    def _parse_card_info(self):
        card, numbers = self.card_info.split(":")
        card = re.sub(" +", " ", card)
        self.card_id = int(card.strip().split(" ")[1])
        self.winning_nos = [
            int(n) for n in numbers.split("|")[0].strip().split(" ") if n
        ]
        self.card_nos = [int(n) for n in numbers.split("|")[1].strip().split(" ") if n]

    def get_len_winning_numbers(self):
        return len(set(self.card_nos).intersection(self.winning_nos))

    def __repr__(self):
        return f"Card(card_id={repr(self.card_id)}, winning_nos={repr(self.winning_nos)}, card_nos={repr(self.card_nos)})"


def calculate_total_cards(card_id, cards_map: typing.Dict[int, Card]):
    if card_id not in cards_map:
        return 0
    card = cards_map[card_id]
    if card.child_cards_won != -1:
        return card.child_cards_won
    winning_nos_len = card.get_len_winning_numbers()
    card.child_cards_won = (
        sum(
            calculate_total_cards(card_id + i + 1, cards_map)
            for i in range(winning_nos_len)
        )
        + 1
    )
    return card.child_cards_won


def solve():
    cards_map = {Card(card_raw).card_id: Card(card_raw) for card_raw in cards_raw}
    return sum(
        calculate_total_cards(card_id + 1, cards_map)
        for card_id in range(len(cards_raw))
    )


if __name__ == "__main__":
    cards_raw = []
    with open("in", "r") as file:
        for line in file:
            cards_raw.append(line.strip())
    print(solve())
