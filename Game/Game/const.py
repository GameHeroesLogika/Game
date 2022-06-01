from dataclasses import replace
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
flag_show_tavern = 30
# КООРДИНАТЫ ЦЕНТРАЛЬНОЙ КЛЕТКИ
CENTER_CELL_COR = [settings['SCREEN_WIDTH']//19*8,settings['SCREEN_HEIGHT']//2]
#Константа громкости звука
SOUNDS_VOLUME = 1


list_losed_card_enemy = []
list_losed_card_pl = []
# Опыт и золото, которое получил игрок при победе
trophy_exp = 0
trophy_gold = 0

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
list_cor_castle_xy = [0,0]
#Размер карты первого уровня
LENGTH_MAP_LVL1 = 31
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
    'iron_bullion':int(settings['IRON']),
    'wood':int(settings['WOOD']),
    'gold_bullion':int(settings['GOLD']),
    'crystal':int(settings['CRYSTAL']),
    'stone':int(settings['STONE']),
}
past_resources_dict = resources_dict.copy()
effect_art_skills_name_dict = {
    'boots_fire.png':'iron_bullion;4;+;resourcesdict',
    'chest_hero.png':'crystal;1;+;resourcesdict',
    'helmet_hero.png':'exp;100;+;characteristicdict',
    'skill_lumberjack_learn.png':'wood;1;+;resourcesdict',
}
# effect_skills_name_dict = {
#     'boots_hero.png':'lvl_skill_domesticpolitics;2;+;characteristicdict',
#     'sword_fire.png':'lvl_skill_fight;2;+;characteristicdict',
#     'boots_ice.png':'count_step;2;+;characteristicdict',
#     'chest_fire.png':'mana;2;*;characteristicdict',
#     'helmet_ice.png':'lvl_skill_diplomacy;2;+;characteristicdict',
#     'skill_idol_people_learn.png':'contribution;2;*;characteristicdict',
#     'skill_forest_path_learn.png':'count_step;2;+;characteristicdict'
# }

characteristic_dict = {
    'exp':int(settings['EXP']),
    'lvl':int(settings['LVL_HERO']),
    'lvl_skill_diplomacy':int(settings['lvl_skill_diplomacy'.upper()]),
    'lvl_skill_domesticpolitics':int(settings['lvl_skill_domesticpolitics'.upper()]),
    'lvl_skill_fight':int(settings['lvl_skill_fight'.upper()]),
    'mana':int(settings['MANA']),
    'day':int(settings['DAY']),
    'week':int(settings['WEEK']),
    'week':int(settings['WEEK']),
    'count_step':int(settings['COUNT_STEP_HERO']),
    'contribution':int(settings['contribution'.upper()]),
    'change_mana':1,
    'change_exp':1,
}
dict_artifact_on = {
    'helmet':None,
    'sword':None,
    'chest':None,
    'boots':None,
    'shield':None,
}
list_learn_skills = list()
dict_artifact_on_past = dict_artifact_on.copy()
list_order_skills = ['skill_earth_blessing','skill_forest_path','skill_idol_people','skill_leader','skill_lumberjack']
mana_fountain = int(settings['MANA_FOUNTAIN'])
exp_fountain = int(settings['EXP_FOUNTAIN'])
flag_buy_card = True
flag_forge = True
flag_show_new_day = 100
flag_use_fountain_exp = True
past_lvl_skill_fight = 0
flag_use_fountain_mana = True
flag_buy_previous_build = 30
flag_show_shack = 30
flag_show_fountain_mana = 30
flag_show_fountain_exp = 30
flag_build_alredy_bought = 30
flag_not_enough_resource = 30
flag_use_tavern = True
flag_button_end = False
flag_market_selected = False
flag_new_lvl_skill_fight = False
flag_market_aritfact_no_slots = 30
flag_not_enough_gold = 30
flag_show_error_not_inventory = 50
flag_show_error_locked = 30
flag_show_error_blocked_camp = 50
changed_hp = 0
changed_dmg = 0
flag_show_error_bought_card = 30
index_water = 0
count_animation= 0
flag_church = True
skill_cost = 200
max_exp_lvl = 1000
max_mana = 1000
mana_shack = 200
change_mana_x = 0
step_exp_text = settings['SCREEN_WIDTH']//93
change_exp_x = 0
flag_show_error_next_week = 30
flag_buy_skill = True
flag_use_royal_academy = True
number_opened_card = 2
#Список из клеток первого уровня
list_cells_lvl1 = [list('0000000000000000000000000000000'),
                   list('00000000000000000tttttttt000000'),
                   list('00000000000000000t000000t000000'),
                   list('0t000000000000000t000000t000000'),
                   list('0t0000000000000ttt0000000000tt0'),
                   list('0ttttt000000000t00000000000tt00'),
                   list('0t000tttttt0000t000000000ttt000'),
                   list('0t00000000t0000t00000000tt00000'),
                   list('0tt0000000t0000t00000000t000000'),
                   list('0000000000tttttt0000000tt000000'),
                   list('0000000000t0000ttt00000t0000000'),
                   list('0000000000t000000ttt000t0000000'),
                   list('000000ttttt00000000ttt0t0000000'),
                   list('00000tt00000000000000t0t0000000'),
                   list('t0000t000000000000000tttt000000'),
                   list('t0000t000000000000000000t000000'),
                   list('tttttt000000000000000000t000000'),
                   list('000t000000000000000000tttttttt0'),
                   list('000t00000000000000000tt000000t0'),
                   list('000t00000000000000000t0000000tt'),
                   list('000ttttttttttttttttttt00000000t'),
                   list('tttt000000000000000t00000000000'),
                   list('t000000000000000000t00000000000'),
                   list('t0000000000000000ttttt000000000'),
                   list('t000000000000000tt000t000000000'),
                   list('tt00000000000000t00000000000000'),
                   list('0ttt00000000000tt00000000000000'),
                   list('000t00000000000t000000000000000'),
                   list('000000000000000t000000000000000'), 
                   list('000000000000000t000000000000000'), 
                   list('00000000000000tt000000000000000')]

