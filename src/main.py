from constants import *
import entities
import pygame

pygame.init()
screen = pygame.display.set_mode((480, 720))
clock = pygame.time.Clock()
running = True

ballon = entities.Ballon()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")


    pygame.draw.circle(screen,("white"), (200, 200), 75)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()