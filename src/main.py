from constants import *
import entities
import pygame
import audio_handler
from user_interface import UserInterface

pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()
running = True
ui = UserInterface()
audio = audio_handler.AudioHandler()

obstacleTimer = 0

boundarybox = pygame.Rect((0,0),RESOLUTION)
balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONCBOXSTARTPOSITION,BALLOONCBOXSIZE),BALLOONSPRITE)
obstacles = []

def drawEntities():
    screen.blit(balloon.image,balloon.drawbox)
    for obstacle in obstacles:
        screen.blit(obstacle.image,obstacle.drawbox)
   # screen.fill((0,255,0),balloon.collisionbox,special_flags=1) #collision box visualization
    screen.blit(ui.font.render("Score:"+str(ui.score),True,(0,0,0)),(10,RESOLUTION[1]-(40)))
     # Display top score on game screen
    screen.blit(ui.font.render("Top Score: " + str(ui.getTopScore()), True, (0, 0, 0)), (10, RESOLUTION[1] - 60)) 

# Function to display text on the screen
def displayText(text, y_pos):
    rendered_text = ui.font.render(text, True, FONTCOLOR)
    screen.blit(rendered_text, (RESOLUTION[0]//2 - rendered_text.get_width()//2, y_pos))

# Start screen function
def startScreen():
    screen.fill(BACKGROUNDCOLOR)
    displayText("Press any key to start", RESOLUTION[1]//2)
      # Display top score on start screen
    displayText("Top Score: " + str(ui.getTopScore()), RESOLUTION[1] // 2 + 40)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                audio.activeBg()
                waiting = False

# Game over screen function
def gameOverScreen():
    screen.fill(BACKGROUNDCOLOR)
    # Update the top score if the current score is higher
    ui.updateTopScore()  
    displayText("Game Over! Press any key to restart", RESOLUTION[1] // 2)
    # Display current score
    displayText("Score: " + str(ui.score), RESOLUTION[1] // 2 + 40) 
    # Display top score on game over screen 
    displayText("Top Score: " + str(ui.getTopScore()), RESOLUTION[1] // 2 + 80)  
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                audio.activeBg()
                resetGame()

def resetGame():
    global obstacles, obstacleTimer, ui, balloon
    obstacles = []
    obstacleTimer = 0
    ui.resetScore()
    balloon = entities.Balloon(pygame.Rect(BALLOONSTARTPOSITION,BALLOONSIZE),pygame.Rect(BALLOONCBOXSTARTPOSITION,BALLOONCBOXSIZE),BALLOONSPRITE)

# Display the start screen
audio.passiveBg()
startScreen()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == GAMEEND:
            audio.playPopSound()
            audio.passiveBg()
            gameOverScreen()



    # Smooth movement handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        audio.playMoveSound()
        balloon.moveLeft()
    
    if keys[pygame.K_RIGHT]:
        audio.playMoveSound()
        balloon.moveRight()

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
    
    ui.updateSpeed()

    screen.fill(BACKGROUNDCOLOR)

    drawEntities()

    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()