import random


class Connection:
    def __init__(self, source, dest, parent_connection, is_random=False):
        self.source = source
        self.dest = dest
        if not is_random:
            self.weight = parent_connection.weight
        else:
            self.weight = random.uniform(0, 1)
