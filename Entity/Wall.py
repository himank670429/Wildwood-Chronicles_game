from pygame.sprite import Sprite
from config import *
class Wall(Sprite):
    def __init__(self, map, game, x, y, width, height):
        self.game = game
        self.group = game.walls
        self.map = map
        super().__init__(self.group)

        self.image = self.game.pg.Surface((width*TILE_SIZE, height*TILE_SIZE))
        self.image.fill((100, 100, 200))
        self.pos = (x * TILE_SIZE, y * TILE_SIZE)
        self.w = width
        self.h = height
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
    
    def update(self):
        self.rect.topleft = self.pos
    
    def draw(self):
        self.map.map_image.blit(self.image, self.rect)
    
    # def __str__(self):
    #     return f'<Wall at ({self.rect.x}, {self.rect.y}, {self.w}, {self.h})>'