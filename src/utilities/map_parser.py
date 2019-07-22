from itertools import chain

from src.utilities.game_params import GameParams
from src.utilities.math_operations import *


def calculate_fruit_activations():  # angle to fruit from snake direction
    fruit_offset = point_offset(GameParams.SNAKE_POS, GameParams.FRUIT_POS)
    dir_offset = GameParams.SNAKE_DIR

    a = magnitude(dir_offset)
    b = magnitude(fruit_offset)
    c = point_distance(fruit_offset, dir_offset)
    if a == 0 or b == 0:
        return [0]
    angle = math.acos((a * a + b * b - c * c) / (2 * a * b))

    d = GameParams.SNAKE_DIR_IDX
    left_dist = square_magnitude(point_offset(GameParams.DIRS[(d - 1) % 4], fruit_offset))
    right_dist = square_magnitude(point_offset(GameParams.DIRS[(d + 1) % 4], fruit_offset))
    if left_dist < right_dist:
        angle *= -1
    return [angle]


def one_hot_encode_tile(tile):
    out = [0] * len(GameParams.TILE_MAP)
    out[GameParams.TILE_MAP[tile]] = 1
    return out


def one_hot_encode_tiles(tiles):
    out = tiles
    for x in range(len(out)):
        for y in range(len(out[x])):
            out[x][y] = one_hot_encode_tile(out[x][y])
    return out


def flatten(arr):
    return chain.from_iterable(arr)


def get_visible_tiles():
    out = []
    p = GameParams.SNAKE_POS
    r = GameParams.SNAKE_VISION_RADIUS
    d = GameParams.SNAKE_DIR

    # gets tiles in relation to snake. rotated to match snake's direction.
    if d[1] != 0:
        for y_offset in range(r * d[1], -d[1], -d[1]):
            for x_offset in range(r * d[1], (r * -d[1]) - d[1], -d[1]):
                x = p[0] + x_offset
                y = p[1] + y_offset
                out.extend(one_hot_encode_tile(GameParams.MAP[x][y]))
    else:
        for x_offset in range(r * d[0], -d[0], -d[0]):
            for y_offset in range(r * d[0], (r * -d[0]) - d[0], -d[0]):
                x = p[0] + x_offset
                y = p[1] - y_offset
                out.extend(one_hot_encode_tile(GameParams.MAP[x][y]))

    return out


def generate_network_input():
    out = []
    out.extend(get_visible_tiles())
    out.extend(calculate_fruit_activations())
    return out


def calculate_input_size():
    v_r = GameParams.SNAKE_VISION_RADIUS
    map_input_size = (((2 * v_r) + 1) * (v_r + 1)) * len(GameParams.TILE_MAP)
    fruit_input_size = 1
    return map_input_size + fruit_input_size
