import json

class GameParams:
    config = None
    screen = None
    map_size = [0, 0]
    map = []
    # "#": wall, "@": player body, "&": player head, ".": empty space, "*": fruit

    @staticmethod
    def print_map():
        for i in GameParams.map:
            print(i)

    @staticmethod
    def load_config_from_json():
        json_path = "settings.json"
        with open(json_path, 'r') as f:
            return json.load(f)

    @staticmethod
    def calculate_map_size():
        r = GameParams.config["resolution"]
        b = GameParams.config["block_size"]
        return [r[0] // b, r[1] // b]

    @staticmethod
    def init_settings():
        GameParams.config = GameParams.load_config_from_json()
        GameParams.map_size = GameParams.calculate_map_size()
