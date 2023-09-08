import pygame as pg

from UI.Button import Button
from UI.Text import Text

from Entity.Player import Player

from config import *

from Modules.SceneManager import Scene
from Modules.Camera import Camera

class GameScene(Scene):
    def __init__(self, game):
        self.game = game
        self.UI = [
            
        ]
        self.player = Player(
            self.game,
            100, HEIGHT/2
        )

        self.actors = [
            self.player
        ]
        self.pause_screen = pg.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.pause_screen.fill((255, 255, 255, 100))
        self.pause_screen_ui = [
            Text(
                self.game,
                self.pause_screen,
                'Paused',
                WIDTH/2, HEIGHT/2-20,
                align='center',
                font_size=60,
                tag = 'Paused'
            ),
            Button(
                self.game,
                self.game.screen,
                self._resume,
                WIDTH/2,HEIGHT/2+50,
                200, 50,
                'Resume',
                font_color=(255,0,0),
                font_size=40,
                align='center'
            ),
            Button(
                self.game,
                self.game.screen,
                self._main_menu,
                WIDTH/2,HEIGHT/2+130,
                200, 50,
                'Main menu',
                font_color=(255,0,0),
                font_size=40,
                align='center'
            ),
        ]
        self.camera = Camera(self.game)

    def _main_menu(self):
        self._resume()
        self.game.scene_manager.set_scene(self.game.scenes['MainMenu'])
    
    def _resume(self):
        self.game.global_state['Pause'] = False

    def _pause(self):
        self.game.global_state['Pause'] = not self.game.global_state['Pause']

    def _quit(self):
        pg.quit()
        exit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self._quit()  
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self._pause()
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ui in self.UI:
                        if ui.mouse_collide(): ui.callback()
                    if self.game.global_state['Pause']:
                        for ui in self.pause_screen_ui:
                            if ui.mouse_collide(): ui.callback()


    def draw(self):
        for ui in self.UI:
            ui.draw()
        for actor in self.actors:
            actor.draw()
        if self.game.global_state['Pause']:
            self.game.screen.blit(self.pause_screen, (0,0))
            for ui in self.pause_screen_ui: ui.draw()
        self.game.map.draw()
    
    def update(self):
        if not self.game.global_state['Pause']:
            for ui in self.UI:
                ui.update()
            for actor in self.actors:
                actor.update()
            self.game.map.update()