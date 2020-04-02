import numpy as np
import pandas as pd

class Noble:
    def __init__(self, cost, points, id):
        self.cost = cost
        self.id = id
        self.points = points

    def get_cost(self):
        return self.cost

    def get_points(self):
        return self.points
