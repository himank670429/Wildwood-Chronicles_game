import pygame as pg
class ToggleButton(pg.sprite.Sprite):
    def __init__(self, game, state_name, x, y, align = 'topleft'):
        self.game = game
        self.state_name = state_name
        self.image = pg.Surface((70, 30))
        self.thumb = pg.Surface((26, 26))
        self.thumb.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.thumb_rect = self.thumb.get_rect()
        
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

        # conditional rendering
        if self.game.global_state[self.state_name]:
            self.image.fill((0, 255, 0))
        else:
            self.image.fill((255, 0, 0))
        self.callback = self.toggle
    def draw(self):
        if self.game.global_state[self.state_name]:
            self.image.fill((0, 150, 0))
            self.image.blit(self.thumb, (
                (self.image.get_width() - self.thumb.get_width()) - 2,
                self.image.get_height()/2 - self.thumb.get_height()/2
            ))
        else:
            self.image.fill((150, 0, 0))
            self.image.blit(self.thumb, (
                2,
                self.image.get_height()/2 - self.thumb.get_height()/2
            ))
        
        self.game.screen.blit(self.image, self.rect)

    def toggle(self):
        self.game.global_state[self.state_name] = not self.game.global_state[self.state_name]

    def mouse_collide(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

