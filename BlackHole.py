import pygame



class BlackHole:
    mass = None
    sprite = None

    def __init__(self, im) -> None:
        self.mass = 1
        self.sprite = im
