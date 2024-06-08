import pygame
import os

from Meteor import Meteor
from BlackHole import BlackHole
from variables import *




def change(i,space, scale):
    if i>=len(space):
        return
    pygame.draw.circle(screen, space[i].color, (space[i].x, space[i].y), space[i].radius)
    pygame.draw.circle(screen, WHITE, (space[i].x, space[i].y), space[i].radius//3)
    space[i].move(center,bh.mass) 
    if center[1]-scale<space[i].y<center[1]+scale and center[0]-scale<space[i].x<center[0]+scale:
        space.pop(i)
        return change(i,space, scale)    
    return change(i+1,space, scale)

def blitBH(screen, image, angle, topleft ):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    screen.blit(rotated_image, new_rect)
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole")
clock = pygame.time.Clock()


running = True
scale = 50
bg = pygame.image.load('Sprites/cosmos.png')
im = pygame.image.load('Sprites/bh.png')
im = pygame.transform.scale(im, (scale*2,scale*2))
bh = BlackHole(im)
space = []
angle = 0
while running:
    
    clock.tick(FPS)
    screen.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            met = Meteor()
            pygame.draw.circle(screen, BLACK, (met.x, met.y), met.radius)
            space.append(met)
    change(0,space, scale-20)

    blitBH(screen,bh.sprite, angle, (center[0]-scale,center[1]-scale))
    angle += 0.3
    angle %=360
    pygame.display.flip()
    
pygame.quit()