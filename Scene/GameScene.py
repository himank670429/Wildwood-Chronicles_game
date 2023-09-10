from UI.Button import Button
from UI.Text import Text
from UI.HealthBar import HealthBar

from Entity.Player import Player

from config import *

from Modules.SceneManager import Scene
from Modules.Camera import Camera

class GameScene(Scene):
    def __init__(self, game):
        self.game = game       

    def inilialize(self):
        self.player = Player(
            self.game,
            280, 300
        )
        self.UI = [
            HealthBar(
                self.game,
                self.player,
                self.game.screen,
                20, 20,
                100, 20,
                align = 'topleft'
            )
        ]

        self.actors = [
            self.player
        ]
        self.pause_screen = self.game.pg.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.pause_screen.fill((255, 255, 255, 100))

        self.game_over = False
        self.game_over_screen = self.game.pg.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.game_over_screen.fill((255, 255, 255, 100))
        
        self.camera = Camera(self.game, self.player)
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
        
        self.game_over_screen_ui = [
            Text(
                self.game,
                self.game_over_screen,
                'game over',
                WIDTH/2, HEIGHT/2-20,
                align='center',
                font_size=60,
                tag = 'game over'
            ),
            Button(
                self.game,
                self.game_over_screen,
                self._main_menu,
                WIDTH/2,HEIGHT/2+50,
                200, 50,
                'main menu',
                font_color=(255,0,0),
                font_size=40,
                align='center'
            ),
        ]
        
        self.game.pg.mouse.set_visible(False)

    def _main_menu(self):
        self._resume()
        self.game.pg.mouse.set_visible(True)
        self.game.scene_manager.set_scene(self.game.scenes['MainMenu'])
    
    def _resume(self):
        self.game.global_state['Pause'] = False
        self.game.pg.mouse.set_visible(False)

    def _pause(self):
        self.game.global_state['Pause'] = not self.game.global_state['Pause']
        self.game.pg.mouse.set_visible(True)

    def _quit(self):
        self.game.pg.quit()
        exit()

    def events(self):
        for event in self.game.pg.event.get():
            if event.type == self.game.pg.QUIT:
                self._quit()  
            if event.type == self.game.pg.KEYDOWN:
                if event.key == self.game.pg.K_ESCAPE:
                    if not self.game.global_state['Pause']:
                        self._pause()
                    else:
                        self._resume()
                if event.key == self.game.pg.K_SPACE:
                    self.player.jump()
            if event.type == self.game.pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for ui in self.UI:
                        if ui.mouse_collide(): ui.callback()
                    if self.game.global_state['Pause']:
                        for ui in self.pause_screen_ui:
                            if ui.mouse_collide(): ui.callback()

    def draw(self):
        self.game.map.draw()
        
        for actor in self.actors:
            actor.draw()

        self.game.screen.blit(self.game.map.map_image, (
            self.camera.offsetx,
            self.camera.offsety
        ))

        for ui in self.UI:
            ui.draw()
        
        if self.game_over and not self.game.global_state['Pause']:
            self.game.screen.blit(self.game_over_screen, (0,0))
            for ui in self.game_over_screen_ui: ui.draw()

        if self.game.global_state['Pause']:
            self.game.screen.blit(self.pause_screen, (0,0))
            for ui in self.pause_screen_ui: ui.draw()
    

    def update(self):
        if not self.game.global_state['Pause']:
            for ui in self.UI:
                ui.update()
            for actor in self.actors:
                actor.update()
            self.game.map.update()
            self.camera.update()

            if self.player.health == 0:
                self.game_over = True
                self.game.pg.mouse.set_visible(True)