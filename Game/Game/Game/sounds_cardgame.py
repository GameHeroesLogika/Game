import pygame

import os
class Sounds():
    def __init__(self, path, volume):
        
        self.path = path
        self.volume = volume
    def play_sound(self):
        self.sound = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + "/.."), self.path))
        self.sound.set_volume(self.volume)
        self.sound.play()