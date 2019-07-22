import math

from network import Network
from game_params import GameParams


class Generation:
    def __init__(self, num_individuals, parent_generation, idx, is_random=False):
        self.previous_generation = parent_generation
        self.individuals = []
        self.index = idx
        self.num_individuals = num_individuals
        if is_random:
            for i in range(num_individuals):
                self.individuals.append(Network(self, GameParams.NETWORK_TEMPLATE, None, i, is_random=True))
        else:
            self.generate_individuals_from_prev()
        self.current_individual = 0

    def next_individual(self):
        if self.current_individual == self.num_individuals - 1:
            return False
        self.current_individual += 1
        return True

    # could also mutate colour, that would be neat
    def select_persistent_individuals(self):
        sorted_individuals = sorted(self.individuals, key=get_fitness, reverse=True)
        return sorted_individuals[:GameParams.PERSISTENT_INDIVIDUALS_PER_GEN]

    def generate_individuals_from_prev(self):
        size = GameParams.PERSISTENT_INDIVIDUALS_PER_GEN
        persistent = self.previous_generation.select_persistent_individuals()
        for i in range(size):
            self.individuals.append(persistent[i])
        for i in range(size, self.num_individuals):
            idx = math.floor((i/self.num_individuals)*size)
            if idx >= size:
                idx = size
            self.individuals.append(Network(self, GameParams.NETWORK_TEMPLATE, persistent[idx], i))


def get_fitness(individual):
    return individual.fitness
