from config import *
from Modules.Math import clamp, abs
class Camera:
    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.margins = {
            'left' : 200,
            'right' : 200,
            'top' : 160,
            'bottom' : 160,
        }
        self.rect = self.game.pg.Rect(
            self.margins['left'], 
            self.margins['top'], 
            self.game.screen.get_width() - (self.margins['left'] + self.margins['right']),
            self.game.screen.get_height() - (self.margins['top'] + self.margins['bottom']),
        )
        self.offsetx = 0
        self.offsety = 0
    
    def update(self):
        if self.player.rect.right > self.rect.right:
            self.offsetx = (self.rect.right - self.player.rect.right)
        if self.player.rect.left <= self.rect.left:
            self.offsetx = (self.rect.left - self.player.rect.left)

        if self.player.rect.bottom > self.rect.bottom:
            self.offsety = (self.rect.bottom - self.player.rect.bottom)
        if self.player.rect.top <= self.rect.top:
            self.offsety = (self.rect.top - self.player.rect.top)

        self.offsetx = clamp(self.offsetx, (self.game.screen.get_width() - self.game.map.map_image.get_width()), 0)
        self.offsety = clamp(self.offsety, (self.game.screen.get_height() - self.game.map.map_image.get_height()), 0)