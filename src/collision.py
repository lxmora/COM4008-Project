#removed after learning pygame can handle collisions on its own

'''
from constants import *
import entities
import pygame

def checkHeight(entityA, entityB) -> bool:
    if aabb(entityA.y,entityA.y+entityA.height,entityB.y,entityB.y+entityB.height):
        return True
    else:
        return False

def checkOverlap(entityA, entityB) -> bool:
    if aabb(entityA.x,entityA.x+entityA.width,entityB.x,entityB.x+entityB.width):
        return True
    else:
        return False
    
def aabb(upperA, lowerA, upperB, lowerB):
    if (upperA < upperB < lowerA < lowerB) or (upperA < upperB < lowerB < lowerA) or (upperB < upperA < lowerA < lowerB) or (upperB < upperA < lowerB < lowerA):
        return True
    else:
        return False

def handleCollison(entityA, entityB):
    if type(entityA)==entities.Ballon and type(entityB)==entities.Wall:
        return GAMEEND
'''
