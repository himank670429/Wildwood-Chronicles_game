# import pygame as pg
from Entity.Wall import Wall
from config import *
class Map:
    def __init__(self, game):
        self.game = game
        self.chapter_1 = [
            Wall(
                self.game, 
                0, HEIGHT-100, 
                WIDTH, 100,
            ),
            Wall(
                self.game,
                -20, 0,
                20, HEIGHT
            ),
            Wall(
                self.game,
                WIDTH, 0,
                20, HEIGHT
            )
        ]
        self.chapter_2 = []
        self.chapter_3 = []
        self.chapter_4 = []
        self.chapter_5 = []
        self.chapter_6 = []
        self.chapter_7 = []

        self.current_map = self.chapter_1

    def draw(self):
        for wall in self.current_map:
            wall.draw() 

    def update(self):
        for wall in self.current_map:
            wall.update()