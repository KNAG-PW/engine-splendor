import numpy as np
import random as random


class Board:
    def __init__(self, n_players):
        self.tokens = self.__get_initial_tokens__(n_players)
        self.board_cards, self.deck = self.__initialize_cards__()
        self.magnates = self.__get_magnets__(n_players)

    def set_up_board(self, n_players):
        self.__init__(n_players)

    def get_available_cards(self):
        return self.board_cards

    def get_available_magnates(self):
        return self.magnates

    def remove_card(self, level, identifier):
        assert self.board_cards[level].__contains__(identifier)
        self.board_cards[level].remove(identifier)
        if self.deck[level].__len__() > 0:
            self.board_cards[level].add(self.deck[level].pop())

    def remove_tokens(self, tokens_to_remove):
        assert np.all(self.tokens - tokens_to_remove >= 0)
        self.tokens = self.tokens - tokens_to_remove

    def add_tokens(self, tokens_to_add):
        self.tokens = self.tokens + tokens_to_add

    def remove_magnates(self, identifier):
        self.magnates.remove(identifier)

    def get_gold_token(self):
        if self.tokens[5] > 0:
            self.tokens[5] -= 1
            return np.array([0, 0, 0, 0, 0, 1])
        else:
            return np.zeros(6, dtype=np.int)

    @staticmethod
    def __get_initial_tokens__(n_players):
        if n_players == 2:
            return np.array([4, 4, 4, 4, 4, 5])
        if n_players == 3:
            return np.array([5, 5, 5, 5, 5, 5])
        if n_players == 4:
            return np.array([7, 7, 7, 7, 7, 5])

    @staticmethod
    def __get_magnets__(n_players):
        return set(random.sample([i for i in range(10)], 1+n_players))

    @staticmethod
    def __initialize_cards__():
        board_cards = []
        deck = []
        for n_cards in [40, 30, 20]:
            cards = random.sample([i for i in range(n_cards)], n_cards)
            board_cards.append(set(cards[:4]))
            deck.append(cards[4:])
        return board_cards, deck

