from Board import Board


class Game:

    def __init__(self, n_players):
        assert n_players in [2, 3, 4]
        self.n_players = n_players
        self.board = Board(n_players)
        self.player_round = 0
        self.players = []
        # for i in range(n_players):
        #     self.players.append(Player())
        # self.cards = Card_list()
        # self.magnates = Magnates_list()
        self.cards = []
        self.magnates = []

    def make_move(self, player_number, move_type, **kwargs):

        self.magnates.check_if_player_can_get_magnet(self.players[player_number].get_cards(), self.board.get_available_magnates())

    def buy_card(self, player_number, level, identifier):
        tokens_cost = self.cards.get_cost_of_card(level, identifier)
        self.players[player_number].add_card(level, identifier)
        tokens_removed = self.players[player_number].remove_tokens(tokens_cost)  # if player used gold token it should return it
        self.board.add_tokens(tokens_removed)
        self.board.remove_card(level, identifier)

    def get_tokens(self, player_number, tokens):
        # check if tokens are available
        self.players[player_number].add_tokens(tokens)
        self.board.remove_tokens(tokens)

    def book_card(self, player_number, level, identifier):
        self.players[player_number].add_card_to_hand(level, identifier)
        self.board.remove_card(level, identifier)
        gold_token = self.board.get_gold_token()
        if gold_token[5] > 0:
            self.players[player_number].add_tokens(gold_token)

    def buy_card_from_pocket(self, player_number, level, identifier):
        self.players[player_number].remove_from_hand(level, identifier)
        tokens_cost = self.cards.get_cost_of_card(level, identifier)
        tokens_removed = self.players[player_number].remove_tokens(tokens_cost)  # if player used gold token it should return it
        self.board.add_tokens(tokens_removed)

