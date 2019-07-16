from neuron import Neuron


class Layer:
    # todo: add bias
    def __init__(self, num_nodes, parent_layer, is_random=False):
        if not is_random:
            self.nodes = [Neuron(parent_layer.nodes[i]) for i in range(num_nodes)]
        else:
            self.nodes = [Neuron(None, is_random=True) for i in range(num_nodes)]

    def connect_to(self, layer):
        for src_node in self.nodes:
            for target_node in layer.nodes:
                src_node.connect_to(target_node)
