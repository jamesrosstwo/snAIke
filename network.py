from layer import Layer
from map_parser import generate_network_input
from math_operations import normalize_arr


class Network:

    def __init__(self, generation, layer_template, parent_network, index, is_random=False):
        self.layers = []
        self.index = index
        self.generation = generation
        for idx, i in enumerate(layer_template):
            if is_random:
                self.layers.append(Layer(self, int(i), None, is_random=True))
                if idx > 0:
                    # connect to previous layer to ensure each neuron has an array of nodes that influence it
                    self.layers[idx].connect_to(self.layers[idx - 1])
            else:
                self.layers.append(Layer(self, int(i), parent_network.layers[idx], is_random=False))
                if idx > 0:
                    self.layers[idx].connect_to(self.layers[idx - 1])

        self.fitness = 0

    def calculate_output(self, network_input):
        self.layers[0].set_values(network_input)  # set activations of input layer
        for layer in self.layers[1:]:
            layer.calculate_activations()
        return self.layers[-1].get_activations()

    def calculate_output_from_map(self):
        return normalize_arr(self.calculate_output(generate_network_input()))
