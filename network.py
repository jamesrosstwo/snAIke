from layer import Layer


class Network:
    def __init__(self, layer_template, parent_network, is_random=False):
        self.layers = []
        for idx, i in enumerate(layer_template):
            if is_random:
                self.layers.append(Layer(i, None, is_random=True))
                if idx > 0:
                    self.layers[idx - 1].connect_to(self.layers[idx])
            else:
                self.layers.append(Layer(i, parent_network.layers[idx], False))

        self.fitness = 0

