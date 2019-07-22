import pygame

from game_params import GameParams
from simulation import Simulation
from snake import Snake
from map_parser import *


def generate_map():
    layout = []
    r = GameParams.SNAKE_VISION_RADIUS
    for x in range(GameParams.MAP_SIZE[0]):
        layout.append([])
        for y in range(GameParams.MAP_SIZE[1]):
            if x < r or (GameParams.MAP_SIZE[0] - 1 - x) < r or y < r or (GameParams.MAP_SIZE[0] - 1 - y) < r:
                layout[x].append("#")
            else:
                layout[x].append(".")
    return layout


def render_map():
    for x in range(GameParams.MAP_SIZE[0]):
        for y in range(GameParams.MAP_SIZE[1]):
            if GameParams.MAP[x][y] == "#":
                GameParams.SCREEN.fill(
                    GameParams.COLS["wall"],
                    (x * GameParams.BLOCK_SIZE, y * GameParams.BLOCK_SIZE, GameParams.BLOCK_SIZE, GameParams.BLOCK_SIZE)
                )


def game_loop():
    sim = Simulation()
    render_map()
    # SNAKE = Snake(GameParams.MAP_SIZE[0]//2, GameParams.MAP_SIZE[1]//2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manually exited by user")
                raise SystemExit
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         SNAKE.move_turn(0)
            #     elif event.key == pygame.K_LEFT:
            #         SNAKE.move_turn(-1)
            #     elif event.key == pygame.K_RIGHT:
            #         SNAKE.move_turn(1)
            #     get_visible_tiles()
        sim.run_step()
        pygame.display.flip()
        pygame.time.delay(int(1000 / GameParams.FRAME_RATE))


if __name__ == "__main__":
    pygame.init()
    GameParams.SCREEN = pygame.display.set_mode(GameParams.RES)
    pygame.display.set_caption("SnAIke")
    tile_map = {}
    pygame.display.flip()
    GameParams.MAP = generate_map()

    pygame.display.update()
    game_loop()
