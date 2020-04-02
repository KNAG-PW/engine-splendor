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
