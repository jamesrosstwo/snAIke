class GameParams:
    SCORE = 0
    FRAME_RATE = 60
    RES = (400, 400)
    BLOCK_SIZE = 20
    SCREEN = None
    SNAKE_POS = [0, 0]
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
