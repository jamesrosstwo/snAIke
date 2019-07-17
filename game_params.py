from simulation import Simulation


class GameParams:
    SCORE = 0
    FRAME_RATE = 60
    RES = (260, 60)
    BLOCK_SIZE = 20
    MAP_SIZE = [RES[0] // BLOCK_SIZE, RES[1] // BLOCK_SIZE]
    MAP = []
    SIMULATION = Simulation()
    COLS = {
        "wall": [66, 135, 245],
        "green": [0, 255, 0],
        "snake": [255, 255, 255],
        "bg": [0, 0, 0],
        "fruit": [255, 0, 0]
    }
    # "#": wall, "@": player body, "&": player head, ".": empty space, "*": fruit

