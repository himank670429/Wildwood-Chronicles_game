import pygame as pg
from UI.Button import Button
from UI.Text import Text
from config import *

from Modules.Math import lerp

class Player(pg.sprite.Sprite):
    def __init__(self, game,x, y):
        self.game = game
        self.tag = 'Player'
        self.image = pg.Surface((30, 100))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.pos = pg.math.Vector2(x, y)  
        self.velocity = pg.math.Vector2(0, 0) 
         
        self.rect.centerx = self.pos.x
        self.rect.bottom = self.pos.y

        self.on_ground = False
    
    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def event(self):
        pass
    
    def update(self):
        keys = pg.key.get_pressed()

        # input movement
        if keys[pg.K_LEFT] or keys[pg.K_a]: 
            self.velocity.x = lerp(self.velocity.x, -PLAYER_SPEED , PLAYER_SPEED_LERP_FACTOR)
        elif keys[pg.K_RIGHT]  or keys[pg.K_d]:
            self.velocity.x = lerp(self.velocity.x, PLAYER_SPEED, PLAYER_SPEED_LERP_FACTOR)
        else:
            self.velocity.x = lerp(self.velocity.x, 0, PLAYER_SPEED_LERP_FACTOR)

        self.pos.x += self.velocity.x * self.game.dt
        self.rect.centerx = self.pos.x


        ## check for collision
        self.check_x_collision()
   

        ## add gravity
        self.velocity.y += GRAVITY * self.game.dt
        self.velocity.y = min(self.velocity.y, MAX_GRAVITY)

        self.pos.y += self.velocity.y * self.game.dt
        self.rect.bottom = self.pos.y
        # check for collision
        self.check_y_collision()


    def check_x_collision(self):
        for platform in self.game.map.current_map:
            if self.rect.colliderect(platform.rect):
                if self.velocity.x > 0:
                    self.pos.x = platform.rect.left - self.rect.width/2
                elif self.velocity.x < 0:
                    self.pos.x = platform.rect.right + self.rect.width/2
                self.velocity.x = 0
                self.rect.centerx = self.pos.x

    def check_y_collision(self):
         for platform in self.game.map.current_map:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    self.pos.y = platform.rect.top
                    self.on_ground = True
                elif self.velocity.y < 0:
                    self.pos.y = platform.rect.bottom
                self.velocity.y = 0
                self.rect.bottom = self.pos.y


    def jump(self):
        if self.on_ground:
            self.velocity.y = JUMP_POWER
            self.on_ground = False
