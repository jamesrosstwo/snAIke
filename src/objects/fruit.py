import random

from src.utilities.game_params import GameParams


class Fruit:
    def __init__(self, screen, x=-1, y=-1):
        self.screen = screen
        if x == -1 and y == -1:
            self.randomize_pos()
        else:
            self.pos = [x, y]
        GameParams.map[self.pos[0]][self.pos[1]] = "*"
        self.draw()

    def randomize_pos(self):
        w = GameParams.map_size[0]
        h = GameParams.map_size[1]
        _x = random.randrange(1, w - 1)
        _y = random.randrange(1, h - 1)
        while GameParams.map[_x][_y] != ".":
            _x = random.randrange(1, w - 1)
            _y = random.randrange(1, h - 1)
        self.pos = [_x, _y]

    def draw(self):
        b = GameParams.config["block_size"]
        self.screen.fill(
            GameParams.config["colours"]["fruit"],
            (self.pos[0] * b, self.pos[1] * b, b, b)
        )
        GameParams.config["fruit"]["position"] = self.pos

    def respawn(self):
        b = GameParams.config["block_size"]
        self.screen.fill(
            GameParams.config["colours"]["bg"],
            (self.pos[0] * b, self.pos[1] * b, b, b)
        )
        GameParams.map[self.pos[0]][self.pos[1]] = "."
        self.randomize_pos()
        GameParams.map[self.pos[0]][self.pos[1]] = "*"
        self.draw()
