from Modules.SceneManager import Scene
from config import *
from UI.Button import Button
from UI.ToggleButton import ToggleButton
from UI.Text import Text

class SettingsMenu(Scene):
    def __init__(self, game):
        self.game = game
    
    def inilialize(self):
        self.UI = [
            Button(
                self.game,
                self.game.screen,
                self._settings,
                30, 30,
                140, 50,
                '<- back',
                font_color=(255,0,0),
                font_size=40,
                align='topleft'
            ),
            Text(
                self.game, 
                self.game.screen,
                'Music : ',
                200, 200,
                font_size = 50,
                align = 'rightcenter'
            ),
            ToggleButton(
                self.game, 
                self.game.screen,
                'Music',
                200, 200,
                align= 'leftcenter'
            ),
            Text(
                self.game,
                self.game.screen,
                'Sound : ',
                200, 260,
                font_size = 50,
                align = 'rightcenter'
            ),
            ToggleButton(
                self.game, 
                self.game.screen,
                'Sound',
                200, 260,
                align= 'leftcenter'
            ),
        ]

    def _settings(self):
        self.game.scene_manager.set_scene(self.game.scenes['MainMenu'])

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