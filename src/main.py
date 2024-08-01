from constants import *
import entities
import pygame
import math

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True

obstacleTimer = 0
score = 0

boundarybox = pygame.Rect((0,0),RESOLUTION)
balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),BALLOONSPRITE)
obstacles = []

def drawEntities():
    screen.blit(balloon.image,balloon.drawbox)
    for obstacle in obstacles:
        screen.blit(obstacle.image,obstacle.drawbox)

    pygame.display.flip()

def scoreToSpeed(self, score):
    return math.sqrt(score)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Position Updates

    balloon.updatePosition()
    for obstacle in obstacle:
        obstacle.updatePosition(scoreToSpeed(score))

    #Collison handling

    for obstacle in obstacles:
        if obstacle.collisionbox.colliderect(balloon.collisionbox):
            running = False
    if not boundarybox.contains(balloon.collisionbox):
        balloon.velocity *= -1


    #Obstacle Generation & Deletion

    obstacleTimer += 1 

    if obstacleTimer == OBSTACLECOOLDOWN: 
        obstacles.append(entities.Obstacle())
        obstacleTimer = 0 
    

    

    #Movement handling

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass

        if event.key == pygame.K_RIGHT:
            pass

    screen.fill(BACKGROUNDCOLOR)

    drawEntities()

    clock.tick(FRAMERATE)

pygame.quit()