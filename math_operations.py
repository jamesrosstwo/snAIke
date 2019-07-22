import math


def relu(val):
    if val < 0:
        return 0
    return val


def normalize_arr(arr):  # clamp between -1, 1
    out = arr[:]  # shallow copy. Only works on 1D arrays of nums.
    highest = abs(out[0])
    for i in out:
        if abs(i) > highest:
            highest = i
    for i in range(len(out)):
        if highest == 0:
            return out
        out[i] /= highest
    return out


def magnitude(vector):
    return math.sqrt(sum(i * i for i in vector))


def square_magnitude(vector):
    return sum(i * i for i in vector)


def point_offset(point_a, point_b):
    return [b - a for a, b in zip(point_a, point_b)]


def point_distance(point_a, point_b):
    return magnitude(point_offset(point_a, point_b))
