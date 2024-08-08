from constants import *
import pygame

class AudioHandler():
    
    def __init__(self):
        self.bgChannel = pygame.mixer.Channel(0)
        self.fxChannel = pygame.mixer.Channel(1)
        self.moveSound = pygame.mixer.Sound("")
        self.popSound = pygame.mixer.Sound("")
        self.bgMusic = pygame.mixer.Sound("")

    def playPopSound(self):
        self.fxChannel.stop()
        self.fxChannel.play(self.popSound)

    def playMoveSound(self):
        self.fxChannel.stop()
        self.fxChannel.play(self.moveSound)