import numpy as np

from generation import Generation
from game_params import GameParams
from snake import Snake


class Simulation:
    def __init__(self, num_generations=5, num_individuals=10, mutation_rate=0.1):
        GameParams.MUTATION_RATE = mutation_rate
        self.num_generations = num_generations
        self.num_individuals = num_individuals
        # should eventually only ever store one gen in memory in order to allow for overnight simulations, etc
        self.generation = Generation(self.num_individuals, None, 0, is_random=True)  # First generation is random
        self.prev_generation = None
        self.snake = Snake(GameParams.MAP_SIZE[0]//2, GameParams.MAP_SIZE[1]//2)

    def create_generation_from_prev(self, previous):

        return Generation(self.num_individuals, previous, previous.index + 1)

    def get_current_individual(self):
        gen = self.generation
        return gen.individuals[gen.current_individual]

    def run_step(self):
        next_move = np.asarray(self.get_current_individual().calculate_output_from_map())
        self.snake.move_dir(next_move.argmax())
        if self.snake.is_dead:
            print(self.get_current_individual().index, " died")
            self.next_individual()
            self.snake.is_dead = False
            self.snake.life = self.snake.lifespan

    def next_individual(self):
        has_more_individuals = self.generation.next_individual()
        if not has_more_individuals:
            self.next_generation()

    def next_generation(self):
        print("----------------")
        print("Generation finished", self.generation.index + 1)
        print("----------------")
        sim_complete = (self.generation.index == self.num_generations - 1)
        if not sim_complete:
            self.prev_generation = self.generation
            self.generation = self.create_generation_from_prev(self.prev_generation)
        else:
            print("Simulation complete")
            exit(0)
