from Text_cardgame import Font
from graphic_elements_cards import Graphic_elements_cards
from sounds import Sounds
from const import*
class Cards(Graphic_elements_cards):
    def __init__(self, x, y, width, height, path, hp, damage, desc_path, name='name',price = None,SCREEN_W =settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT']):
        super().__init__(x, y, width, height, path, name)
        #Значение урона и хп карты
        self.HP = hp
        self.DAMAGE = damage
        #Старотовые координаты карты
        self.START_X = x
        self.START_Y = y
        #Иконка урона и хр карты
        self.img_heart = Graphic_elements_cards(self.X,self.Y+self.HEIGHT-self.HEIGHT//6,self.HEIGHT//5,self.HEIGHT//5,'images/hp_symb.png')
        self.img_dmg = Graphic_elements_cards(self.X+ self.WIDTH -self.WIDTH//34,self.Y+self.HEIGHT-self.HEIGHT//6,self.HEIGHT//3.5,self.HEIGHT//3.5,'images/dmg_symb.png')
        #Отображаемый текст урона и хп карты
        self.hp_text = Font('images/Font/pixel_font.ttf',int(self.HEIGHT//5),'lime','0',self.X + self.img_heart.WIDTH//4,self.Y+self.HEIGHT-self.HEIGHT//6)
        self.dmg_text = Font('images/Font/pixel_font.ttf',int(self.HEIGHT//5),'red','0',self.X + self.WIDTH -self.WIDTH//5,self.Y+self.HEIGHT-self.HEIGHT//6)
        #Путь к картеочке-описанию
        self.DESC_PATH = desc_path 
        #Объект карточки-описания 
        self.desc = Graphic_elements_cards(SCREEN_W//2 - int(SCREEN_W*0.7)//2, SCREEN_H//2 - int(SCREEN_H*0.7)//2, int(SCREEN_W*0.7), int(SCREEN_H*0.7), self.DESC_PATH)
        # Может ли ходить карта
        self.can_move = True
        # Уникальный звук для карты
        self.sound_card = Sounds(None, settings['SOUNDS_VOLUME'])
        # цена карты
        self.price = price
    #Метод, отображающий на карте ее урон и хп
    def show_parametres(self,win):
        self.img_heart.X,self.img_heart.Y = self.X ,self.Y+self.HEIGHT-self.HEIGHT//6
        self.img_dmg.X, self.img_dmg.Y = self.X+ self.WIDTH -self.WIDTH//2.5,self.Y+self.HEIGHT-self.HEIGHT//5
        self.hp_text.font_x, self.hp_text.font_y = self.X + self.img_heart.WIDTH//4,self.Y+self.HEIGHT-self.HEIGHT//6
        self.dmg_text.font_x,self.dmg_text.font_y = self.X + self.WIDTH -self.WIDTH//5,self.Y+self.HEIGHT-self.HEIGHT//6
        self.img_heart.show_image(win)
        self.img_dmg.show_image(win)
        self.hp_text.font_content = str(self.HP)
        self.hp_text.show_text(win)
        self.dmg_text.font_content = str(self.DAMAGE)
        self.dmg_text.show_text(win)
    #Метод для отображения карточки-описания
    def show_desc(self,win):
        self.desc.path = self.DESC_PATH
        self.desc.show_image(win)

    def __str__(self):
        return self.NAME