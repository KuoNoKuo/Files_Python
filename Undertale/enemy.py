import pygame
import pygame as pygame
from variables import*
import math
from variables import hit

spirit = [
    pygame.image.load('img/frame_00_delay-0.03s.png'),
    pygame.image.load('img/frame_01_delay-0.03s.png'),
    pygame.image.load('img/frame_02_delay-0.03s.png'),
    pygame.image.load('img/frame_03_delay-0.03s.png'),
    pygame.image.load('img/frame_04_delay-0.03s.png'),
    pygame.image.load('img/frame_05_delay-0.03s.png'),
    pygame.image.load('img/frame_06_delay-0.03s.png'),
    pygame.image.load('img/frame_07_delay-0.03s.png'),
    pygame.image.load('img/frame_08_delay-0.06s.png'),
    pygame.image.load('img/frame_09_delay-0.03s.png'),
    pygame.image.load('img/frame_10_delay-0.03s.png'),
    pygame.image.load('img/frame_11_delay-0.03s.png'),
    pygame.image.load('img/frame_12_delay-0.03s.png'),
    pygame.image.load('img/frame_13_delay-0.03s.png'),
    pygame.image.load('img/frame_14_delay-0.03s.png'),
    pygame.image.load('img/frame_15_delay-0.03s.png'),
    pygame.image.load('img/frame_16_delay-0.03s.png'),
    pygame.image.load('img/frame_17_delay-0.03s.png'),
    pygame.image.load('img/frame_18_delay-0.03s.png'),
    pygame.image.load('img/frame_19_delay-0.03s.png'),
    pygame.image.load('img/frame_20_delay-0.06s.png'),
    pygame.image.load('img/frame_21_delay-0.06s.png'),
    pygame.image.load('img/frame_22_delay-0.03s.png'),
    pygame.image.load('img/frame_23_delay-0.03s.png'),
    pygame.image.load('img/frame_24_delay-0.03s.png'),
    pygame.image.load('img/frame_25_delay-0.03s.png'),
    pygame.image.load('img/frame_26_delay-0.03s.png'),
    pygame.image.load('img/frame_27_delay-0.03s.png'),
    pygame.image.load('img/frame_28_delay-0.03s.png'),
    pygame.image.load('img/frame_29_delay-0.03s.png'),
    pygame.image.load('img/frame_30_delay-0.03s.png'),
    pygame.image.load('img/frame_31_delay-0.03s.png'),
    pygame.image.load('img/frame_32_delay-0.03s.png'),
    pygame.image.load('img/frame_33_delay-0.03s.png'),
    pygame.image.load('img/frame_34_delay-0.06s.png'),
    pygame.image.load('img/frame_35_delay-0.06s.png'),
    pygame.image.load('img/frame_36_delay-0.03s.png'),
    pygame.image.load('img/frame_37_delay-0.03s.png'),
    pygame.image.load('img/frame_38_delay-0.03s.png'),
    pygame.image.load('img/frame_39_delay-0.03s.png'),
    pygame.image.load('img/frame_40_delay-0.03s.png'),
    pygame.image.load('img/frame_41_delay-0.03s.png'),
    pygame.image.load('img/frame_42_delay-0.03s.png'),
    pygame.image.load('img/frame_43_delay-0.03s.png'),
    pygame.image.load('img/frame_44_delay-0.03s.png'),
    pygame.image.load('img/frame_45_delay-0.03s.png')
]
class enemy(pygame.sprite.Sprite):

    def __init__(self, x,y , hp=3, type='standard' ):
        super().__init__()
        self.stunned = False
        self.damaged_iframe = 15
        self.hp = hp
        self.type = type
        if self.type == 'spirit':
            self.image = pygame.image.load('img/frame_00_delay-0.03s.png')
            self.direction = pygame.math.Vector2(0,0)

        #hitbox
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.angle = 0
        self.original_image = self.image
        self.distance_unit = 0

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 2
    def damage(self, amount):
        if self.damaged_iframe == 0:
            self.hp -= amount
            self.damaged_iframe = 15
            hit.play()
        print(self.hp)
    def update(self, btimer, px, py, current_player):
        victim = current_player
        self.image = spirit[btimer]
        self.original_image = self.image
        self.angle = self.get_player_angle(victim.rect.centerx, victim.rect.centery)
        self.rot_center(self.angle)
        dx, dy = px - self.rect.x, py - self.rect.y

        dist = math.hypot(dx, dy)
        if dist == 0:
            pass
        else:
            dx, dy = dx / dist, dy / dist  # Normalize.
        if self.damaged_iframe > 0:
            self.damaged_iframe -= 1

        # Move along this normalized vector towards the player at current speed.
        if self.stunned == False:
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

        #self.rect.x += self.speed *self.direction.y
        #self.rect.y += self.speed *self.direction.y




    def get_player_angle(self, x, y):
        distance_x = x-self.rect.centerx
        distance_y = y-self.rect.centery

        distance = pygame.math.Vector2(distance_x, distance_y)
        try:
            self.distance_unit = pygame.math.Vector2.normalize(distance)
        except:
            pass
        angle = math.atan2(distance_y, distance_x)
        look_angle = -angle*180/math.pi
        sprite_rotation = +90
        return look_angle + sprite_rotation

    def rot_center(self, angle):
        x = self.rect.centerx
        y = self.rect.centery
        image = self.image
        rotated_image = pygame.transform.rotate(self.original_image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=(x,y)).center)

        self.image = rotated_image
        self.rect = new_rect