import random

from connection import Connection


class Neuron:
    def __init__(self, parent_node, is_random=False):
        self.connections = []
        if is_random:
            self.activation = random.uniform(0, 1)
        else:
            for i in range(len(parent_node.connections)):
                p_connection = parent_node.connections[i]
                self.connections.append(Connection(p_connection.source, p_connection.dest, p_connection, False))
            self.activation = parent_node.activation

    def connect_to(self, target_node):
        # random weight. connect_to is only called on first gen
        weight = 1
        self.connections.append(Connection(self, target_node, weight, is_random=True))

    def calculate_activation(self):
        out = 0
        num_connections = len(self.connections)
        for connection in self.connections:
            out += connection.dest.activation * connection.weight
        out /= num_connections  # average activation of connections
        self.activation = out

