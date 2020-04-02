import numpy as np
import pandas as pd

class Nobles_list:
    def __init__(self, nobles_path):
        self.nobles_list = load_nobles_from_file(nobles_path)

