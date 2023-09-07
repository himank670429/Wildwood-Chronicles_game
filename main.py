import pygame as pg

# local modules
from config import *
from modules.SceneManager import SceneManager
from Scene.MainMenu import MainMenu
from Scene.SettingsMenu import SettingsMenu

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
        self.global_state = {
            'Music' : False,
            'Sound' : False
        }

        self.scenes = {
            "MainMenu" : MainMenu(self),
            "SettingsMenu" : SettingsMenu(self)
        }
        self.scene_manager = SceneManager(self, self.scenes["MainMenu"])

    
    def run(self):
        self.running = True
        while self.running:
            self.dt = 1000/self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
    
    def events(self):
        self.scene_manager.handle_scene_events()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.scene_manager.draw_scene()
        # pg.draw.line(self.screen, (255, 0, 0), (WIDTH/2, 0), (WIDTH/2, HEIGHT))
        # pg.draw.line(self.screen, (255, 0, 0), (0, HEIGHT/2), (WIDTH, HEIGHT/2))
    
    def update(self):
        self.scene_manager.update_scene()
        pg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()