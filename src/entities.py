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
        self.velocity=0

    def moveLeft(self):
        self.velocity -= BALLOONSPEED

    def moveRight(self):
        self.velocity += BALLOONSPEED

    def updatePosition(self):
        self.collisionbox.x += self.velocity
        self.drawbox.update(self.drawbox.clamp(self.collisionbox))

class Obstacle(Entity):
    def __init__(self):
        self.size = (random.randint(1, 5))
        image=SPIKESPRITES[self.size-1]
        dbox=pygame.Rect((0,0),(image.get_width(),image.get_height()))
        cbox=pygame.Rect((0,0),(image.get_width(),image.get_height()))
        super().__init__(dbox , cbox, image)


    def randomPosition(self):
    
        movePosition= random.randrange(0,RESOLUTION[0]- self.drawbox.width)

        self.drawbox.x = movePosition
        self.collisionbox.x = movePosition
    
    def updatePosition(self, speed):
        self.collisionbox.y += speed
        self.drawbox.y += speed



        


        
