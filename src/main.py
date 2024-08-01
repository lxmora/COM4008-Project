from constants import *
import entities
import pygame

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BACKGROUNDCOLOR)

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()