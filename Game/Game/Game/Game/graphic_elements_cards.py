import os
from pygame import*
#Класс для удобного отображения графических єлементов
class Graphic_elements_cards():
    def __init__(self,x,y,width,height,path,name = 'name'):
        self.X = x
        self.Y = y
        self.HEIGHT = height
        self.WIDTH = width
        self.NAME = name
        self.path = path
        if self.path != None:
            self.image_load()
    #Метод для подгрузки, задания размера картинке и ее отображения
    def show_image(self,screen_object):
        if self.path != None:
            self.image_load()
            screen_object.blit(self.IMG, (self.X,self.Y))
    def image_load(self):
        self.IMG = os.path.join(os.path.abspath(__file__ + "/.."), self.path)
        self.IMG = image.load(self.IMG)
        self.IMG = transform.scale(self.IMG, (self.WIDTH,int(self.HEIGHT)))

