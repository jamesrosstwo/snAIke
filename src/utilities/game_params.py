class GameParams:
    FRAME_RATE = 1000
    RES = (370, 370)
    BLOCK_SIZE = 10
    NETWORK_TEMPLATE = []
    MUTATION_RATE = 0
    MUTATION_CHANCE = 0
    PERSISTENT_INDIVIDUALS_PER_GEN = 4
    SCREEN = None
    SNAKE_VISION_RADIUS = 1
    SNAKE_POS = [0, 0]
    SNAKE_DIR = []
    SNAKE_DIR_IDX = 0
    DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    FRUIT_POS = [0, 0]
    MAP_SIZE = [RES[0] // BLOCK_SIZE, RES[1] // BLOCK_SIZE]
    MAP = []
    COLS = {
        "wall": [66, 135, 245],
        "green": [0, 255, 0],
        "snake": [255, 255, 255],
        "bg": [0, 0, 0],
        "fruit": [255, 0, 0]
    }
    TILE_MAP = {"#": 0, "@": 1, "&": 2, ".": 3, "*": 4}

    # "#": wall, "@": player body, "&": player head, ".": empty space, "*": fruit

    @staticmethod
    def print_map():
        for i in GameParams.MAP:
            print(i)
