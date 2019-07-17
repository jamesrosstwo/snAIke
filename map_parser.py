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
    new_map = copy.deepcopy(GameParams.MAP)
    anchor_pos = GameParams.SNAKE_POS
    for x_offset in range(anchor_pos[0] - 1, anchor_pos[0] + 2):
        for y_offset in range(anchor_pos[1] - 1, anchor_pos[1] + 2):
            if x_offset != 0 or y_offset != 0:  # dont check current tile
                out.extend(one_hot_encode_tile(GameParams.MAP[x_offset][y_offset]))

    out.extend(calculate_fruit_activations())

    encoded_tiles = flatten(flatten(one_hot_encode_tiles(new_map)))
    out.extend(encoded_tiles)
    return out
