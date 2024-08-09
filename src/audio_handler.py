from constants import *
import pygame

class AudioHandler():
    
    def __init__(self):
        self.bgChannel = pygame.mixer.Channel(0)
        self.fxChannel = pygame.mixer.Channel(1)
        self.moveSound = pygame.mixer.Sound(MOVESOUND)
        self.popSound = pygame.mixer.Sound(POPSOUND)
        self.activeBgMusic = pygame.mixer.Sound(ACTIVEBGMUSIC)
        self.passiveBgMusic = pygame.mixer.Sound(PASSIVEBGMUSIC)

    def playPopSound(self):
        self.fxChannel.stop()
        self.fxChannel.play(self.popSound)

    def playMoveSound(self):
        if not self.fxChannel.get_busy():
            self.fxChannel.play(self.moveSound)

    def activeBg(self):
        self.bgChannel.stop()
        self.bgChannel.play(self.activeBgMusic, loops=-1)

    def passiveBg(self):
        self.bgChannel.stop()
        self.bgChannel.play(self.passiveBgMusic, loops=-1)