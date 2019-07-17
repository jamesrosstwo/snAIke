from neuron import Neuron


class Layer:
    # todo: add bias
    def __init__(self, num_neurons, parent_layer, is_random=False):
        if is_random:
            self.neurons = [Neuron(None, is_random=True) for i in range(num_neurons)]
        else:
            self.neurons = [Neuron(parent_layer.nodes[i]) for i in range(num_neurons)]

    def connect_to(self, layer):
        for src_neuron in self.neurons:
            for target_neuron in layer.neurons:
                src_neuron.connect_to(target_neuron)

    def set_values(self, vals):
        for idx, neuron in enumerate(self.neurons):
            neuron.activation = vals[idx]

    def calculate_activations(self):
        for neuron in self.neurons:
            neuron.calculate_activation()

    def get_activations(self):
        out = []
        for neuron in self.neurons:
            out.append(neuron.activation)
        return out
