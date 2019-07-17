from network import Network
from game_params import GameParams


class Generation:
    def __init__(self, num_individuals, parent_generation, idx, is_random=False):
        input_size = GameParams.MAP_SIZE[0] * GameParams.MAP_SIZE[1]
        hidden_layer_size = input_size // 1.5
        self.layer_template = [input_size, hidden_layer_size, 4]
        self.individuals = []
        self.index = idx
        self.num_individuals = num_individuals
        for i in range(num_individuals):
            if not is_random:
                self.individuals.append(Network(self.layer_template, parent_generation.individuals[i], i))
            else:
                self.individuals.append(Network(self.layer_template, None, i, is_random=True))
        self.current_individual = 0

    def simulate(self):
        pass

    def next_individual(self):
        print(self.current_individual, self.num_individuals)
        if self.current_individual == self.num_individuals - 1:
            return False
        self.current_individual += 1
        return True

    def select_mating_individuals(self):
        pass
