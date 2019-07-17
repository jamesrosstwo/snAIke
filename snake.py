from fruit import Fruit
from game_params import GameParams
import numpy as np


class Snake:
    def __init__(self, x, y, lifespan=30):
        self.lifespan = lifespan
        self.life = self.lifespan
        self.is_dead = False
        self.head_pos = [x, y]
        GameParams.SNAKE_POS = self.head_pos
        self.dir = [1, 0]
        self.length = 5
        self.segments = []
        for i in range(self.length):
            self.segments.append([x - i, y])
            GameParams.MAP[x - i][y] = "@"
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        self.fruit = Fruit(GameParams.SCREEN)
        self.draw()

    # Control

    def move(self, x, y):
        self.life -= 1
        if self.life == 0:
            self.die()
            return
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
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (last[0] * b, last[1] * b, b, b))
            GameParams.MAP[last[0]][last[1]] = "."

        self.segments.insert(0, self.head_pos)
        GameParams.SCREEN.fill(GameParams.COLS["snake"], (self.head_pos[0] * b, self.head_pos[1] * b, b, b))
        GameParams.MAP[self.segments[1][0]][self.segments[1][1]] = "@"
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        GameParams.SCORE += 1

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

    def die(self):
        b = GameParams.BLOCK_SIZE
        self.is_dead = True
        x = GameParams.MAP_SIZE[0] // 2
        y = GameParams.MAP_SIZE[1] // 2

        for segment in self.segments:
            GameParams.MAP[segment[0]][segment[1]] = "."
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (segment[0] * b, segment[1] * b, b, b))
        self.segments = []

        self.length = 5
        self.head_pos = [x, y]
        for i in range(self.length):
            self.segments.append([x - i, y])
            GameParams.MAP[x - i][y] = "@"
        GameParams.MAP[x][y] = "&"
        self.draw()
        self.dir = [1, 0]
        print("died")
