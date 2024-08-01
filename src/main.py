from constants import *
import entities
import pygame

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True

boundarybox = pygame.Rect((0,0),RESOLUTION)
balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),BALLOONSPRITE)
obstacles = []

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Position Updates



    #Collison handling

    for obstacle in obstacles:
        if obstacle.collisionbox.colliderect(balloon.collisionbox):
            running = False
    if not boundarybox.contains(balloon.collisionbox):
        balloon.velocity *= -1


    #Obstacle Generation

    

    #Movement handling

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass

        if event.key == pygame.K_RIGHT:
            pass

    screen.fill(BACKGROUNDCOLOR)

    #Entity Drawing

    screen.blit(balloon.image,balloon.drawbox)
    for obstacle in obstacles:
        screen.blit(obstacle.image,obstacle.drawbox)

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()