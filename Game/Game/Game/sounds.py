import pygame
pygame.init()
import os
class Sounds():
    def __init__(self, path, volume):
        self.path = path
        self.volume = volume
    def play_sound(self,index=0):
        self.sound = pygame.mixer.Sound(os.path.join(os.path.abspath(__file__ + "/.."), self.path))
        self.sound.set_volume(self.volume)
        self.sound.play(index)
    def stop_sound(self):
        pygame.mixer.Sound.stop(self.sound)

class Music(Sounds):
    def __init__(self,path,volume):
        super().__init__(path=path,volume=volume)
        
    def load_music(self):
        pygame.mixer.music.load(os.path.join(os.path.abspath(__file__ + "/.."), self.path))
        pygame.mixer.music.set_volume(self.volume) 
    def music_play(self):
        if pygame.mixer.music.get_busy():
            return True
        if not pygame.mixer.music.get_busy():
            return False
    def stop_music(self):
        pygame.mixer.music.stop()
    def unload_music(self):
       pygame.mixer.music.unload()