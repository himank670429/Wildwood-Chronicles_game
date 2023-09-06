import pygame as pg
import sys

# local modules
from config import *
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.font.init()

        # variables
        self.screen = pg.display.set_mode((
            WIDTH,
            HEIGHT
        ))
        pg.display.set_caption('1 week game challenge')
        self.clock = pg.time.Clock()
    
    def run(self):
        self.running = True
        while self.running:
            self.dt = 1000/self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def draw(self):
        self.screen.fill(BLACK)
    
    def update(self):
        pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()