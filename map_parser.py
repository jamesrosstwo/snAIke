from itertools import chain
import copy
from game_params import GameParams


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
    encoded_tiles = flatten(flatten(one_hot_encode_tiles(new_map)))
    out.extend(encoded_tiles)
    return out
