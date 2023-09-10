from Modules.SceneManager import Scene
from UI.Button import Button
from UI.Text import Text
from config import *
class MainMenu(Scene):
    def __init__(self, game):
        self.game = game
    
    def inilialize(self):
        self.UI = [
            Button(
                self.game,
                self.game.screen,
                self._resume_game,
                WIDTH-70,HEIGHT-280,
                140, 50,
                'Play',
                font_color=(255,0,0),
                font_size=40,
                align='bottomright'
            ),
            Button(
                self.game,
                self.game.screen,
                self._resume_game,
                WIDTH-70,HEIGHT-210,
                140, 50,
                'Resumes',
                font_color=(255,0,0),
                font_size=40,
                align='bottomright'
            ),
            Button(
                self.game,
                self.game.screen,
                self._settings,
                WIDTH-70,HEIGHT-140,
                140, 50,
                'settings',
                font_color=(255,0,0),
                font_size=40,
                align='bottomright'
            ),
            Button(
                self.game,
                self.game.screen,
                self._quit,
                WIDTH-70,HEIGHT-70,
                140, 50,
                'Quit',
                font_color=(255,0,0),
                font_size=40,
                align='bottomright'
            ),
            Text(
                self.game,
                self.game.screen,
                'Wildwood Chronicles',
                20, 60,
                font_size = 70,
                align = 'topleft'
            ),
            Text(
                self.game,
                self.game.screen,
                'The Unseen Realm',
                30, 130,
                font_size = 40,
                align = 'topleft'
            )
        ]
    
    def _play_game(self):
        self.game.scene_manager.set_scene(self.game.scenes['GameScene'])
    
    def _settings(self):
        self.game.scene_manager.set_scene(self.game.scenes['SettingsMenu'])
    
    def _resume_game(self):
        self._play_game()
    
    def _quit(self):
        self.game.pg.quit()
        exit()

    def draw(self):
        for ui in self.UI:
            ui.draw()

    def events(self):
        for event in self.game.pg.event.get():
            if event.type == self.game.pg.QUIT:
                self._quit()
            
            if event.type == self.game.pg.MOUSEBUTTONDOWN and event.button == 1:
                for ui in self.UI:
                    if ui.mouse_collide(): ui.callback()
    
    def update(self):
        for ui in self.UI:
            ui.update()