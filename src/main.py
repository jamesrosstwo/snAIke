import pygame
from src.utilities.map_parser import *
from src.genetics.simulation import Simulation


def generate_map():
    layout = []
    r = GameParams.config["snake"]["vision_radius"]
    for x in range(GameParams.map_size[0]):
        layout.append([])
        for y in range(GameParams.map_size[1]):
            if x < r or (GameParams.map_size[0] - 1 - x) < r or y < r or (GameParams.map_size[0] - 1 - y) < r:
                layout[x].append("#")
            else:
                layout[x].append(".")
    return layout


def render_map():
    b = GameParams.config["block_size"]
    for x in range(GameParams.map_size[0]):
        for y in range(GameParams.map_size[1]):
            if GameParams.map[x][y] == "#":
                GameParams.screen.fill(
                    GameParams.config["colours"]["wall"],
                    (x * b, y * b, b, b)
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
        pygame.time.delay(int(1000 / GameParams.config["framerate"]))


if __name__ == "__main__":
    pygame.init()
    GameParams.init_settings()
    GameParams.screen = pygame.display.set_mode(GameParams.config["resolution"])
    pygame.display.set_caption("SnAIke")
    tile_map = {}
    pygame.display.flip()
    GameParams.map = generate_map()
    pygame.display.update()
    game_loop()
