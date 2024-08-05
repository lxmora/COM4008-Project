from constants import *
import pygame
import math

class UserInterface():
    def __init__(self) -> None:
        self.score = 0
        self.font = pygame.font.SysFont(FONTSTYLE,FONTSIZE)
        self.speed = self.scoreToSpeed(self.score)

    def increaseScore(self, ammount : int = DEFAULTSCOREGAIN):
        self.score += ammount

    def resetScore(self):
        self.score = 0

    def scoreToSpeed(score):
        return math.sqrt(score)/FALLSPEEDDIVISOR

    def startGame(self):
        pygame.event.post(GAMESTART)