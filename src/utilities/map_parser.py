from itertools import chain

from src.utilities.game_params import GameParams
from src.utilities.math_operations import *


def calculate_fruit_activations():  # angle to fruit from snake direction
    fruit_offset = point_offset(GameParams.config["snake"]["position"], GameParams.config["fruit"]["position"])
    dir_offset = GameParams.config["snake"]["direction"]

    a = magnitude(dir_offset)
    b = magnitude(fruit_offset)
    c = point_distance(fruit_offset, dir_offset)
    if a == 0 or b == 0:
        return [0]
    angle = math.acos((a * a + b * b - c * c) / (2 * a * b))

    d = GameParams.config["snake"]["direction_index"]
    left_dist = square_magnitude(point_offset(GameParams.config["directions"][(d - 1) % 4], fruit_offset))
    right_dist = square_magnitude(point_offset(GameParams.config["directions"][(d + 1) % 4], fruit_offset))
    if left_dist < right_dist:
        angle *= -1
    return [angle]


def one_hot_encode_tile(tile):
    out = [0] * len(GameParams.config["tile_map"])
    out[GameParams.config["tile_map"][tile]] = 1
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
    s = GameParams.config["snake"]
    p = s["position"]
    r = s["vision_radius"]
    d = s["direction"]

    # gets tiles in relation to snake. rotated to match snake's direction.
    if d[1] != 0:
        for y_offset in range(r * d[1], -d[1], -d[1]):
            for x_offset in range(r * d[1], (r * -d[1]) - d[1], -d[1]):
                x = p[0] + x_offset
                y = p[1] + y_offset
                out.extend(one_hot_encode_tile(GameParams.map[x][y]))
    else:
        for x_offset in range(r * d[0], -d[0], -d[0]):
            for y_offset in range(r * d[0], (r * -d[0]) - d[0], -d[0]):
                x = p[0] + x_offset
                y = p[1] - y_offset
                out.extend(one_hot_encode_tile(GameParams.map[x][y]))

    return out


def generate_network_input():
    out = []
    out.extend(get_visible_tiles())
    out.extend(calculate_fruit_activations())
    return out


def calculate_input_size():
    v_r = GameParams.config["snake"]["vision_radius"]
    map_input_size = (((2 * v_r) + 1) * (v_r + 1)) * len(GameParams.config["tile_map"])
    fruit_input_size = 1
    return map_input_size + fruit_input_size
