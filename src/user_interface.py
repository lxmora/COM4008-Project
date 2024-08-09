from constants import *
import pygame
import math
import os

class UserInterface():
    def __init__(self) -> None:
        self.score = 0
        self.font = pygame.font.SysFont(FONTSTYLE,FONTSIZE)
        self.speed = 0
        # Add a variable to store the top score
        self.topScore = self.loadTopScore()

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
        if self.score > self.topScore:
            self.topScore = self.score
         # Save the top score to file    
            self.saveTopScore() 

    def getTopScore(self):
        return self.topScore
    
    def saveTopScore(self):
        with open("top_score.txt", "w") as file:
            file.write(str(self.topScore))
            file.close()

    def loadTopScore(self):
        with open("top_score.txt", "r") as file:
           score = int(file.read())
           file.close()
           return score
        