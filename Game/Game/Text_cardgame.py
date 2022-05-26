import pygame
import os

pygame.font.init()

class Font():
    def __init__(self,font_path,font_size,font_color,font_content,font_x,font_y):
        self.font_path = os.path.join(os.path.abspath(__file__+'/..'),font_path)
        self.font_size = font_size
        self.font_color = font_color
        self.font_content = font_content
        self.font_x = font_x
        self.font_y = font_y
    def show_text(self,win):
        self.font = pygame.font.Font(self.font_path,self.font_size)
        self.font = self.font.render(self.font_content,True,self.font_color)
        win.blit(self.font,(self.font_x,self.font_y))
    

