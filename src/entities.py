from constants import *
import pygame

class Entity():
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect):
        self.drawbox=drawbox
        self.collisionbox=collisionbox
        self.image=None

class Wall(Entity):
    def __init__(self):
        super().__init__()

class Balloon(Entity):
    def __init__(self):
        super().__init__()
        self.velocity=None

    def moveLeft():
        pass

    def moveRight():
        pass