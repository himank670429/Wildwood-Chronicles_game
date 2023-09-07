import pygame as pg
class Button(pg.sprite.Sprite):
    def __init__(self, game, callback, x, y, width, height, text, font_face = None, font_size = 10, font_color = (255, 255,255), align = 'topleft',  fill = (255, 255, 255)):
        self.game = game
        self.callback = callback if callback else self._default_callback
        self.image = pg.Surface((width,height))
        self.image.fill(fill) if fill else None
        self.rect = self.image.get_rect()
        
        if align == 'topleft': self.rect.topleft = x, y
        elif align == 'bottomleft': self.rect.bottomleft = x, y
        elif align == 'topright': self.rect.topright = x, y
        elif align == 'bottomright': self.rect.bottomright = x, y
        elif align == 'center': self.rect.center = x, y
        elif align == 'topcenter':
            self.rect.centerx = x
            self.rect.top = y
        elif align == 'bottomcenter':
            self.rect.centerx = x
            self.rect.bottom = y
        elif align == 'leftcenter':
            self.rect.centery = y
            self.rect.left = x
        elif align == 'rightcenter':
            self.rect.centery = y
            self.rect.right = x
        else:
            raise Exception('invalid alignment specified')

        self.text = text
        self.font_color = font_color

        self.font = pg.font.Font(font_face, font_size)

    def _default_callback(self):
        pass

    def draw(self):
        text_surf = self.font.render(self.text, True, self.font_color)
        self.image.blit(text_surf, (
            self.image.get_width()/2 - text_surf.get_width()/2,
            self.image.get_height()/2 - text_surf.get_height()/2,
        ))
        self.game.screen.blit(self.image, self.rect)
    
    def mouse_collide(self):
        return self.rect.collidepoint(pg.mouse.get_pos())