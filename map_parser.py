from itertools import chain
import copy
from game_params import GameParams
from math_operations import *


def calculate_fruit_activations():  # 4 offsets (RULD), normalized to a magnitude of 1.
    offsets = normalize_arr([b - a for a, b in zip(GameParams.SNAKE_POS, GameParams.FRUIT_POS)])
    return [relu(offsets[0]), relu(offsets[1]), relu(-offsets[0]), relu(-offsets[1])]


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


def generate_network_input():
    out = []
    p = GameParams.SNAKE_POS
    r = GameParams.SNAKE_VISION_RADIUS
    for x_offset in range(p[0] - r, p[0] + r + 1):
        for y_offset in range(p[1] - r, p[1] + r + 1):
            if x_offset != p[0] or y_offset != p[1]:  # dont check current tile
                # out.append(GameParams.MAP[x_offset][y_offset] == "#")
                out.extend(one_hot_encode_tile(GameParams.MAP[x_offset][y_offset]))
    out.extend(calculate_fruit_activations())
    return out


def calculate_input_size():
    # Size of the square multiplied by the number of tiled (because of one hot), - 5 because of no center tile
    # +4 because of fruit
    return (((2 * GameParams.SNAKE_VISION_RADIUS) + 1) ** 2) * len(GameParams.TILE_MAP) + 4 - len(GameParams.TILE_MAP)
