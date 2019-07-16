import random

from connection import Connection


class Neuron:
    def __init__(self, parent_node, is_random=False):
        self.connections = []
        if not is_random:
            for i in range(len(parent_node.connections)):
                p_connection = parent_node.connections[i]
                self.connections.append(Connection(p_connection.source, p_connection.dest, p_connection, False))
            self.value = parent_node.value
        else:
            self.value = random.uniform(0, 1)

    def connect_to(self, target_node):
        # random weight. connect_to is only called on first gen
        weight = 1
        self.connections.append(Connection(self, target_node, weight))
