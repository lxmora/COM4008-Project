import pygame

GAMESTART = pygame.event.custom_type()
GAMEEND = pygame.event.custom_type()
FRAMERATE = 60
BACKGROUNDCOLOR = (100,100,200)
RESOLUTION = (480, 720)
BALLOONSIZE = (128,128)
BALLOONHEIGHTOFFSET=28
BALLOONHEIGHT = RESOLUTION[1]-BALLOONSIZE[1]-BALLOONHEIGHTOFFSET
BALLOONSTARTPOSITION = ((RESOLUTION[0]/2)-(BALLOONSIZE[0]/2),BALLOONHEIGHT)
BALLOONSPRITE = pygame.transform.scale(pygame.image.load("assets/balloon.png"),BALLOONSIZE)
SPIKESPRITES = [pygame.image.load("assets/spike"+str(size)+".png") for size in range(1,6)]
BALLOONSPEED = 20
OBSTACLECOOLDOWN = 360