import random
from game_params import GameParams


class Fruit:
    def __init__(self, screen, x=-1, y=-1):
        self.screen = screen
        if x == -1 and y == -1:
            self.randomize_pos()
        else:
            self.pos = [x, y]
        GameParams.MAP[self.pos[0]][self.pos[1]] = "*"
        self.draw()

    def randomize_pos(self):
        w = GameParams.MAP_SIZE[0]
        h = GameParams.MAP_SIZE[1]
        _x = random.randrange(1, w-1)
        _y = random.randrange(1, h-1)
        while GameParams.MAP[_x][_y] != ".":
            _x = random.randrange(1, w - 1)
            _y = random.randrange(1, h - 1)
        self.pos = [_x, _y]

    def draw(self):
        b = GameParams.BLOCK_SIZE
        self.screen.fill(
            GameParams.COLS["fruit"],
            (self.pos[0] * b, self.pos[1] * b, b, b)
        )

    def eat(self):
        GameParams.SCORE += 5
        b = GameParams.BLOCK_SIZE
        self.screen.fill(
            GameParams.COLS["bg"],
            (self.pos[0] * b, self.pos[1] * b, b, b)
        )
        GameParams.MAP[self.pos[0]][self.pos[1]] = "."
        self.randomize_pos()
        GameParams.MAP[self.pos[0]][self.pos[1]] = "*"
        self.draw()

