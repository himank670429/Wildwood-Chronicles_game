import pygame as pg
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.game = game
        self.group = game.walls
        super().__init__(self.group)

        self.image = pg.Surface((width, height))
        self.image.fill((100, 100, 200))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
    
    def update(self):
        self.rect.topleft = self.pos
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)