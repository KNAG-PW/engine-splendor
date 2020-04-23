import pandas as pd
from cards.Card import Card


def load_cards_from_file(card_path):
    cards = pd.read_csv(card_path)
    card_list = [[] for _ in range(max(cards.level))]
    for i, c in cards.iterrows():
        card = Card([c.white, c.blue, c.green, c.red, c.black], c.color, c.level, c.points, i)
        card_list[c.level-1].append(card)
    return card_list


class CardList:
    def __init__(self, card_path='data/cards.csv'):
        self.card_list = load_cards_from_file(card_path)

    def get_card_by_level_and_id(self, level, identifier):
        return self.card_list[level-1][identifier]

    def get_cost_of_card(self, level, identifier):
        return self.get_card_by_level_and_id(level, identifier).get_cost()
