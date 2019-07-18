class GameParams:
    FRAME_RATE = 1000
    RES = (420, 420)
    BLOCK_SIZE = 20
    MUTATION_RATE = 0
    MUTATION_CHANCE = 0
    PERSISTENT_INDIVIDUALS_PER_GEN = 4
    SCREEN = None
    SNAKE_VISION_RADIUS = 1
    SNAKE_POS = [0, 0]
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
