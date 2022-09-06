import pygame
import math
import numpy
balls = pygame.mixer.Sound('sounds/voice_sans.mp3')
balls.set_volume(0.1)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player_look_angle, type='bone'):
        print(player_look_angle)
        super().__init__()
        self.type = type
        self.damage = 1
        if self.type == 'bone':
            self.image = pygame.transform.scale(pygame.image.load('img/bone.png'), (25,100))
            self.image = pygame.transform.rotate(self.image, (player_look_angle+90))

        self.angle = player_look_angle
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.speed = 50
        self.direction = pygame.math.Vector2(0,0)
    def update(self, pos, player):

        x = math.cos(math.radians(self.angle))
        y = -math.sin(math.radians(self.angle))
        print(f'A:{self.angle}, X: {x}, Y:{y}')
        self.direction = pygame.math.Vector2(x, y)
        self.rect.x += self.speed*self.direction.x
        self.rect.y += self.speed*self.direction.y
        pass