from generation import Generation


class Simulation:
    def __init__(self, num_generations=5, num_individuals=10, mutation_rate=0.1):
        self.num_generations = num_generations
        self.num_individuals = num_individuals
        self.mutation_rate = mutation_rate
        self.generations = []

    def create_generation_from_prev(self, previous):
        return Generation(self.num_individuals, previous)

    def run(self):
        self.generations.append(Generation(self.num_individuals, None, True))  # First generation is random
        for i in range(self.num_generations - 1):
            print("Generation", i)
            self.generations[i].run()
            self.generations.append(self.create_generation_from_prev(self.generations[i]))
