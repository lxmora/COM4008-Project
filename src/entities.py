from constants import *
import pygame, random

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

    def moveLeft(self):
        self.velocity -= BALLOONSPEED

    def moveRight(self):
        self.velocity += BALLOONSPEED

class Obstacle(Entity):
    def __init__(self, drawbox : pygame.Rect, collisionbox : pygame.Rect):
        self.size = (random.randint(1, 5))
        image=SPIKESPRITES[self.size]
        super().__init__(drawbox , collisionbox, image)


    def randomPosition(self):
    
        movePosition= random.randrange(0,RESOLUTION[0]- self.drawbox.width)

        self.drawbox.x = movePosition
        self.collisionbox.x = movePosition

        


        
