import sys
import pygame
import time

from snake import Snake
from game_params import GameParams
from simulation import Simulation

pygame.init()


def exit_dead():
    # print("Bugs eaten:\t%d" % (len(SNAKE.elements) - START_LENGTH + 1))
    # print("Score:\t\t%d" % ((len(SNAKE.elements) - START_LENGTH + 1) * DIFFICULTY))
    time.sleep(1)
    pygame.quit()
    sys.exit()


def generate_map():
    layout = []
    for x in range(GameParams.MAP_SIZE[0]):
        layout.append([])
        for y in range(GameParams.MAP_SIZE[1]):
            if x == 0 or x == GameParams.MAP_SIZE[0] - 1 or y == 0 or y == GameParams.MAP_SIZE[1] - 1:
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
    render_map()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manually exited by user")
                raise SystemExit
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_DOWN:
            #         SNAKE.move(0, 1)
            #     elif event.key == pygame.K_UP:
            #         SNAKE.move(0, -1)
            #     elif event.key == pygame.K_LEFT:
            #         SNAKE.move(-1, 0)
            #     elif event.key == pygame.K_RIGHT:
            #         SNAKE.move(1, 0)
        SIMULATION.run_step()
        pygame.display.flip()
        pygame.time.delay(1000 // GameParams.FRAME_RATE)


if __name__ == "__main__":
    GameParams.SCREEN = pygame.display.set_mode(GameParams.RES)
    pygame.display.set_caption("SnAIke")
    tile_map = {}
    pygame.display.flip()
    GameParams.MAP = generate_map()

    SIMULATION = Simulation()
    pygame.display.update()
    game_loop()
