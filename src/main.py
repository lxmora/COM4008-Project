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



# Smooth movement for the balloon
balloon_velocity = pygame.Vector2(0, 0)
balloon_speed = 5




def drawEntities():
    screen.blit(balloon.image,balloon.drawbox)
    for obstacle in obstacles:
        screen.blit(obstacle.image,obstacle.drawbox)
    #screen.fill((0,255,0),balloon.collisionbox,special_flags=1) #collision box visualization
    screen.blit(ui.font.render("Score:"+str(ui.score),True,(0,0,0)),(10,RESOLUTION[1]-(40)))





# Function to display text on the screen
def displayText(text, y_pos):
    rendered_text = ui.font.render(text, True, FONTCOLOR)
    screen.blit(rendered_text, (RESOLUTION[0]//2 - rendered_text.get_width()//2, y_pos))

# Start screen function
def startScreen():
    screen.fill(BACKGROUNDCOLOR)
    displayText("Press any key to start", RESOLUTION[1]//2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Game over screen function
def gameOverScreen():
    screen.fill(BACKGROUNDCOLOR)
    displayText("Game Over! Press any key to restart", RESOLUTION[1]//2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                resetGame()

def resetGame():
    global obstacles, obstacleTimer, ui, balloon
    obstacles = []
    obstacleTimer = 0
    ui.resetScore()
    balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONCBOXSTARTPOSITION,BALLOONCBOXSIZE),BALLOONSPRITE)

# Display the start screen
startScreen()






while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAMEEND:
            running = False



    # Smooth movement handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        balloon_velocity.x = -balloon_speed
    elif keys[pygame.K_RIGHT]:
        balloon_velocity.x = balloon_speed
    else:
        balloon_velocity.x = 0






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
    


    screen.fill(BACKGROUNDCOLOR)

    drawEntities()

    pygame.display.flip()

    clock.tick(FRAMERATE)

    # Display the game over screen
gameOverScreen()

pygame.quit()