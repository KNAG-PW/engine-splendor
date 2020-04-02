

class Card:
    def __init__(self, cost, colour, level, points, card_id):
        self.cost = cost
        self.colour = colour
        self.level = level
        self.points = points
        self.id = card_id

    def get_cost(self):
        return self.cost

    def get_level(self):
        return self.level

    def get_points(self):
        return self.cost

    def get_colour(self):
        return self.colour

    def get_color(self):
        return self.get_colour()
