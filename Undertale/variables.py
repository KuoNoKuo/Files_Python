import pygame
import pygame as pygame
import math
pygame.font.init()
score = 0

pygame.mixer.init()
bgmusic = pygame.mixer.music.load('sounds/Undertale  Megalovania.mp3')
pygame.mixer.music.set_volume(0.2)

hit = pygame.mixer.Sound('sounds/undertale-sound-effect-attack-hit.mp3')
hit.set_volume(0.05)

background_colour = (255,255,255)
width, height =1080, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption(' ')
screen.fill(background_colour)

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('ARCADE_R.TTF',10)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((460),(10))
    screen.blit(TextSurf, TextRect)

flag = 0
frame = 0

timer = 0
btimer = 0
fram = 30

wave = 0
enemyHealth_Multiplier = 1
damage_Multiplier = 1

character_locked = False

gay = pygame.image.load('img/mario.png')
gay = pygame.transform.scale(gay,(50,50))

bg = pygame.image.load('img/9276341dcb5d809.png')
bg = pygame.transform.scale(bg, (1080,500))

bullet = pygame.image.load('img/am.png')
bullet = pygame.transform.scale(bullet, (20,100))

one = pygame.image.load('img/1.png')
two = pygame.image.load('img/2.png')
three = pygame.image.load('img/3.png')
four = pygame.image.load('img/4.png')
five = pygame.image.load('img/5.png')
five = pygame.transform.scale(five,(300,400))

bone = pygame.image.load('img/bone.png')
bone = pygame.transform.scale(bone, (25,100))


clock = pygame.time.Clock()
running = True
x = width/2
y = height/2

f = 0

slidex = 0
slidey = 0
running = True

bullets = {

}

import random





aa = pygame.image.load('img/frame_00_delay-0.1s.png')
bb = pygame.image.load('img/frame_01_delay-0.1s.png')
cc = pygame.image.load('img/frame_02_delay-0.1s.png')
dd = pygame.image.load('img/frame_03_delay-0.1s.png')
ee = pygame.image.load('img/frame_04_delay-0.1s.png')
ff = pygame.image.load('img/frame_05_delay-0.1s.png')
gg = pygame.image.load('img/frame_06_delay-0.1s.png')
hh = pygame.image.load('img/frame_07_delay-0.1s.png')
ii = pygame.image.load('img/frame_08_delay-0.1s.png')
jj = pygame.image.load('img/frame_09_delay-0.1s.png')
kk = pygame.image.load('img/frame_10_delay-0.1s.png')
ll = pygame.image.load('img/frame_11_delay-0.1s.png')
p1_Character = [
    pygame.transform.scale(aa, (100,100)),
    pygame.transform.scale(bb, (100, 100)),
    pygame.transform.scale(cc, (100, 100)),
    pygame.transform.scale(dd, (100, 100)),
    pygame.transform.scale(ee, (100, 100)),
    pygame.transform.scale(ff, (100, 100)),
    pygame.transform.scale(gg, (100, 100)),
    pygame.transform.scale(hh, (100, 100)),
    pygame.transform.scale(ii, (100, 100)),
    pygame.transform.scale(jj, (100, 100)),
    pygame.transform.scale(kk, (100, 100)),
    pygame.transform.scale(ll, (100, 100)),

]
#CHARACTER


class player(pygame.sprite.Sprite):
    def __init__(self, x,y , hp=5, player1=True ):
        super().__init__()
        self.can_teleport = True
        self.teleport_cooldown = 0
        self.hp = hp
        self.damaged_iframe = 60
        self.vulnerable = False
        self.image_condition = player1
        if self.image_condition:
            self.image = p1_Character[0]
        else:
            self.image = p1_Character[0]

        #hitbox
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.angle = 0

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
    def damage(self, amount):
        if self.damaged_iframe == 0:
            self.hp -= amount
            self.damaged_iframe = 60
        print(self.hp)
    def update(self, frame, pos):

        self.angle = self.change_angle(pos)

        self.change_direction()
        self.rect.x += self.speed * self.direction.x
        self.rect.y += self.speed * self.direction.y
        self.image = p1_Character[frame]
        self.check_boundaries(width, height)
        if self.damaged_iframe > 0:
            self.damaged_iframe -= 1
    def change_direction(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x =-1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if keys[pygame.K_e]:
            if self.can_teleport == True:
                self.can_teleport = False
                self.teleport_cooldown = 180
                self.teleport(pygame.mouse.get_pos())



    def check_boundaries(self, width, height):

        if self.rect.left < -20:
            self.rect.left = -20
        if self.rect.top < 15:
            self.rect.top = 15
        if self.rect.bottom > 500:
            self.rect.bottom = 500
        if self.rect.right >= 1100:
            self.rect.right = 1100

    def teleport(self, pos):
        self.rect.center = pos

    def change_angle(self, pos):
        distance_x = pos[0] - self.rect.centerx
        distance_y = pos[1] - self.rect.centery

        distance = pygame.math.Vector2(distance_x, distance_y)
        try:
            self.distance_unit = pygame.math.Vector2.normalize(distance)
        except:
            pass
        angle = math.atan2(distance_y, distance_x)
        look_angle = -angle * 180 / math.pi
        sprite_rotation = +0
        return look_angle + sprite_rotation
