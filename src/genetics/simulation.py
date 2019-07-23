import numpy as np

from src.utilities.game_params import GameParams
from src.genetics.generation import Generation
from src.utilities.map_parser import calculate_input_size
from src.objects.snake import Snake


class Simulation:
    def __init__(self):
        input_size = calculate_input_size()
        hidden_layer_size = input_size // 1.5
        GameParams.config["genetics"]["network_template"] = [input_size, hidden_layer_size, 3]
        self.num_generations = GameParams.config["genetics"]["num_generations"]
        self.num_individuals = GameParams.config["genetics"]["individuals_per_generation"]
        self.generation = Generation(self.num_individuals, None, 0, is_random=True)  # First generation is random
        self.prev_generation = None
        self.snake = Snake(GameParams.map_size[0] // 2, GameParams.map_size[1] // 2)

    def get_current_individual(self):
        gen = self.generation
        return gen.individuals[gen.current_individual]

    def run_step(self):
        next_move = np.asarray(self.get_current_individual().calculate_output_from_map())
        self.snake.move_turn(next_move.argmax() - 1)
        if self.snake.is_dead:
            print("snake", self.get_current_individual().index, "died, fitness of:", self.snake.score)
            self.get_current_individual().fitness = self.snake.score
            self.next_individual()
            self.snake.is_dead = False
            self.snake.life = self.snake.lifespan
            self.snake.score = 0

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
            self.generation = Generation(self.num_individuals, self.prev_generation, self.prev_generation.index + 1)
            self.snake.fruit.respawn()
        else:
            print("Simulation complete")
            exit(0)
