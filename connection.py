import random
from game_params import GameParams


class Connection:
    def __init__(self, source, dest, parent_connection, is_random=False):
        self.source = source
        self.dest = dest
        if not is_random:
            self.calculate_weight_from_previous(parent_connection.weight)
        else:
            self.weight = random.uniform(0, 1)

    def calculate_weight_from_previous(self, prev_weight):
        m = GameParams.MUTATION_RATE
        self.weight = prev_weight + random.uniform(-m, m)
