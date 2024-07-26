from constants import *
import pygame

class Entity():
    def __init__(self):
        self.x=None
        self.y=None
        self.height=None
        self.width=None 
        self.image=None

class Wall(Entity):
    def __init__(self):
        super().__init__()

class Ballon(Entity):
    def __init__(self):
        super().__init__()
        self.velocity=None

    def moveLeft():
        pass

    def moveRight():
        pass