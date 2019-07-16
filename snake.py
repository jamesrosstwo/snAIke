from game_params import GameParams
from fruit import Fruit


class Snake:

    def __init__(self, x, y, screen):
        self.fruit = Fruit(screen)
        self.screen = screen
        self.head_pos = [x, y]
        self.dir = [1, 0]
        self.length = 5
        self.segments = []
        for i in range(self.length):
            self.segments.append([x - i, y])

    def move(self, x, y):
        b = GameParams.BLOCK_SIZE
        if self.dir[0] == x * -1 and x != 0:
            return
        if self.dir[1] == y * -1 and y != 0:
            return
        self.dir = [x, y]
        self.head_pos = [x + y for x, y in zip(self.head_pos, self.dir)]

        if self.check_pos(self.head_pos) == "*":
            self.fruit.eat()
            self.length += 1
        else:  # increase length when fruit is eaten
            last = self.segments.pop()
            self.screen.fill(GameParams.COLS["bg"], (last[0] * b, last[1] * b, b, b))

        self.segments.insert(0, self.head_pos)
        self.screen.fill(GameParams.COLS["snake"], (self.head_pos[0] * b, self.head_pos[1] * b, b, b))
        GameParams.SCORE += 1

    def draw(self, screen):
        b = GameParams.BLOCK_SIZE
        for segment in self.segments:
            screen.fill(GameParams.COLS["snake"], (segment[0] * b, segment[1] * b, b, b))

    def check_pos(self, new_pos):
        current_block = GameParams.MAP[new_pos[0]][new_pos[1]]
        if current_block == "#":
            print("Death")
        if self.head_pos in self.segments[1:]:
            print("Death")

        return current_block
