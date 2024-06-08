from random import *
from variables import *
import pygame


class Meteor:
    radius = None
    mass = None
    x = None
    y = None
    color = None
    def __init__(self) -> None:
        self.radius = randint(3,10)
        self.mass = randint(10,100)
        self.x = randint(1,1000)
        self.y = randint(1,1000)
        self.color = choice(cometColor)


    def move(self, coord, mass):
        
        dx = coord[0]-self.x
        dy = coord[1]-self.y
        vx,vy = dx/(mass*self.mass), dy/(mass*self.mass)
        self.x += vx
        self.y += vy






        
    


