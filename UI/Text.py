import pygame as pg
class Text(pg.sprite.Sprite):
    def __init__(self, game, render_surf, text, x, y, font_face = None, font_size = 20, font_color = (255, 255, 255), align = 'topleft', tag = ''):
        self.game = game
        self.render_surf = render_surf
        self.tag = tag
        self.text = text
        self.font_face = font_face
        self.font_size = font_size
        self.font_color = font_color

        self.font = pg.font.Font(font_face, font_size)
        self.text_surf = self.font.render(text, True, font_color)
        self.text_rect = self.text_surf.get_rect()

        if align == 'topleft': self.text_rect.topleft = x, y
        elif align == 'bottomleft': self.text_rect.bottomleft = x, y
        elif align == 'topright': self.text_rect.topright = x, y
        elif align == 'bottomright': self.text_rect.bottomright = x, y
        elif align == 'center': self.text_rect.center = x, y
        elif align == 'topcenter':
            self.text_rect.centerx = x
            self.text_rect.top = y
        elif align == 'bottomcenter':
            self.text_rect.centerx = x
            self.text_rect.bottom = y
        elif align == 'leftcenter':
            self.text_rect.centery = y
            self.text_rect.left = x
        elif align == 'rightcenter':
            self.text_rect.centery = y
            self.text_rect.right = x
        else:
            raise Exception('invalid alignment specified')
    
    def draw(self):
        self.render_surf.blit(self.text_surf, self.text_rect)
    
    def mouse_collide(self):
        return False