#Список-матрица объектов(персонаж, здания, ресурсы)
mat_objetcs_lvl1 =[ list('KkkP00000000БCл0000000000Nnгггг'),#M,p,P,E,g,i,c,w,T,t,F,f,H,h,D,d,N,n,R,r,X,x,C,W,A,B,e,m,s
                    list('kkk0000b0000ллл0000000000nn11гг'),#A,a-academia
                    list('kkk000000000лллHh0000P000000вг1'),#J,j-taverna
                    list('0p0000000000Mллhh0000000000вв11'),#S-Хижина
                    list('000000000000лл0000000000W0вв00S'),#B-Храм
                    list('000000W00000лл0000000000ввв0000'),#\ / | л
                    list('00000000000лл000000E000вв000000'),#
                    list('00000000000лл0000000000в0000000'),#
                    list('000Jj000лл00000000000ввв0000000'),#
                    list('000jj000лл00000000000вC00000000'),#
                    list('Гл0ллллллл00000000000вв0000000C'),#
                    list('Cллллллллл000000000000в00000000'),#
                    list('000000000000000000000Ав0000E000'),#
                    list('S0000000000000000000в0в00000000'),#
                    list('000000Dd000000ввв00вв0000000000'),#
                    list('000000dd000000в0вввв00Oo0000000'),#
                    list('00000000000000в00в0000oo0000000'),#
                    list('0000000000000ввXxв000P000000000'),#
                    list('000000000000вв0xxв0000000000000'),
                    list('00000000E000в0000вв000000000000'),
                    list('00P00000000Г00000Г0000000000000'),
                    list('000000000000вRr00вв000000000ллА'),
                    list('0Ff000000000вrr0ввC00000000ллл0'),
                    list('0ff00000000вввввв000000лллл0000'),
                    list('00000000000в0000000000Wлллл0000'),
                    list('00000000вввв0000000000лл00000лC'),
                    list('Б000000вв0000000000000лл000лллл'),
                    list('Cвв000вв00000000000000ллГллл000'),
                    list('ввввW0в000000Aa0000000лл0лл0Ззз'), 
                    list('ввввввв000000aa000000лл00лл0ззз'), 
                    list('вввC0000000000000000Mлл00Г00ззз')]
list_forest_element = ['|','\\','/','л']
for el in range(len(mat_objetcs_lvl1)):
    for element in range(len(mat_objetcs_lvl1[el])):
        if mat_objetcs_lvl1[el][element] == 'л':
            mat_objetcs_lvl1[el][element] = choice(list_forest_element)
list_flower_element = ['1','2','3','4','0','0','0']
for el in range(len(list_cells_lvl1)):
    for element in range(len(list_cells_lvl1[el])):
        if list_cells_lvl1[el][element] == '0':
            list_cells_lvl1[el][element] = choice(list_flower_element)
#Список, в которм будут храниться объекты клеток
list_objects_cells_lvl1 = []

