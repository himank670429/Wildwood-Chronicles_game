import pygame as pg

# local modules
from config import *
from Modules.SceneManager import SceneManager
from Scene.MainMenu import MainMenu
from Scene.SettingsMenu import SettingsMenu
from Scene.GameScene import GameScene
from Modules.Map import Map
from UI.Text import Text

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
            'Sound' : False,
            'Pause' : False
        }
        self.pg = pg
        self.walls = pg.sprite.Group()
        self.map = Map(self)
        self.scenes = {
            "MainMenu" : MainMenu(self),
            "SettingsMenu" : SettingsMenu(self),
            "GameScene" : GameScene(self)
        }
        
        self.scene_manager = SceneManager(self, self.scenes["MainMenu"])

    def initialize(self):
        self.scene_manager.initialize_scene()

    def run(self):
        self.running = True
        self.initialize()
        while self.running:
            self.dt = self.clock.tick(FPS)/1000.0
            self.events()
            self.draw()
            self.update()
    
    def events(self):
        self.scene_manager.handle_scene_events()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.scene_manager.draw_scene()
    
    def update(self):
        pg.display.flip()
        self.scene_manager.update_scene()


if __name__ == "__main__":
    game = Game()
    game.run()