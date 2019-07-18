import random

from connection import Connection


class Neuron:
    def __init__(self, layer, index, parent_node, is_random=False):
        self.index = index
        self.connections = []
        self.layer = layer
        self.is_random = is_random
        if self.is_random:
            self.activation = random.uniform(0, 1)
        else:
            self.connection_weights = [connection.weight for connection in parent_node.connections]
            self.activation = parent_node.activation

    def connect_to(self, target_node):
        if self.is_random:
            weight = 1
            self.connections.append(Connection(self, target_node, weight, is_random=True))
        else:
            weight = self.connection_weights[target_node.index]
            self.connections.append(Connection(self, target_node, weight, is_random=False))

    def calculate_activation(self):
        out = 0
        num_connections = len(self.connections)
        for connection in self.connections:
            out += connection.dest.activation * connection.weight
        # out /= num_connections  # average activation of connections
        self.activation = out
