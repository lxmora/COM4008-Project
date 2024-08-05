from constants import *
import entities
import pygame
import math
from user_interface import UserInterface

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True
ui = UserInterface()

obstacleTimer = 0

boundarybox = pygame.Rect((0,0),RESOLUTION)
balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONCBOXSTARTPOSITION,BALLOONCBOXSIZE),BALLOONSPRITE)
obstacles = []



def drawEntities():
    screen.blit(balloon.image,balloon.drawbox)
    for obstacle in obstacles:
        screen.blit(obstacle.image,obstacle.drawbox)
    #screen.fill((0,255,0),balloon.collisionbox,special_flags=1) #collision box visualization
    screen.blit(ui.font.render("Score:"+str(ui.score),True,(0,0,0)),(10,RESOLUTION[1]-(40)))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAMEEND:
            running = False

    #Position Updates

    balloon.updatePosition()
    for obstacle in obstacles:
        obstacle.updatePosition(ui.speed)

    #Collison handling

    for obstacle in obstacles:
        if obstacle.collisionbox.colliderect(balloon.collisionbox):
            pygame.event.post(GAMEENDEVENT)
    if not boundarybox.contains(balloon.collisionbox):
        balloon.velocity *= -1


    #Obstacle Generation & Deletion

    obstacleTimer += 1 

    if obstacleTimer == OBSTACLECOOLDOWN: 
        obstacles.append(entities.Obstacle())
        obstacleTimer = 0 
        obstacles[-1].randomPosition()
    
    ui.score += 1
    

    #Movement handling

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            balloon.moveLeft()

        if event.key == pygame.K_RIGHT:
            balloon.moveRight()

    screen.fill(BACKGROUNDCOLOR)

    drawEntities()

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()