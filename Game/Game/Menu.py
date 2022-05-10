from const import *
from Addition_Module import*
pygame.init()

class Menu(Graphic_elements):
    def __init__(self,x,y,width,height,path,image_button_b,image_button_y,x_divider,y_divider):
        self.IMAGE_BUTTON_B = image_button_b
        self.IMAGE_BUTTON_Y = image_button_y
        self.X_DIVIDER = x_divider
        self.Y_DIVIDER = y_divider
        super().__init__(x,y,width,height,path)
        self = Graphic_elements(x,y,width,height,path)
        self.IMAGE_BUTTON_B = image_button_b
        self.IMAGE_BUTTON_Y = image_button_y
        self.X_DIVIDER = x_divider
        self.Y_DIVIDER = y_divider
        self.path = path
    def resize_button_menu(self, mouse_cor,SCREEN_W,SCREEN_H):
        if check_mouse_cor(self,mouse_cor):
            self.path = self.IMAGE_BUTTON_Y
            self.X = SCREEN_W//self.X_DIVIDER -1
            self.Y = SCREEN_H//self.Y_DIVIDER -1
            self.WIDTH = SCREEN_W//7
            self.HEIGHT = SCREEN_H//8
            self.image_load()
        else:
            self.path = self.IMAGE_BUTTON_B
            self.X = SCREEN_W//self.X_DIVIDER
            self.Y = SCREEN_H//self.Y_DIVIDER
            self.WIDTH = SCREEN_W//8
            self.HEIGHT = SCREEN_H//9
            self.image_load()


    

