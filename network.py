from layer import Layer
import numpy as np


class Network:
    def __init__(self, layer_template, parent_network, is_random=False):
        self.layers = []
        for idx, i in enumerate(layer_template):
            if is_random:
                self.layers.append(Layer(i, None, is_random=True))
                if idx > 0:
                    # connect to previous layer to ensure each neuron has an array of nodes that influence it
                    self.layers[idx].connect_to(self.layers[idx - 1])
            else:
                self.layers.append(Layer(i, parent_network.layers[idx], False))

        self.fitness = 0

    def calculate_output(self, network_input):
        self.layers[0].set_values(network_input)  # set activations of input layer
        for layer in self.layers[1:]:
            layer.calculate_activations()
        return self.layers[-1].get_activations()


if __name__ == "__main__":
    layer_temp = [10, 5, 4]
    n = Network(layer_temp, None, True)
    network_in = np.random.randint(2, size=10)
    print(n.calculate_output(network_in))
    network_in = np.random.randint(2, size=10)
    print(n.calculate_output(network_in))
