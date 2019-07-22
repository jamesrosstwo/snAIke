from fruit import Fruit
from game_params import GameParams
from map_parser import calculate_fruit_activations


class Snake:
    def __init__(self, x, y, lifespan=50):
        self.lifespan = lifespan
        self.life = self.lifespan
        self.is_dead = False
        self.head_pos = [x, y]
        self.last_dist = 0
        self.dist = 0
        GameParams.SNAKE_POS = self.head_pos
        self.dir = [1, 0]
        GameParams.SNAKE_DIR = [1, 0]

        self.starting_length = 8
        self.length = self.starting_length
        self.segments = []
        for i in range(self.length):
            self.segments.append([x - i, y])
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        self.fruit = Fruit(GameParams.SCREEN)
        self.draw()
        self.score = 0

    # Control

    def move(self, x, y):
        self.life -= 1
        b = GameParams.BLOCK_SIZE

        if self.life <= 0:
            self.die()
            return

        # if [x, y] != self.dir:
        #     self.score += 0.1
        self.dir = [x, y]
        GameParams.SNAKE_DIR = [x, y]
        self.head_pos = [x + y for x, y in zip(self.head_pos, self.dir)]

        current_block = self.check_pos(self.head_pos)
        fruit_eaten = False
        if current_block == "*":
            fruit_eaten = True
        elif current_block == "@" or current_block == "#":
            self.die()
            return
        else:  # increase length when fruit is eaten
            last = self.segments.pop()
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (last[0] * b, last[1] * b, b, b))
            GameParams.MAP[last[0]][last[1]] = "."

        self.segments.insert(0, self.head_pos)
        GameParams.SCREEN.fill(GameParams.COLS["snake"], (self.head_pos[0] * b, self.head_pos[1] * b, b, b))
        GameParams.MAP[self.segments[1][0]][self.segments[1][1]] = "@"
        GameParams.MAP[self.head_pos[0]][self.head_pos[1]] = "&"
        GameParams.SNAKE_POS = self.head_pos
        self.last_dist = self.dist
        self.dist = self.dist_from_fruit()
        self.score += 1
        if self.dist <= self.last_dist:
            self.score += 1
        if fruit_eaten:
            self.fruit.respawn()
            self.length += 1
            self.score += 22
            self.life += 50

    def move_dir(self, direction):
        if direction == 0:
            self.move(0, -1)
        elif direction == 1:
            self.move(1, 0)
        elif direction == 2:
            self.move(0, 1)
        elif direction == 3:
            self.move(-1, 0)

    # 1 0, 0 1, -1 0, 0 -1
    def move_turn(self, turn):
        dirs = GameParams.DIRS
        for i in range(len(dirs)):
            if self.dir == dirs[i]:
                GameParams.SNAKE_DIR_IDX = i
                break
        if turn == -1:  # left
            GameParams.SNAKE_DIR_IDX = (GameParams.SNAKE_DIR_IDX - 1) % 4
        elif turn == 1:  # right
            GameParams.SNAKE_DIR_IDX = (GameParams.SNAKE_DIR_IDX + 1) % 4
        self.move(dirs[GameParams.SNAKE_DIR_IDX][0], dirs[GameParams.SNAKE_DIR_IDX][1])

    def draw(self):
        b = GameParams.BLOCK_SIZE
        for segment in self.segments:
            GameParams.SCREEN.fill(GameParams.COLS["snake"], (segment[0] * b, segment[1] * b, b, b))

    def check_pos(self, new_pos):
        return GameParams.MAP[new_pos[0]][new_pos[1]]

    def dist_from_fruit(self):
        offset = [self.fruit.pos[0] - self.head_pos[0], self.fruit.pos[1] - self.head_pos[1]]

        d = abs(offset[0]) + abs(offset[1])
        # print(self.fruit.pos, self.head_pos, offset, d)
        return d

    def die(self):
        b = GameParams.BLOCK_SIZE
        x = GameParams.MAP_SIZE[0] // 2
        y = GameParams.MAP_SIZE[1] // 2

        self.score -= self.dist_from_fruit()

        self.is_dead = True

        for segment in self.segments:
            GameParams.MAP[segment[0]][segment[1]] = "."
            GameParams.SCREEN.fill(GameParams.COLS["bg"], (segment[0] * b, segment[1] * b, b, b))
        self.segments = []

        self.length = self.starting_length
        self.head_pos = [x, y]
        for i in range(self.length):
            self.segments.append([x - i, y])
        GameParams.MAP[x][y] = "&"
        self.draw()
        self.dir = [1, 0]
        GameParams.SNAKE_DIR = [1, 0]
