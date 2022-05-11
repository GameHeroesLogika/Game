import pygame
import os
from graphic_elements import*
from sounds import Sounds
from random import randint, choice
from Addition_Module import*
from Text import Font
pygame.init()
settings = dict()
with open('settings.txt','r') as file:
    for text in file:
        text = text.split('=')
        text[1] = text[1].split('\n')[0]
        if text[0] == 'SCREEN_WIDTH' or text[0] == 'SCREEN_HEIGHT':
            settings[text[0]] = int(text[1])
        elif text[0] == 'SOUNDS_VOLUME':
            settings[text[0]] = int(text[1])
        else:
            settings[text[0]] = text[1]
if settings['FULLSCREEN'] == 'True':
    settings['FULLSCREEN'] = True
else:
    settings['FULLSCREEN'] = False
if settings['SCREEN_WIDTH'] == 0 and settings['SCREEN_HEIGHT'] == 0:
    settings['SCREEN_WIDTH'] = pygame.display.Info().current_w
    settings['SCREEN_HEIGHT'] = pygame.display.Info().current_h

key_is_pressed = False
count_move = 0
#Направление движения игрока
where_move = None
# Флаг для отображения ошибки
flag_show_error = 100

# КООРДИНАТЫ ЦЕНТРАЛЬНОЙ КЛЕТКИ
CENTER_CELL_COR = [settings['SCREEN_WIDTH']//19*8,settings['SCREEN_HEIGHT']//2]
#Константа громкости звука
SOUNDS_VOLUME = 1

draw_cells = False
#Переменная, отвечающяя за сцену
scene = settings['SCENE']
#Создаем карту 1-го уровня

buttonIsPressed = False
#Влаг для перемещаения к игроку после телепорта
flag_to_move_to_hero = 0
#Переменная игры
game = True
card_pressed = None
index_card = None
artifact_pressed = None
#Игровой цикл
artifact_chest = None
time = pygame.time.Clock()
list_cor_player_xy = [0,0]

#Размер карты первого уровня
LENGTH_MAP_LVL1 = 30
#Размер клеточки в мини-карте
W_CELL_MINI_MAP = settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1
H_CELL_MINI_MAP = settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1
# Координаты для старта отрисовки клеток в мини-карте
X_FRAME_MM, Y_FRAME_MM = (settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1) + settings['SCREEN_WIDTH']//200,  settings['SCREEN_WIDTH']//19 + settings['SCREEN_WIDTH']//220 
# список клеток для мини-карты
list_cells_MM = list()
#Список из звуков подбора ресурсов
recourse_sounds = [Sounds('sounds/res1.wav',settings['SOUNDS_VOLUME']),Sounds('sounds/res2.wav',settings['SOUNDS_VOLUME']),Sounds('sounds/res3.wav',settings['SOUNDS_VOLUME'])]
flag_new_lvl = False
#Словарь отвечает за кол-во ресурсов у игрока

resources_dict = {
    'food':int(settings['FOOD']),
    'iron':int(settings['IRON']),
    'wood':int(settings['WOOD']),
    'gold':int(settings['GOLD']),
    'crystal':int(settings['CRYSTAL']),
    'stone':int(settings['STONE']),
}
past_resources_dict = resources_dict.copy()
effect_art_skills_name_dict = {
    'boots_fire.png':'iron;4;+;resourcesdict',
    'chest_hero.png':'crystal;1;+;resourcesdict',
    'helmet_hero.png':'exp;100;+;characteristicdict',
    'skill_lumberjack_learn.png':'wood;1;+;resourcesdict',
    'boots_hero.png':'lvl_skill_domesticpolitics;2;+;characteristicdict',
    'sword_fire.png':'lvl_skill_fight;2;+;characteristicdict',
    'boots_ice.png':'count_step;2;+;characteristicdict',
    'chest_fire.png':'mana;2;*;characteristicdict',
    'helmet_ice.png':'lvl_skill_diplomacy;2;+;characteristicdict',
    'skill_idol_people_learn.png':'contribution;2;*;characteristicdict',
    'skill_forest_path_learn.png':'count_step;2;+;characteristicdict'
}

characteristic_dict = {
    'exp':int(settings['EXP']),
    'lvl':int(settings['LVL_HERO']),
    'lvl_skill_diplomacy':int(settings['lvl_skill_diplomacy'.upper()]),
    'lvl_skill_domesticpolitics':int(settings['lvl_skill_domesticpolitics'.upper()]),
    'lvl_skill_fight':int(settings['lvl_skill_fight'.upper()]),
    'mana':int(settings['MANA']),
    'day':int(settings['DAY']),
    'week':int(settings['WEEK']),
    'count_step':int(settings['COUNT_STEP_HERO']),
    'contribution':int(settings['contribution'.upper()])
}

mana_fountain = int(settings['MANA_FOUNTAIN'])
exp_fountain = int(settings['EXP_FOUNTAIN'])
flag_show_new_day = 100
flag_use_fountain_exp = True
flag_use_fountain_mana = True
flag_use_tavern = True
flag_button_end = False
skill_cost = 200
max_exp_lvl = 1000
max_mana = 1000
change_mana_x = 0
step_exp_text = settings['SCREEN_WIDTH']//93
change_exp_x = 0
#Список из клеток первого уровня
list_cells_lvl1 = [list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'),
                   list('000000000000000000000000000000'), 
                   list('000000000000000000000000000000')]

#fdsffdsf
#Список-матрица объектов(персонаж, здания, ресурсы)
mat_objetcs_lvl1 =[ list('000000000000000000000000000000'),#M,p,P,E,g,i,c,w,T,t,F,f,H,h,D,d,N,n,R,r,X,x,C,W,A,B
                    list('0MpP00E0000000000P0000000Jj000'),#A,a-academia
                    list('0000gi0cw000Aa00000000S00jj00C'),#J,j-taverna
                    list('00C0C0000000aa0000000000000000'),#S-Хижина
                    list('00Ff0000000000000T00000t000000'),#B-Храм
                    list('00ff00000000000000000000000000'),#
                    list('00000Hh00000000000000000000000'),#
                    list('00000hh00000000000000000000000'),#
                    list('00000000Dd00000000000000000000'),#
                    list('00000000dd00000000000000000000'),#
                    list('000000000000Nn0000000000000000'),#
                    list('000000000000nn0000000000000000'),#
                    list('000000000000000Rr0000000000000'),#
                    list('000000000000000rr0000000000000'),#
                    list('0000000000000000000Xx000000000'),#
                    list('0000000000000000000xx000000000'),#
                    list('000000000000000000000000000000'),#
                    list('000000000000000000000000000000'),#
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('0000000000W0000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'),
                    list('000000000000000000000000000000'), 
                    list('000000000000000000000000000000')]
#Список, в которм будут храниться объекты клеток
list_objects_cells_lvl1 = []


list_cards_pl = [['бард',1,2],['клаус',5,0],['бард',3,5],['гигант',4,3],['ями',2,3],[None,3,2]]
list_card_pl_reserv = [['клаус',1,2],['бард',5,0],['подрывник',3,5],['арбалетчик',4,3],['гигант',2,3],[None,3,2]]
list_cards_menu_hero = list()

create_map(list_cells_lvl1, list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])

#Список с ячейками артефактов 

list_paths_pressed = [['images/game_interface/to_hero.png','images/game_interface/to_hero_w.png'],['images/game_interface/to_castle.png','images/game_interface/to_castle_w.png',],['images/game_interface/end_moves.png','images/game_interface/end_moves_w.png',]]
list_cor_portals = [ [[1,3],[1,17]] ]
list_matrix_artifact = []

    
create_icon_card(SCREEN_W=settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT'],
                    list_cards_pl=list_cards_pl,
                    list_card_pl_reserv=list_card_pl_reserv,
                    list_cards_menu_hero=list_cards_menu_hero)
    
