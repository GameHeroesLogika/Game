from operator import index
import pygame
import os

pygame.font.init()

class Font():
    def __init__(self,font_path,font_size,font_color,font_content,font_x,font_y,index=1,font_name=None):
        self.font_path = os.path.join(os.path.abspath(__file__+'/..'),font_path)
        self.index = index
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.font_content = font_content
        self.start_content = self.font_content
        self.font_x = font_x
        self.font_y = font_y
        self.start_y = self.font_y
        if self.font_content != None and self.index != 1:
            self.font_content = self.font_content.split(';')
    def show_text(self,win):
        
        for i in range(self.index):
            self.font = pygame.font.Font(self.font_path,round(self.font_size))
            if self.index == 1:
                if type(self.font_content) == type(list()):
                    self.font = self.font.render(self.font_content[0],True,self.font_color)
                else:
                    self.font = self.font.render(self.font_content,True,self.font_color)
            else:
                self.font = self.font.render(self.font_content[i],True,self.font_color)
            win.blit(self.font,(self.font_x,self.font_y))
            self.font_y += self.font_size
        self.font_y = self.start_y
    

