import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")


    clock.tick(60)

pygame.quit()