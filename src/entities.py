from constants import *
import pygame

class Entity():
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect, image):
        self.drawbox=drawbox
        self.collisionbox=collisionbox
        self.image=image

class Wall(Entity):
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect, image):
        super().__init__(drawbox , collisionbox, image)

class Balloon(Entity):
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect, image):
        super().__init__(drawbox , collisionbox, image)
        self.velocity=None

    def moveLeft():
        pass

    def moveRight():
        pass

class Obstacle(Entity):
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect, image):
        super().__init__(drawbox , collisionbox, image)
