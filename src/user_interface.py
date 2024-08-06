from constants import *
import pygame
import math

class UserInterface():
    def __init__(self) -> None:
        self.score = 0
        self.font = pygame.font.SysFont(FONTSTYLE,FONTSIZE)
        self.speed = 0
        self.top_score = 0  # Add a variable to store the top score

    def increaseScore(self, ammount : int = DEFAULTSCOREGAIN):
        self.score += ammount

    def resetScore(self):
        self.score = 0

    def updateSpeed(self):
        self.speed = math.sqrt(self.score)/FALLSPEEDDIVISOR

    def startGame(self):
        pygame.event.post(GAMESTART)

#update top score 
    def updateTopScore(self):
        if self.score > self.top_score:
            self.top_score = self.score
         # Save the top score to file    
            self.saveTopScore() 

    def getTopScore(self):
        return self.top_score
    
    def saveTopScore(self):
        with open("top_score.txt", "w") as file:
            file.write(str(self.top_score))

    def loadTopScore(self):
        if os.path.exists("top_score.txt"):
            with open("top_score.txt", "r") as file:
                return int(file.read())
        return 0