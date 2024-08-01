from constants import *
import entities
import pygame

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True

balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),BALLOONSPRITE)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Collison handling

    #Obstacle Generation

    #Movement handling

    screen.fill(BACKGROUNDCOLOR)

    #Entity Drawing
    screen.blit(balloon.image,balloon.drawbox)

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()