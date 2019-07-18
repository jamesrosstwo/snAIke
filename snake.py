import math

from fruit import Fruit
from game_params import GameParams


class Snake:
    def __init__(self, x, y, lifespan=50):
        self.lifespan = lifespan
        self.life = self.lifespan
        self.is_dead = False
        self.head_pos = [x, y]
        GameParams.SNAKE_POS = self.head_pos
        self.dir = [1, 0]
        self.starting_length = 2
        self.length = self.starting_length
        self.segments = []
        for i in range(self.length):
            self.segments.append([x - i, y])
            GameParams.MAP[x - i][y] = "@"
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        self.fruit = Fruit(GameParams.SCREEN)
        self.draw()
        self.score = 0

    # Control

    def move(self, x, y):
        old_dist = self.dist_from_fruit()
        self.life -= 1
        if self.life == 0:
            self.die()
            return
        b = GameParams.BLOCK_SIZE
        if (self.dir[0] == x * -1 and x != 0) or (self.dir[1] == y * -1 and y != 0):
            self.life -= 5

        if [x, y] != self.dir:
            self.score += 0.25
        self.dir = [x, y]
        self.head_pos = [x + y for x, y in zip(self.head_pos, self.dir)]

        if self.check_pos(self.head_pos) == "*":
            self.fruit.respawn()
            self.length += 1
            self.score += 22
            self.life += 50

        else:  # increase length when fruit is eaten
            last = self.segments.pop()
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (last[0] * b, last[1] * b, b, b))
            GameParams.MAP[last[0]][last[1]] = "."

        self.segments.insert(0, self.head_pos)
        GameParams.SCREEN.fill(GameParams.COLS["snake"], (self.head_pos[0] * b, self.head_pos[1] * b, b, b))
        GameParams.MAP[self.segments[1][0]][self.segments[1][1]] = "@"
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        GameParams.SNAKE_POS = self.head_pos
        new_dist = self.dist_from_fruit()
        # if new_dist < old_dist:
        #     self.score += old_dist - new_dist
        self.score += 1

    def move_dir(self, direction):
        if direction == 0:
            self.move(0, -1)
        elif direction == 1:
            self.move(1, 0)
        elif direction == 2:
            self.move(0, 1)
        elif direction == 3:
            self.move(-1, 0)

    def draw(self):
        b = GameParams.BLOCK_SIZE
        for segment in self.segments:
            GameParams.SCREEN.fill(GameParams.COLS["snake"], (segment[0] * b, segment[1] * b, b, b))

    def check_pos(self, new_pos):
        current_block = GameParams.MAP[new_pos[0]][new_pos[1]]
        if current_block == "#" or current_block == "@":
            self.die()
        return current_block

    def dist_from_fruit(self):
        offset = [b - a for a, b in zip(self.head_pos, self.fruit.pos)]
        return math.sqrt(offset[0] ** 2 + offset[1] ** 2)

    def die(self):
        b = GameParams.BLOCK_SIZE
        x = GameParams.MAP_SIZE[0] // 2
        y = GameParams.MAP_SIZE[1] // 2

        # self.score -= self.dist_from_fruit() / 8

        self.is_dead = True

        for segment in self.segments:
            GameParams.MAP[segment[0]][segment[1]] = "."
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (segment[0] * b, segment[1] * b, b, b))
        self.segments = []

        self.length = self.starting_length
        self.head_pos = [x, y]
        for i in range(self.length):
            self.segments.append([x - i, y])
            GameParams.MAP[x - i][y] = "@"
        GameParams.MAP[x][y] = "&"
        self.draw()
        self.dir = [1, 0]
