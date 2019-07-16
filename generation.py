from network import Network
from game_params import GameParams


class Generation:
    def __init__(self, num_individuals, parent_generation, is_random=False):
        input_size = GameParams.MAP_SIZE[0] * GameParams.MAP_SIZE[1]
        hidden_layer_size = input_size // 1.5
        self.layer_template = [input_size, hidden_layer_size, 4]
        self.networks = []
        for i in range(num_individuals):
            if not is_random:
                self.networks.append(Network(self.layer_template, parent_generation.networks[i]))
            else:
                self.networks.append(Network(self.layer_template, None, True))

    def simulate(self):
        pass

    def select_mating_individuals(self):
        pass
