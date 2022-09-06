import pygame.mouse
from variables import* #imports all veriables and chracter
from enemy import*
from bullet import*
#sprite setup
pygame.mixer.music.play()
mc = player(x/5, y)
mc_group = pygame.sprite.Group()
mc_group.add(mc)

mouse_click_pos = ()
player_pos = ()

bullet_group = pygame.sprite.Group()


mob = enemy(width,random.randint(0,height),type='spirit')
enemy_group = pygame.sprite.Group()
enemy_group.add(mob)
cursor = pygame.image.load('cursor.png')
cursor = pygame.transform.scale(cursor,(75,50))
pygame.mouse.set_visible(False)
cursor_img_rect = cursor.get_rect()

print(len(enemy_group))
def spawn_enemies(wave):
  for x in range(1,wave):
    a = random.randint(1,2)
    b = random.randint(1,2)
    if a == 1:
      if b == 1:
        enemy_group.add(enemy(width, random.randint(0, height), type='spirit'))
      elif b == 2:
        enemy_group.add(enemy(0, random.randint(0, height), type='spirit'))
    elif a == 2:
      if b ==1:
        enemy_group.add(enemy(random.randint(0,width), height, type='spirit'))
      elif b == 2:
        enemy_group.add(enemy(random.randint(0, width), 0, type='spirit'))
while True:
  while running:
    screen.fill((0, 0, 0))
    message_display(('Project: Undertale                                                                   Wave:{}'.format(wave)))
    cursor_img_rect.center = pygame.mouse.get_pos()  # update position
    screen.blit(cursor, cursor_img_rect)  # draw the cursor
    if len(enemy_group) == 0:
      wave += 1
      spawn_enemies(wave)
    if mc.can_teleport == False:
      if mc.teleport_cooldown == 0:
        mc.can_teleport = True
        mc.teleport_cooldown = 0
      mc.teleport_cooldown-=1
    if frame >= 5:
      if btimer >= 45:
        btimer = 0
      btimer += 1
      if f >= 11:
        f = 0
      f += 1
      frame = 0
   # pygame.draw.rect(screen, (100,255,100), pygame.Rect(0,480,400,20))
    #screen.blit(aura, (x-random.randint(65,80),y-random.randint(65,80)))
    #screen.blit(gay,(x,y))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_click_pos = pygame.mouse.get_pos()
        player_pos = mc.rect.center
        if event.button ==1:
          bullet_group.add(Bullet(mc.rect.centerx, mc.rect.centery, mc.angle, type = 'bone'))
          balls.play()

      #if event.type == pygame.MOUSEBUTTONDOWN:
              #pos = pygame.mouse.get_pos()
              #if fram == 0:
                #fram = 30

              #if character_locked == False and timer == 0:
                  #timer = 180
                  #x = pos[0]-25
                  #y = pos[1]-25
     #if flag == 1:
        #character_locked = True
        #if fc >= 70:
            #flag = 0
            #character_locked = False
            #fc = 0
        #elif fc >= 0 and fc < 10:
            #screen.blit(one, (x + 490, y - 290))
        #elif fc >= 10 and fc < 25:
            #screen.blit(two, (x+490, y-290))
        #elif fc >= 25 and fc < 40:
            #screen.blit(three, (x+450,  y-100))
        #elif fc >= 40 and fc < 60:
            #screen.blit(four, (x+400, y-290))
        #elif fc >= 60:
            #screen.blit(five, (x+400,y-400))
        #screen.blit(beam, (x + random.randint(20,30), y - random.randint(105,115)))
        #fc += 1
    #if timer != 0:
        #timer -= 1
        #if timer == 0:
            #timer = 0
    #if btimer != 0:
        #btimer -= 1
        #if timer == 0:
            #timer = 0
    #Check hitbox overlap
    #if fram != 0:
      #screen.blit(bone, (mob.rect.x,mob.rect.y))
      #fram -= 1
   # if fram == 0:
      #farm = 0

    #for single_enemy in enemy_group:
    #  if single_enemy.rect.colliderect(mc.rect):
    #    mc.damage(1)
    for single_bullet in bullet_group:
      for single_enemy in enemy_group:
        if single_bullet.rect.colliderect(single_enemy):
          single_enemy.damage(single_bullet.damage)
          if single_enemy.hp <= 0:
            single_enemy.kill()

    frame += 1
    fram += 1
    mc_group.update(f, pygame.mouse.get_pos())
    mc_group.draw(screen)
    playerx = mc.rect.x
    playery = mc.rect.y
    enemy_group.update(btimer, playerx, playery, mc)
    enemy_group.draw(screen)
    print(mc.angle)
    bullet_group.update(mouse_click_pos, player_pos)
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
