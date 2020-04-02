import numpy as np
import pandas as pd
from cards.Noble import Noble


def load_nobles_from_file(nobles_path):
    nobles = pd.read_csv(nobles_path)
    nobles_list = [Noble([n.white, n.blue, n.green, n.red, n.black], n.points, i) for i, n in nobles.iterrows()]
    return nobles_list


class NoblesList:
    def __init__(self, nobles_path='data/nobles.csv'):
        self.nobles_list = load_nobles_from_file(nobles_path)

    def check_if_player_can_get_noble(self, player_cards, available_magnates):
        for i in available_magnates:
            if self.nobles_list[i].get_cost() <= player_cards:
                return i

    def get_noble_by_id(self, noble_id):
        return self.nobles_list[noble_id]
