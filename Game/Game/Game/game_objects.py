import pygame
from constants import*
from cards import Cards
from graphic_elements_cards import Graphic_elements_cards
from sounds import Sounds
from Text import Font
#Создаем окно, с параметром БЕЗ РАМКИ
win = pygame.display.set_mode((SCREEN_W, SCREEN_H),)#pygame.FULLSCREEN
#Создаем объект фона
bg = Graphic_elements_cards(0,0,SCREEN_W,SCREEN_H,'images/bg.bmp')
#Создаем объекты карт
card_pl_1 = Cards(SCREEN_W//12*3.2,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_1')
card_pl_2 = Cards(SCREEN_W//12*4.6,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_2')
card_pl_3 = Cards(SCREEN_W//12*6,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_3')
card_pl_4 = Cards(SCREEN_W//12*7.4,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_4')
card_pl_5 = Cards(SCREEN_W//12*8.9,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_5')
card_pl_6 = Cards(SCREEN_W//12*10.4,SCREEN_H//1.5, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='pl_6')
card_en_1 = Cards(SCREEN_W//12*3.2,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_1')
card_en_2 = Cards(SCREEN_W//12*4.6,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_2')
card_en_3 = Cards(SCREEN_W//12*6,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_3')
card_en_4 = Cards(SCREEN_W//12*7.4,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_4')
card_en_5 = Cards(SCREEN_W//12*8.9,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_5')
card_en_6 = Cards(SCREEN_W//12*10.4,SCREEN_H//20, SCREEN_W//12, SCREEN_W//7,path = None,hp = None,damage = None,desc_path = None,name='en_6')
#Списки объектов карт
list_objects_cards_pl = [card_pl_1,card_pl_2,card_pl_3,card_pl_4,card_pl_5,card_pl_6]
list_objects_cards_en = [card_en_1,card_en_2,card_en_3,card_en_4,card_en_5,card_en_6]
# Картинка взрыва для способности подрывника
img_boom = Graphic_elements_cards(None,None,SCREEN_W//12, SCREEN_H//12,'images/boom.png')
#Картинка иссцеляющего облака
heal_cloud = Graphic_elements_cards(0,0,SCREEN_W//12, SCREEN_H//12,'images/hill_cloud.png')
#Картинка "Оглушение" 
stun_img = Graphic_elements_cards(0,0,SCREEN_W//9, SCREEN_H//9,'images/stun.png')
#Картинка меча
dmg_img = Graphic_elements_cards(0,0,SCREEN_W//12, SCREEN_H//12,'images/dmg_symb2.png')
#Иконка способностей
flash_light_icon = Graphic_elements_cards(SCREEN_W//6, SCREEN_H//1.3,SCREEN_W//15,SCREEN_W//15,'images/skills_icons/flash_icon.png', name='flash_light')
heal_skill_Icon = Graphic_elements_cards(SCREEN_W//6, SCREEN_H//1.3,SCREEN_W//15,SCREEN_W//15,'images/skills_icons/heal_icon.png', name='heal')
damage_skill_Icon = Graphic_elements_cards(SCREEN_W//6, SCREEN_H//1.3,SCREEN_W//15,SCREEN_W//15,'images/skills_icons/dmg_icon.png', name='damage')
#Описание скилла героя 
desc_skill = Graphic_elements_cards(SCREEN_W//2.5,SCREEN_H//4,SCREEN_W//4,SCREEN_H//2,None)

#Картинка молнии
flash_light_image = Graphic_elements_cards(0,0,SCREEN_W//12,SCREEN_W//12,None)
# Рамка для ошибки
frame_error = Graphic_elements_cards(SCREEN_W//2 - SCREEN_W//6, SCREEN_H//2 - SCREEN_H//8, SCREEN_W//3, SCREEN_H//4, 'images/error_sheet.png')
# Объект текста ошибки
error_text_obj = Font('images/Font/pixel_font.ttf',SCREEN_W//50,'red',None,frame_error.X+SCREEN_W//40,frame_error.Y + SCREEN_H//10)

# Подгружаем звуки для игры
sound_hit = Sounds('sounds/sword.wav',1)
sound_heal = Sounds('sounds/healsound.wav',1)
sound_flashlight = Sounds('sounds/flashlight.wav',1)
sound_explosion = Sounds('sounds/explosion.wav',1)
sound_paper = Sounds('sounds/book_opened.wav',1)
# Объект карты для отображения потерь в сцене результата боя
card_for_result_screen =Graphic_elements_cards(None,None,SCREEN_W//12, SCREEN_W//7,None)

#Иконки ресурсов для сцены результата боя
gold_icon = Graphic_elements_cards(SCREEN_W//12*3.2,SCREEN_H//1.15,SCREEN_W//15,SCREEN_W//20,'images/gold_bullion.png')
exp_icon = Graphic_elements_cards(SCREEN_W//12*6,SCREEN_H//1.15,SCREEN_W//20,SCREEN_W//20,'images/exp.png')
# Текст для кол-ва ресурсов для сцены результата боя
trophy_recourse_text = Font('images/Font/pixel_font.ttf',SCREEN_W//20,'white',None,None,None)
# Кнопка завершения боя
button_end_fight = Graphic_elements_cards(SCREEN_W//12*10,SCREEN_H//1.2, SCREEN_W//8, SCREEN_W//15,'images/buttons/end_fight_y.png')
#Экраны для победы и поражения
bg_win = Graphic_elements_cards(0,0, SCREEN_W, SCREEN_H,'images/bg_win.png')
bg_lose = Graphic_elements_cards(0,0, SCREEN_W, SCREEN_H,'images/bg_lose.png')