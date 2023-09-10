from Entity.Wall import Wall
import numpy as np
from config import *
from Modules.CSVMapLoader import MapLoader
from os import path
class Map:
    def __init__(self, game):
        self.game = game
        self.map_loader = MapLoader()
        self.levels = {
            'level_1' : {
                'data' : np.array([Wall(self, self.game, int(data[0]), int(data[1]), int(data[2]), int(data[3])) for data in self.map_loader.load_from_file(path.join('assets', 'level', 'level_1.csv'))]),
                'size' : [70, 40]
            },
            'level_2' : {'data' : [], 'size' : []},
            'level_3' : {'data' : [], 'size' : []},
            'level_4' : {'data' : [], 'size' : []},
            'level_5' : {'data' : [], 'size' : []},
            'level_6' : {'data' : [], 'size' : []},
            'level_7' : {'data' : [], 'size' : []},
        }

        self.current_level = self.levels['level_1']
        self.map_image = self.game.pg.Surface((self.current_level['size'][0] * TILE_SIZE, self.current_level['size'][1] * TILE_SIZE))

    def draw(self):
        # draw the wall on the map
        self.map_image.fill(BLACK)
        for wall in self.current_level['data']:
            wall.draw()

    def update(self):
        for wall in self.current_level['data']:
            wall.update()