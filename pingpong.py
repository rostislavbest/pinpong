import pygame
pygame.init()
from random import choice
class Player():
    def __init__(self,x,y,w,h,img):
        self.x = x
        self.y = y
        self.w = w
        self.h =h
        self.img = img
        self.img_new = pygame.transform.scale(pygame.image.load(self.img),(self.w,self.h))
        self.imgrect = self.img_new.get_rect(center = (self.x,self.y))

player = Player(59,190,30,175,'platforma.png')
enemy = Player(650,190,30,175,'platforma.png')
ball = Player(330,219,50,50,'ball.png')

W,H  = 700,450
pygame.display.set_caption('Ping-Pong')
scr  =pygame.display.set_mode((W,H))
fon = pygame.transform.scale(pygame.image.load('eeeeeeeee.jpg'),(W,H))
run = True
fps = pygame.time.Clock()
dx = 1
dy =1
emove =10
f = 100
rand_list = [1,-1]
def ball_move():
    global dx,dy
    ball.imgrect.x +=dx
    ball.imgrect.y +=dy
    if ball.imgrect.bottom>=H:
        dy = -1
    if ball.imgrect.right>=W:
        ball.imgrect.x, ball.imgrect.y = 330, 219
        dx = -1

    if ball.imgrect.top<=0:
        dy = 1
    if ball.imgrect.left<=0:
        ball.imgrect.x, ball.imgrect.y = 330,219
        dx =1
    if player.imgrect.colliderect(ball.imgrect):
        dx =1
def enemy_move():
    global dx
    global emove
    global f
    if f == 100:
        emove = choice(rand_list)
        f = 0

    enemy.imgrect.y -=emove
    if enemy.imgrect.top <=0:
        emove = -1
    elif enemy.imgrect.bottom>=H:
        emove = 1
    if enemy.imgrect.colliderect(ball.imgrect):
        dx -=1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player.imgrect.top >0:
        player.imgrect.y -=1
    if key[pygame.K_DOWN] and player.imgrect.bottom <H:
        player.imgrect.y += 1
    ball_move()
    enemy_move()
    scr.blit(fon,(0,0))
    scr.blit(player.img_new,(player.imgrect.x,player.imgrect.y))

    scr.blit(ball.img_new, (ball.imgrect.x, ball.imgrect.y))
    scr.blit(enemy.img_new, (enemy.imgrect.x, enemy.imgrect.y))
    fps.tick(130)
    f+=1
    pygame.display.update()
