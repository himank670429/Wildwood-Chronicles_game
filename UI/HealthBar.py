from pygame.sprite import Sprite
class HealthBar(Sprite):
    def __init__(self, game, enitity, render_surf, x, y, width, height, align = 'topleft'):
        self.game = game
        self.entity = enitity
        self.render_surf = render_surf
        self.x = x
        self.y = y
        self.width = width
        self.height = height


        self.image = self.game.pg.Surface((width, height))
        self.image.fill((255, 0, 0))
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

        self.fill_image = self.game.pg.Surface((width * (self.entity.health/self.entity.max_health), height))
        self.fill_image.fill((0, 255, 0))
    
    def draw(self):
        self.image.fill((255, 0, 0))
        self.image.blit(self.fill_image, (0,0))
        self.render_surf.blit(self.image, self.rect)
    
    def update(self):
        self.fill_image = self.game.pg.transform.scale(self.fill_image, (self.width * ((self.entity.health/self.entity.max_health)), self.height))
    
    def mouse_collide(self):
        pass