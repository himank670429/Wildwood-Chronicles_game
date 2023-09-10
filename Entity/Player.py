from pygame.sprite import Sprite
from UI.Button import Button
from UI.Text import Text
from config import *

from Modules.Math import normalize

from Modules.Math import lerp

class Player(Sprite):
    def __init__(self, game,x, y):
        self.game = game
        self.tag = 'Player'
        self.image = self.game.pg.Surface((30, 70))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.pos = self.game.pg.math.Vector2(x, y)  
        self.velocity = self.game.pg.math.Vector2(0, 0) 
         
        self.rect.centerx = self.pos.x
        self.rect.bottom = self.pos.y

        self.state = 'idle'
        self.attack_state = None
        self.attack_timer = {
            'attack_1' : 1000,
            'attack_2' : 800,
        }

        self.last = self.game.pg.time.get_ticks()
        self.ground = None

        self.max_health = PLAYER_HEALTH
        self.health = PLAYER_HEALTH


    def _inputs(self):
        keys = self.game.pg.key.get_pressed()

        # input movement
        if keys[self.game.pg.K_LEFT] or keys[self.game.pg.K_a]: 
            self.velocity.x = lerp(self.velocity.x, -PLAYER_SPEED , PLAYER_SPEED_LERP_FACTOR)
        elif keys[self.game.pg.K_RIGHT]  or keys[self.game.pg.K_d]:
            self.velocity.x = lerp(self.velocity.x, PLAYER_SPEED, PLAYER_SPEED_LERP_FACTOR)
        else:
            self.velocity.x = lerp(self.velocity.x, 0, PLAYER_SPEED_LERP_FACTOR)

        if keys[self.game.pg.K_e]:
            self.heavy_attack()
        if keys[self.game.pg.K_q]:
            self.light_attack()

    def draw(self):
        self.game.map.map_image.blit(self.image, self.rect)

    def update(self):
        self._inputs()

        self.pos.x += self.velocity.x * self.game.dt
        self.rect.centerx = self.pos.x


        ## check for collision
        self.check_x_collision()

        # if keys[self.game.pg.K_UP] or keys[self.game.pg.K_w]: 
        #     self.velocity.y = lerp(self.velocity.y, -PLAYER_SPEED , PLAYER_SPEED_LERP_FACTOR)
        # elif keys[self.game.pg.K_DOWN]  or keys[self.game.pg.K_SPACE]:
        #     self.velocity.y = lerp(self.velocity.y, PLAYER_SPEED, PLAYER_SPEED_LERP_FACTOR)
        # else:
        #     self.velocity.y = lerp(self.velocity.y, 0, PLAYER_SPEED_LERP_FACTOR)


        # # ## add gravity
        self.velocity.y += GRAVITY * self.game.dt
        self.velocity.y = min(self.velocity.y, MAX_GRAVITY)

        self.pos.y += self.velocity.y * self.game.dt
        self.rect.bottom = self.pos.y
        # check for collision
        self.check_y_collision()

        if self.attack_state == 'attack_1' and self.game.pg.time.get_ticks() - self.last < self.attack_timer['attack_1']:
            self.image.fill((255, 255, 255))

        elif self.attack_state == 'attack_2' and self.game.pg.time.get_ticks() - self.last < self.attack_timer['attack_2']:
            self.image.fill((0, 255, 0))
        else:
            self.image.fill((255, 255, 0))
            self.attack_state = None
        
        # print(self.ground)
        if self.rect.bottom > self.game.map.current_level['size'][1] * TILE_SIZE + 1000:
            self.health = 0

    def heavy_attack(self):
        if self.state == 'idle' and self.attack_state == None:
            self.attack_state = 'attack_1'
            self.last = self.game.pg.time.get_ticks()

    def light_attack(self):
        if self.state == 'idle' and self.attack_state == None:
            self.attack_state = 'attack_2'
            self.last = self.game.pg.time.get_ticks()


    def check_x_collision(self):
        for platform in self.game.map.current_level['data']:
            if self.rect.colliderect(platform.rect):
                if self.velocity.x > 0:
                    self.pos.x = platform.rect.left - self.rect.width/2
                elif self.velocity.x < 0:
                    self.pos.x = platform.rect.right + self.rect.width/2
                self.velocity.x = 0
                self.rect.centerx = self.pos.x

    def check_y_collision(self):
        for platform in self.game.map.current_level['data']:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0:
                    if self.velocity.y >= VELOCITY_THRESHOLD:
                        damage = PLAYER_HEALTH * normalize(VELOCITY_THRESHOLD, MAX_GRAVITY, self.velocity.y) * DAMAGE_MULTIPLIER
                        self.health -= damage
                        if self.health < 0:
                            self.health = 0

                    self.pos.y = platform.rect.top
                    self.state = 'idle'
                    self.ground = platform
                elif self.velocity.y < 0:
                    self.pos.y = platform.rect.bottom + self.rect.height
                self.velocity.y = 0
                self.rect.bottom = self.pos.y  

        if self.ground and self.rect.bottom > self.ground.rect.top:
            self.state = 'jump'
            self.ground = None
            
    def jump(self):
        if self.state != 'jump':
            self.velocity.y = JUMP_POWER
            self.state = 'jump'
            self.ground = None
