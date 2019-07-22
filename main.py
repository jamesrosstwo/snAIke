import pygame

from map_parser import *
from simulation import Simulation


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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manually exited by user")
                raise SystemExit
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
