from modules.SceneManager import Scene
import pygame as pg
from config import *
from UI.Button import Button
from UI.ToggleButton import ToggleButton
from UI.Text import Text

class SettingsMenu(Scene):
    def __init__(self, game):
        self.game = game
        self.UI = [
            Button(
                self.game,
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
                'Music : ',
                200, 200,
                font_size = 50,
                align = 'rightcenter'
            ),
            ToggleButton(
                self.game, 
                'Music',
                200, 200,
                align= 'leftcenter'
            ),
            Text(
                self.game,
                'Sound : ',
                200, 260,
                font_size = 50,
                align = 'rightcenter'
            ),
            ToggleButton(
                self.game, 
                'Sound',
                200, 260,
                align= 'leftcenter'
            ),
        ]

    def _settings(self):
        self.game.scene_manager.set_scene(self.game.scenes['MainMenu'])

    def _quit(self):
        pg.quit()
        exit()

    def draw(self):
        for ui in self.UI:
            ui.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._quit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for ui in self.UI:
                    if ui.mouse_collide(): ui.callback()

    def update(self):
        for ui in self.UI:
            ui.update()