from src.objects.fruit import Fruit
from src.utilities.game_params import GameParams


class Snake:
    def __init__(self, x, y, lifespan=50):
        self.lifespan = lifespan
        self.life = self.lifespan
        self.is_dead = False
        self.head_pos = [x, y]
        self.last_dist = 0
        self.dist = 0
        GameParams.config["snake"]["position"] = self.head_pos
        self.dir = [1, 0]
        GameParams.config["snake"]["direction"] = [1, 0]

        self.starting_length = 8
        self.length = self.starting_length
        self.segments = []
        for i in range(self.length):
            self.segments.append([x - i, y])
        GameParams.map[self.head_pos[0]][self.head_pos[1]] = "&"
        self.fruit = Fruit(GameParams.screen)
        self.draw()
        self.score = 0

    # Control

    def move(self, x, y):
        self.life -= 1
        b = GameParams.config["block_size"]

        if self.life <= 0:
            self.die()
            return

        self.dir = [x, y]
        GameParams.config["snake"]["direction"] = [x, y]
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
            GameParams.screen.fill(GameParams.config["colours"]["bg"], (last[0] * b, last[1] * b, b, b))
            GameParams.map[last[0]][last[1]] = "."

        self.segments.insert(0, self.head_pos)
        GameParams.screen.fill(GameParams.config["colours"]["snake"], (self.head_pos[0] * b, self.head_pos[1] * b, b, b))
        GameParams.map[self.segments[1][0]][self.segments[1][1]] = "@"
        GameParams.map[self.head_pos[0]][self.head_pos[1]] = "&"
        GameParams.config["snake"]["position"] = self.head_pos
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
        self.draw()

    def move_dir(self, direction):
        if direction == 0:
            self.move(0, -1)
        elif direction == 1:
            self.move(1, 0)
        elif direction == 2:
            self.move(0, 1)
        elif direction == 3:
            self.move(-1, 0)

    def move_turn(self, turn):
        dirs = GameParams.config["directions"]
        for i in range(len(dirs)):
            if self.dir == dirs[i]:
                GameParams.config["snake"]["direction_index"] = i
                break
        if turn == -1:  # left
            GameParams.config["snake"]["direction_index"] = (GameParams.config["snake"]["direction_index"]  - 1) % 4
        elif turn == 1:  # right
            GameParams.config["snake"]["direction_index"] = (GameParams.config["snake"]["direction_index"] + 1) % 4
        self.move(dirs[GameParams.config["snake"]["direction_index"]][0], dirs[GameParams.config["snake"]["direction_index"]][1])

    def draw(self):
        b = GameParams.config["block_size"]
        for segment in self.segments:
            GameParams.screen.fill(GameParams.config["colours"]["snake"], (segment[0] * b, segment[1] * b, b, b))

    def check_pos(self, new_pos):
        return GameParams.map[new_pos[0]][new_pos[1]]

    def dist_from_fruit(self):
        offset = [self.fruit.pos[0] - self.head_pos[0], self.fruit.pos[1] - self.head_pos[1]]

        d = abs(offset[0]) + abs(offset[1])
        return d

    def die(self):
        b = GameParams.config["block_size"]
        x = GameParams.map_size[0] // 2
        y = GameParams.map_size[1] // 2

        self.score -= self.dist_from_fruit()
        self.is_dead = True

        for segment in self.segments:
            GameParams.map[segment[0]][segment[1]] = "."
            GameParams.screen.fill(GameParams.config["colours"]["bg"], (segment[0] * b, segment[1] * b, b, b))
        self.segments = []

        self.length = self.starting_length
        self.head_pos = [x, y]
        for i in range(self.length):
            self.segments.append([x - i, y])
        GameParams.map[x][y] = "&"
        self.draw()
        self.dir = [1, 0]
        GameParams.config["snake"]["direction"] = [1, 0]
