import numpy as np

from generation import Generation
from game_params import GameParams
from snake import Snake


class Simulation:
    def __init__(self, num_generations=5, num_individuals=10, mutation_rate=0.1):
        self.num_generations = num_generations
        self.num_individuals = num_individuals
        self.mutation_rate = mutation_rate
        # should eventually only ever store one gen in memory in order to allow for overnight simulations, etc
        self.generations = [Generation(self.num_individuals, None, 0, is_random=True)]  # First generation is random
        self.current_generation = 0
        self.snake = Snake(GameParams.MAP_SIZE[0]//2, GameParams.MAP_SIZE[1]//2)

    def create_generation_from_prev(self, previous):
        return Generation(self.num_individuals, previous)

    def get_current_generation(self):
        return self.generations[self.current_generation]

    def get_current_individual(self):
        gen = self.get_current_generation()
        return gen.individuals[gen.current_individual]

    def run_step(self):
        next_move = np.asarray(self.get_current_individual().calculate_output_from_map())
        print(next_move, next_move.argmax())
        self.snake.move_dir(next_move.argmax())
        if self.snake.is_dead:
            self.next_individual()
            self.snake.is_dead = False
            self.snake.life = self.snake.lifespan

    def next_individual(self):
        has_more_individuals = self.get_current_generation().next_individual()
        if not has_more_individuals:
            self.next_generation()

    def next_generation(self):
        sim_complete = (self.current_generation == self.num_generations - 1)
        if not sim_complete:
            self.generations.append(self.create_generation_from_prev(self.get_current_generation()))
            self.current_generation += 1
        else:
            print("Simulation complete")
            exit(0)
