import sys
import pygame
import time
from snake import Snake
from game_params import GameParams

pygame.init()


#
# def create_bug():
#     global BUG
#     BUG = ()
#     while (list(BUG) in WALL) or (list(BUG) in SNAKE.elements) or (not BUG):
#         BUG = (random.randrange(40, RES[0] - 40, 20),
#                (random.randrange(40, RES[1] - 40, 20)))
#
#     pygame.draw.circle(SCREEN, (255, 0, 0), BUG, RADIUS)
#     pygame.display.flip()


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
                SCREEN.fill(
                    GameParams.COLS["wall"],
                    (x * GameParams.BLOCK_SIZE, y * GameParams.BLOCK_SIZE, GameParams.BLOCK_SIZE, GameParams.BLOCK_SIZE)
                )


def game_loop():
    render_map()
    SNAKE.draw(SCREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manually exited by user")
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    SNAKE.move(0, 1)
                elif event.key == pygame.K_UP:
                    SNAKE.move(0, -1)
                elif event.key == pygame.K_LEFT:
                    SNAKE.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    SNAKE.move(1, 0)
        pygame.display.flip()
        pygame.time.delay(1000 // GameParams.FRAME_RATE)


if __name__ == "__main__":
    SCREEN = pygame.display.set_mode(GameParams.RES)
    pygame.display.set_caption("SnAIke")

    pygame.display.flip()
    GameParams.MAP = generate_map()
    SNAKE = Snake(GameParams.MAP_SIZE[0] // 2, GameParams.MAP_SIZE[1] // 2, SCREEN)
    pygame.display.update()

    game_loop()