dict_card_characteristics = {
                            'бард':[1,2,'earth'],
                            'клаус':[1,0,'hell'],
                            'гигант':[1,3,'mountain'],
                            'ями':[9,1,'hell'],
                            'подрывник':[8,5,'earth'],
                            'арбалетчик':[9,3,'earth'],
                            'кентавр':[10,3,'hell'],
                            'орк':[10,2,'mountain'],
                            'дворф':[10,2,'mountain'],
                            'рогги':[6,3,'hell'],
                            'суртур':[7,3,'hell'],
                            'лудорн':[8,3,'mountain'],
                            'друид':[7,4,'earth']
}
dict_card_characteristics_enemy = {
                            'бард':[1,2,'earth'],
                            'клаус':[1,0,'hell'],
                            'гигант':[1,3,'mountain'],
                            'ями':[9,1,'hell'],
                            'подрывник':[8,5,'earth'],
                            'арбалетчик':[9,3,'earth'],
                            'кентавр':[10,3,'hell'],
                            'орк':[10,2,'mountain'],
                            'дворф':[10,2,'mountain'],
                            'рогги':[6,3,'hell'],
                            'суртур':[7,3,'hell'],
                            'лудорн':[8,3,'mountain'],
                            'друид':[7,4,'earth']
}
dict_card_price = {
                    'бард':'gold_bullion/4;',
                    'клаус':'gold_bullion/5;crystal/2',
                    'гигант':'gold_bullion/8;food/15',
                    'ями':'gold_bullion/4;crystal/1',
                    'подрывник':'gold_bullion/12;',
                    'арбалетчик':'gold_bullion/9;',
                    'кентавр':'gold_bullion/9;',
                    'орк':'gold_bullion/9;',
                    'дворф':'gold_bullion/9;',
}
city_cor_enter = [3,15]
list_cards_pl = [[None,1,2],['гигант',10,10],[None,3,5],[None,4,3],[None,2,3],[None,3,2]]
list_card_pl_reserv = [[None,1,2],[None,5,0],['подрывник',3,5],['арбалетчик',4,3],['гигант',2,3],['ями',3,2]]
list_cards_en = [['кентавр',10,3],[None,9,3],[None,10,0],[None,10,1],[None,5,2],[None,0,0]]
list_cards_menu_hero = list()
create_map(list_cells_lvl1, list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
 
list_paths_pressed = [['images/game_interface/to_hero.png','images/game_interface/to_hero_w.png'],['images/game_interface/to_castle.png','images/game_interface/to_castle_w.png',],['images/game_interface/end_moves.png','images/game_interface/end_moves_w.png',]]
list_cor_portals = [ [[0,3],[1,3]],[[0,3],[17,21]],[[0,3],[29,6]],[[0,3],[20,2]],[[0,3],[2,21]] ]

dict_bought_city = {
                    'camp':False,
                    'portal_resource':False,
                    'altar':False,
                    'church':False,
                    'forge':False,
                    
}
dict_price_city = {
                    'camp':'gold_bullion/10;food/10',
                    'portal_resource':'gold_bullion/20;stone/10;crystal/5',
                    'altar':'gold_bullion/15;stone/15;crystal/2;iron_bullion/5',
                    'church':'gold_bullion/25;stone/10;wood/10;food/15;crystal/4',
                    'forge':'gold_bullion/20;food/10;iron_bullion/10;stone/20;crystal/3',
}
    
create_icon_card(SCREEN_W=settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT'],
                    list_cards_pl=list_cards_pl,
                    list_card_pl_reserv=list_card_pl_reserv,
                    list_cards_menu_hero=list_cards_menu_hero)

cardgame_variables = {
    'need_to_play_final_music':True,#Нужно ли проиграть финальную музыку
    'flag_show_desc':30,#Флаг для показа описаний карт
    'flag_show_desc_skill':30,#Флаг для показа описания скилла
    'flag_show_error':30,#Флаг для показа ошибок
    'card_attacker': None,#Атакующая карта
    'card_victim':None,#Карта-жертва
    'card_that_move_pl':None,#
    'count_play_sound':50,#Счетчик для проигрыша звука взятой карты
    'index_picked_card':0,#Индекс взятой карты в списке
    'picked_card':None,#Взятая игроком карта
    'text_error_content': None,# Контент отображаемой ошибки
    'need_to_show_skill':False, # Нужно ли отображать целебое облако или мечь, при использовании скилла
    'active_skill':None,#Применяется ли скилл в данный момент
    'is_healing':None, #Происходит ли сейчас лечение 
    'card_that_showing_desc':None,   #Карта, описание которой нужно показать
    'who_move':'player', #Пременная означает, кто ходит
    'count_text_move':0, #Счетчик для отображения тескта для хода
    'card_that_move_index':0, #Индекс карты игрока, которая должна ходить  
    'card_that_move_en':None,#Карта, которая должна ходить у врага
    'index_card_that_move_en':0,# Индекс карты, которая должна ходить у врага
    'flag_animation_attack':0, #Счетчик для анимации атаки
    "double_damage":None,  #Должна ли атакующая карта делать двойной урон
    'healed_card':None,#Карта, которую нужно похилить
    'hp_for_heal':None,# Кол-во хп, которое нужно прибавить карте
    'who_won':None,#Означает, кто победил
    'hp_text':None#Объект текста, который отображает прибавляемое хп карте
}
dict_arguments = {
    'flag_show_error':flag_show_error,
    'CENTER_CELL_COR':CENTER_CELL_COR,
    'draw_cells':draw_cells,
    'scene':scene,
    'buttonIsPressed':buttonIsPressed,
    'flag_to_move_to_hero':flag_to_move_to_hero,
    'game':game,
    'card_pressed':card_pressed,
    'index_card':index_card,
    'artifact_pressed':artifact_pressed,
    'artifact_chest':artifact_chest,
    'list_cor_player_xy':list_cor_player_xy,
    'LENGTH_MAP_LVL1':LENGTH_MAP_LVL1,
    'W_CELL_MINI_MAP':W_CELL_MINI_MAP,
    'H_CELL_MINI_MAP':H_CELL_MINI_MAP,
    'X_FRAME_MM':X_FRAME_MM,
    'Y_FRAME_MM':Y_FRAME_MM,
    'list_cells_MM':list_cells_MM,
    'recourse_sounds':recourse_sounds,
    'resources_dict':resources_dict,
    'settings':settings,
    'change_exp_x':change_exp_x,
    'max_exp_lvl':max_exp_lvl,
    'max_mana':max_mana,
    'skill_cost':skill_cost,
    'flag_show_new_day':flag_show_new_day,
    'change_mana_x':change_mana_x,
    'flag_button_end':flag_button_end,
    'past_resources_dict':past_resources_dict,
    'flag_use_fountain_exp':flag_use_fountain_exp,
    'flag_use_fountain_mana':flag_use_fountain_mana,
    'flag_use_royal_academy':flag_use_royal_academy,
    'flag_use_tavern':flag_use_tavern,
    'flag_buy_skill':flag_buy_skill,
    'flag_show_tavern':flag_show_tavern,
    'flag_new_lvl':False,
    'flag_use_shack':True,
    'flag_show_error_next_week':flag_show_error_next_week,
    'dict_artifact_on_past':dict_artifact_on_past,
    'flag_market_selected':flag_market_selected,
    'flag_market_aritfact_no_slots':flag_market_aritfact_no_slots,
    'flag_not_enough_gold':flag_not_enough_gold,
    'number_opened_card':number_opened_card,
    'flag_buy_card':flag_buy_card,
    'flag_show_error_not_inventory':flag_show_error_not_inventory,
    'flag_show_error_locked':flag_show_error_locked,
    'flag_show_error_blocked_camp':flag_show_error_blocked_camp,
    'dict_bought_city':dict_bought_city,
    'flag_church':flag_church,
    'flag_forge':flag_forge,
    'flag_show_error_bought_card':flag_show_error_bought_card,
    'past_lvl_skill_fight':flag_new_lvl_skill_fight,
    'list_cor_castle_xy':list_cor_castle_xy,
    'flag_show_shack':flag_show_shack,
    'flag_show_fountain_mana':flag_show_fountain_mana,
    'flag_show_fountain_exp':flag_show_fountain_exp,
    'flag_build_alredy_bought':flag_build_alredy_bought,
    'flag_not_enough_resource':flag_not_enough_resource,
    'flag_buy_previous_build':flag_buy_previous_build,
    'trophy_exp':trophy_exp,
    'trophy_gold':trophy_gold,
    'list_cards_en':list_cards_en,
    'count_animation':count_animation,
    'cardgame_variables':cardgame_variables,
    'list_losed_card_enemy':list_losed_card_enemy,
    'list_losed_card_pl':list_losed_card_pl,
    'changed_hp':changed_hp,
    'changed_dmg':changed_dmg,
    'index_water':index_water,
}