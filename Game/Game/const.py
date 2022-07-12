import pygame
import os
from graphic_elements import*
from random import randint, choice
from Addition_Module import*
from Text import Font
import json
pygame.init()
settings = dict()
settings_display = dict()
with open('saves/settings_display.json','r') as file:
    settings_display = json.load(file)
with open('saves/config.json','r') as file:
    settings = json.load(file)
for key in settings_display.keys():
    settings[key] = settings_display[key]

if settings['AUTOSAVE'] == 'True':
    settings['AUTOSAVE'] = True
else:
    settings['AUTOSAVE'] = False
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

settings['SOUNDS_VOLUME'] = settings['SOUNDS_VOLUME']/100
settings['MUSIC_VOLUME'] = settings['MUSIC_VOLUME']/100

SCREEN_CELL_H = settings['SCREEN_HEIGHT']//10.8
SCREEN_CELL_W = settings['SCREEN_WIDTH']//19


list_losed_card_enemy = []
list_losed_card_pl = []
# Опыт и золото, которое получил игрок при победе
trophy_exp = 0
trophy_gold = 0

draw_cells = False
#Переменная, отвечающяя за сцену
scene = settings['SCENE']
#Создаем карту 1-го уровня
minute_in_game = 0
buttonIsPressed = False
#Влаг для перемещаения к игроку после телепорта
flag_to_move_to_hero = 0
#Переменная игры
game = True
card_pressed = None
index_card = None
artifact_pressed = None
#Игровой цикл
path_artifact_chest = None
time = pygame.time.Clock()
list_cor_player_xy = [0,0]
list_cor_castle_xy = [0,0]
#Размер карты первого уровня
LENGTH_MAP_LVL1 = 31
#Размер клеточки в мини-карте
W_CELL_MINI_MAP = settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1
H_CELL_MINI_MAP = settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1
# Координаты для старта отрисовки клеток в мини-карте
X_FRAME_MM, Y_FRAME_MM = settings['SCREEN_WIDTH']//1.17,  settings['SCREEN_WIDTH']//19 + settings['SCREEN_HEIGHT']//115.8 
# список клеток для мини-карты
list_cells_MM = list()
#Список из звуков подбора ресурсов
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
    'potion':0
}
dict_artifact_on = {
    'helmet':None,
    'sword':None,
    'chest':None,
    'boots':None,
    'shield':None,
}
dict_path_skills = {
                    'skill_earth_blessing':'images/skills/eliot/skill_earth_blessing.png',
                    'skill_lumberjack':'images/skills/eliot/skill_lumberjack.png',
                    'skill_forest_path':'images/skills/eliot/skill_forest_path.png',
                    'skill_idol_people':'images/skills/eliot/skill_idol_people.png',
                    'skill_leader':'images/skills/eliot/skill_leader.png',
}
dict_order_skills = {
                    'skill_leader':True,#Первый
                    
                    'skill_earth_blessing':False,#Слево
                    'skill_lumberjack':False,#Справо

                    'skill_forest_path':False,#Слево
                    'skill_idol_people':False,#Справо
}
list_learn_skills = list()
dict_artifact_on_past = dict_artifact_on.copy()
 
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
flag_not_enough_cards = 30
flag_market_aritfact_no_slots = 30
flag_not_enough_gold = 30
flag_show_error_not_inventory = 50
flag_show_error_locked = 30
flag_show_error_blocked_camp = 50
changed_hp = 0
changed_dmg = 0
flag_show_dialog = False
flag_show_error_bought_card = 30
index_water = 0
count_animation= 0
count_dialog_offer = 50
count_dialog_fight = 50
count_daily_event = 80
count_dialog_threat = 50
flag_fight_start_post = False
flag_church = True
flag_save = 50
skill_cost = 200
max_exp_lvl = 100
max_mana = 1000
mana_shack = 200
change_mana_x = 0
flag_offer = True
flag_show_offer = False
flag_fight_start = False
step_exp_text = settings['SCREEN_WIDTH']//93
change_exp_x = 0
flag_show_error_next_week = 30
flag_buy_skill = True
flag_use_royal_academy = True
number_opened_card = 2
count_dialog = 50
flag_dialog_offer_yes = False
flag_dialog_offer_no = False
flag_dialog_threat_win = False
flag_dialog_threat_lose = False
flag_dialog_fight = False
count_daily_event_post_fight = 80
daily_event = None
flag_mouse_volume_sound = False
flag_mouse_volume_music = False
index_fog = 0
flag_show_error_choose_icon = 30
flag_pause = False
dict_card_path_camp = {
                        "бард":'images/cards/бард_locked.png',
                        "гигант":'images/cards/гигант_locked.png',
                        "клаус":'images/cards/клаус_locked.png',
                        "друид":'images/cards/друид_locked.png',
                        "подрывник":'images/cards/подрывник_locked.png'
}
dict_card_name_camp = {
                        "бард": None,
                        "гигант":None,
                        "клаус":None,
                        "друид":None,
                        "подрывник":None,
}
list_card_camp_civ = ['бард','друид','клаус','гигант','подрывник']
dict_path_artifact = {
                        'helmet':None,
                        'chest':'images/artifacts/chest_ice.png',
                        'sword':None,
                        'shield':'images/artifacts/shield_fire.png',
                        'boots':'images/artifacts/boots_hero.png',

                        'reserv1':None,
                        'reserv2':None,
                        'reserv3':None,
}

list_daily_events = [
                    'post_fight',
                    'goblin',
                    'enemy',
                    'gold',
                    'heist',
                    'artifact',
                    'add_army',
                    'fog_more',
                    'fog_less',
                    'discount',
                    ]
#Список из клеток первого уровня
list_cells_lvl1 = [
                   list('0000000000000000000000000000000'),
                   list('00000000000000000tttttttt000000'),
                   list('00000000000000000t000000t0ckd00'),
                   list('0t000000000000000t000000tckdd00'),
                   list('0t0000000000000ttt00000cbkddgt0'),
                   list('0ttttt000000000t000000ckdddgjt0'),
                   list('0t000tttttt0000t000000addghj0t0'),
                   list('0t00000000t0000t0000cbkdgj000t0'),
                   list('0tt0000000t0000t0000adddl0000t0'),
                   list('0000000000tttttt0000adogj0000t0'),
                   list('0000000000t0000ttt00addl00000t0'),
                   list('0000000000t000000tttemdltttttt0'),
                   list('000000ttttt00000000tttdlt0000t0'),
                   list('00000tt000000cbbbfckdtdlt0000t0'),
                   list('t0000t0000000adddooddtttt0000t0'),
                   list('t0000t0000000adoddddg000t0000t0'),
                   list('tttttt000000ckdoodghj000t0000t0'),
                   list('000t0000000ckkdoodl000tttttttt0'),
                   list('000t0000000addooodnf0tt000000t0'),
                   list('000t0000000adooooddl0t0000000tt'),
                   list('000ttttttttбббббббббtt00000000t'),
                   list('tttt0000000adooooddl0t000000000'),
                   list('t000000000ckdoooddgj0t000000000'),
                   list('t000000000addddddgj00t000000000'),
                   list('t000000cbbkdghhhhj000t000000000'),
                   list('tt0000ckddddl000tttttt000000000'),
                   list('bbbf0ckddghhj00tt00000000000000'),
                   list('odtnfaddgj00000t000000000000000'),
                   list('ddddoodgj000000t000000000000000'),
                   list('dddddddl0000000t000000000000000'),
                   list('dddohhhj000000tt000000000000000')]

#Список-матрица объектов(персонаж, здания, ресурсы)
mat_objetcs_lvl1 =[ list('KkkP00000000БCл1000000000Nnгггг'),#M,p,P,E,g,i,c,w,T,t,F,f,H,h,D,d,N,n,R,r,X,x,C,W,A,B,e,m,s
                    list('kkk0000.0000лл110000.0000nn11гг'),#A,a-academia
                    list('kkk0000000001л1Hh0000P000.00вг1'),#J,j-taverna
                    list('0p0000000000Mл1hh0000.00000вв11'),#S-Хижина
                    list('00C000000000л110000000.0W0вв00S'),#B-Храм
                    list('00000W000000л10000000000ввв0000'),#\ / | л
                    list('00000000000л1100000E000вв00.000'),#
                    list('000.000000011000.000000в0000000'),#
                    list('000Jj000л10000.000000ввв000.000'),#
                    list('000jj000л100000000000вC00000000'),#
                    list('Глллллллл100000.00000вв0000.00C'),#
                    list('Cллл111111000000000000в00000000'),#
                    list('01111000000.000000000Ав0000E000'),#
                    list('S000000000.000000000в0в00000000'),#
                    list('0.0000Dd000000ввв00вв000000.000'),#
                    list('000000dd000000в0вввв00Oo0000000'),#
                    list('0000000000.000в00в0000oo0000000'),#
                    list('000.000000000ввXxв000P0000.0000'),#
                    list('000000000000вв0xxв00000.0000000'),
                    list('0000.000E000в.000вв.000000.0000'),
                    list('00P00000.00А00000П0000000000000'),
                    list('000000000000вRr00вв00000000лл1С'),
                    list('0Ff000000000вrr0ввC00000000л110'),
                    list('0ff000.0000вввввв000000лллл1100'),
                    list('00000000000в00000.0000W1111100C'),
                    list('0.000000вввв0000000000л100000лл'),
                    list('Б000000вв0000000.00000л10лллллл'),
                    list('Cвв000вв00000.00000000л1Рл11111'),
                    list('ввввW0в000000Aa0000000л10л10Ззз'),
                    list('ввввввв00.000aa000000лл10110ззз'),
                    list('вввC0000000000000И00M1л10Я00ззз')]
list_forest_element = ['|','\\','/','л']
list_story_end_cor = [[30,27],[28,27],[29,27]]
for el in range(len(mat_objetcs_lvl1)):
    for element in range(len(mat_objetcs_lvl1[el])):
        if mat_objetcs_lvl1[el][element] == 'л':
            mat_objetcs_lvl1[el][element] = choice(list_forest_element)
list_flower_element = ['1','2','3','4','0','0','0']
for el in range(len(list_cells_lvl1)):
    for element in range(len(list_cells_lvl1[el])):
        if list_cells_lvl1[el][element] == '0':
            list_cells_lvl1[el][element] = choice(list_flower_element)
list_untochable_cells = [ [1,3],[2,3],[3,3],[3,0],[3,1],[3,2] ]
with open('images/artifacts/artifact_list.txt','r') as file:
    for text in file:
        text = text.split(',')
    list_matrix_artifact = text
list_symbol_resource = ['i','g','w','c','T','b','']
for el in range(len(mat_objetcs_lvl1)):
    for element in range(len(mat_objetcs_lvl1[el])):
        if mat_objetcs_lvl1[el][element] == '.':
            mat_objetcs_lvl1[el][element] = choice(list_symbol_resource)
list_studied_map = [
                    [0,0],[0,1],[0,2],
                    [1,0],[1,1],[1,2],
                    [2,0],[2,1],[2,2],
                    ]
#Список, в которм будут храниться объекты клеток
list_objects_cells_lvl1 = []
dict_card_dialog = {
                    'бард':[
                        ['Бард: Кто хочет','сразиться? Первый удар','бесплатно! Ну, что?'],
                        ['Бард: Даже я не знаю','своих сил!'],
                        ['Бард: Спокойно, мне','не нужны проблемы'],
                        ['Бард: Благодарю'],
                        ['Бард: Очень жаль'],
                        ['Бард: Бард всегда не','прочь подраться!'],
                        ],
                    'клаус':[
                        ['Клаус: Какие чудеса','узрею я сегодня?'],
                        ['Клаус: Неплохо. Хотя','нет: это было ужасно.'],
                        ['Клаус: Я такое никогда','не забуду.'],
                        ['Клаус: Так себе плата.'],
                        ['Клаус: Очень жаль'],
                        ['Клаус: Готовься к','испытанию!'],
                        ],
                    'гигант':[
                        ['Гигант: Сила ведёт','меня.'],
                        ['Гигант: Не беспокойся,','твоим волнениям конец.'],
                        ['Гигант: Спокойно, мне','не нужны проблемы'],
                        ['Гигант: Подойдёт','Едва ли.'],
                        ['Гигант: Что ты за','рыцарь?'],
                        ['Гигант:  Я раздавлю','тебя своей железной','волей.'],
                        ],
                    'ями':[
                        ['Ями: Неутолимый голод','преисподней.'],
                        ['Ями: Взгляни в глаза','своему страху, мне.'],
                        ['Ями: Увидимся в','преисподней.'],
                        ['Ями: Благодарю'],
                        ['Ями: Очень жаль'],
                        ['Ями: Хе-ха-ха, со мной','вся ярость ада.'],
                        ],
                    'подрывник':[
                        ['Подрывник: БУМ-БУМ!','Взорву всё вокруг!'],
                        ['Подрывник: Ты умрешь,','но для науки'],
                        ['Подрывник: Спокойно,','мне не нужны проблемы'],
                        ['Подрывник: Благодарю'],
                        ['Подрывник: Очень жаль'],
                        ['Подрывник: Взрывчатыe','вещества опасны ровно','настолько, насколько','опасен человек,','который их строит'],
                        ],
                    'арбалетчик':[
                        ['Арбалетчик: Тетива',' всё упруже!'],
                        ['Арбалетчик: Один на','один со смертью…'],
                        ['Арбалетчик: Спокойно,','мне не нужны проблемы'],
                        ['Арбалетчик: Честная','сделка!'],
                        ['Арбалетчик: Очень жаль'],
                        ['Арбалетчик: Бросает в','дрожь от нетерпения!'],
                        ],
                    'кентавр':[
                        ['Кентавр: Я не позволю','контролировать меня'],
                        ['Кентавр: Ты умрёшь','и другие возрадуются.'],
                        ['Кентавр: Спокойно,','мне не нужны проблемы'],
                        ['Кентавр: Благодарю'],
                        ['Кентавр: Очень жаль'],
                        ['Кентавр: Я растопчу','тебя в пыль!'],
                        ],
                    'орк':[
                        ['Орк: Ргррхрхрх!'],
                        ['Орк: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Орк: Спокойно я уйду'],
                        ['Орк: Благодарю'],
                        ['Орк: Очень жаль'],
                        ['Орк: Да начнётся','битва!'],
                        ],
                    'дворф':[
                        ['Дворф: Я лучший кузнец','этого мира!'],
                        ['Дворф: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Дворф: Спокойно, мне','не нужны проблемы'],
                        ['Дворф: Благодарю'],
                        ['Дворф: Очень жаль'],
                        ['Дворф: Да начнётся','битва!'],
                        ],
                    'рогги':[
                        ['Рогги: Не вставай',' у меня на пути!'],
                        ['Рогги: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Рогги: Спокойно, мне','не нужны проблемы'],
                        ['Рогги: Благодарю'],
                        ['Рогги: Очень жаль'],
                        ['Рогги: Да начнётся','битва!'],
                        ],
                    'суртур':[
                        ['Суртур: Огненный меч','правит судьбой'],
                        ['Суртур: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Суртур: Спокойно, мне','не нужны проблемы'],
                        ['Суртур: Благодарю'],
                        ['Суртур: Очень жаль'],
                        ['Суртур: Да начнётся','битва!'],
                        ],
                    'лудорн':[
                        ['Лудорн: Мой,Брат','глупец!'],
                        ['Лудорн: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Лудорн: Спокойно, мне','не нужны проблемы'],
                        ['Лудорн: Благодарю'],
                        ['Лудорн: Очень жаль'],
                        ['Лудорн: Да начнётся','битва!'],
                        ],
                    'друид':[
                        ['Друид: Я покровитель','леса.'],
                        ['Друид: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Друид: Спокойно, мне','не нужны проблемы'],
                        ['Друид: Благодарю'],
                        ['Друид: Очень жаль'],
                        ['Друид: Да начнётся','битва!'],   
                        ],
                    'голем':[
                        ['Голем: Братья мои!','Вставайте!'],
                        ['Голем: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Голем: Спокойно, мне','не нужны проблемы'],
                        ['Голем: Благодарю'],
                        ['Голем: Очень жаль'],
                        ['Голем: Да начнётся','битва!'],
                        ],
                    'рудорн':[
                        ['Рудорн: Мой,Брат','глупец!'],
                        ['Рудорн: Думаешь, мне','страшно? Я с тебя','шкуру сдеру!'],
                        ['Рудорн: Спокойно, мне','не нужны проблемы'],
                        ['Рудорн: Благодарю'],
                        ['Рудорн: Очень жаль'],
                        ['Рудорн: Да начнётся','битва!'],
                        ],
}
list_choice_slots_market = [
                            choice(list_matrix_artifact),
                            choice(list_matrix_artifact),
                            choice(list_matrix_artifact),
]
dict_card_characteristics = {
                            'бард':[7,2,'earth'],
                            'клаус':[10,0,'hell'],
                            'гигант':[12,3,'mountain'],
                            'ями':[9,1,'hell'],
                            'подрывник':[8,5,'earth'],
                            'арбалетчик':[9,3,'earth'],
                            'кентавр':[10,3,'hell'],
                            'орк':[10,2,'mountain'],
                            'дворф':[10,2,'mountain'],
                            'рогги':[6,3,'hell'],
                            'суртур':[7,3,'hell'],
                            'лудорн':[8,3,'mountain'],
                            'друид':[7,4,'earth'],
                            'голем':[10,5,'mountain'],
                            'рудорн':[6,3,'hell'],
}
dict_card_characteristics_enemy = {
                            'бард':[7,2,'earth'],
                            'клаус':[10,0,'hell'],
                            'гигант':[12,3,'mountain'],
                            'ями':[9,1,'hell'],
                            'подрывник':[8,5,'earth'],
                            'арбалетчик':[9,3,'earth'],
                            'кентавр':[10,3,'hell'],
                            'орк':[10,2,'mountain'],
                            'дворф':[10,2,'mountain'],
                            'рогги':[6,3,'hell'],
                            'суртур':[7,3,'hell'],
                            'лудорн':[8,3,'mountain'],
                            'друид':[7,4,'earth'],
                            'король_гоблинов':[20,10,'earth'],
                            'гоблин':[5,2,'earth'],
                            'голем':[10,5,'mountain'],
                            'рудорн':[6,3,'hell'],

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
                    'гоблин':'gold_bullion/1;',
                    'король_гоблинов':'gold_bullion/2;',
                    'рогги':'gold_bullion/4;',
                    'суртур':'gold_bullion/4;iron_bullion/2;',
                    'лудорн':'gold_bullion/6;',
                    'друид':'gold_bullion/4;wood/8;',
                    'голем':'gold_bullion/7;stone/18;',
                    'рудорн':'gold_bullion/4;',

}
dict_count_resource = {
    'wood':20,
    'iron_bullion':20,
    'stone':20,
    'crystal':20,
    'food':20,
}
city_cor_enter = [3,1]
list_cards_pl = [['бард',1,2],[None,10,10],[None,3,5],['гигант',4,3],['клаус',2,3],[None,3,2]]
list_cards_pl_post_army = [[None,1,2],['бард',10,10],[None,3,5],['подрывник',4,3],[None,2,3],[None,3,2]]
list_card_pl_reserv = [[None,1,2],[None,5,0],['бард',3,5],[None,4,3],[None,2,3],[None,3,2]]
list_cards_en = [[None,10,3],[None,9,3],[None,10,0],[None,10,1],[None,5,2],[None,0,0]]
list_cards_menu_hero = list()
list_cards_enemy_castle = [['король_гоблинов',20,10],['гоблин',2,2],['гоблин',2,2],['гоблин',2,2],['гоблин',2,2],['гоблин',2,2]]
create_map(list_cells_lvl1, list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
list_paths_pressed = [['images/game_interface/to_hero.png','images/game_interface/to_hero_w.png'],['images/game_interface/pause.png','images/game_interface/pause_w.png',],['images/game_interface/end_moves.png','images/game_interface/end_moves_w.png',]]
list_cor_portals = [ [[0,3],[1,3]],[[0,3],[17,21]],[[0,3],[29,6]],[[0,3],[20,2]],[[0,3],[2,21]] ]
list_cards_symbol = ['А','Д','Б','Г','Е','К','Л','О','П','Р','С','Я','В']
dict_bought_city = {
                    'camp':False,
                    'portal':False,
                    'altar':False,
                    'church':False,
                    'forge':False,
                    
}
dict_price_city = {
                    'camp':'gold_bullion/10;food/10',
                    'portal':'gold_bullion/20;stone/10;crystal/5',
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
    'card_that_move_pl':None,
    'card_victim':None,#Карта-жертва
    'count_play_sound':50,#Счетчик для проигрыша звука взятой карты
    'index_picked_card':0,#Индекс взятой карты в списке
    'picked_card':None,#Взятая игроком карта
    'text_error_content': None,# Контент отображаемой ошибки
    'need_to_show_skill':False, # Нужно ли отображать целебое облако или мечь, при использовании скилла
    'active_skill':None,#Применяется ли скилл в данный момент
    'is_healing':None, #Происходит ли сейчас лечение 
    'card_that_showing_desc':None,#Карта, описание которой нужно показать
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
    'path_artifact_chest':path_artifact_chest,
    'list_cor_player_xy':list_cor_player_xy,
    'LENGTH_MAP_LVL1':LENGTH_MAP_LVL1,
    'W_CELL_MINI_MAP':W_CELL_MINI_MAP,
    'H_CELL_MINI_MAP':H_CELL_MINI_MAP,
    'X_FRAME_MM':X_FRAME_MM,
    'Y_FRAME_MM':Y_FRAME_MM,
    'list_cells_MM':list_cells_MM,
    'resources_dict':resources_dict,
    'change_exp_x':change_exp_x,
    'max_exp_lvl':max_exp_lvl,
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
    'count_text_new_game':150,
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
    'flag_show_dialog':flag_show_dialog,
    'flag_show_offer':flag_show_offer,
    'flag_offer':flag_offer,
    'flag_fight_start':flag_fight_start,
    'flag_not_enough_cards':flag_not_enough_cards,
    'count_dialog':count_dialog,
    'flag_dialog_offer_yes':flag_dialog_offer_yes,
    'flag_dialog_offer_no':flag_dialog_offer_no,
    'flag_dialog_threat_win':flag_dialog_threat_win,
    'flag_dialog_threat_lose':flag_dialog_threat_lose,
    'flag_dialog_fight':flag_dialog_fight,
    'daily_event':daily_event,
    'count_daily_event':count_daily_event,
    'flag_fight_start_post':flag_fight_start_post,
    'count_daily_event_post_fight':count_daily_event_post_fight,
    'index_fog':index_fog,
    'minute_in_game':minute_in_game,
    'flag_mouse_volume_sound':flag_mouse_volume_sound,
    'flag_save':flag_save,
    'flag_mouse_volume_music':flag_mouse_volume_music,
    'characteristic_dict':characteristic_dict,
    'mat_objetcs_lvl1':mat_objetcs_lvl1,
    'list_studied_map':list_studied_map,
    'list_cards_pl':list_cards_pl,
    'list_cards_pl_post_army':list_cards_pl_post_army,
    'list_card_pl_reserv':list_card_pl_reserv,
    'dict_path_artifact':dict_path_artifact,
    'dict_path_skills':dict_path_skills,
    'list_capture_buildings':list(),
    'list_capture_buildings_symbol':list(),
    'list_choice_slots_market':list_choice_slots_market,
    'list_matrix_artifact':list_matrix_artifact,
    'dict_count_resource':dict_count_resource,
    'gold_count_enemy':0,
    'name_card':None,
    'text_tavern_font_content':None,
    'flag_show_error_choose_icon':flag_show_error_choose_icon,
    'flag_pause':flag_pause,
    'civ_selected':None,
    'flag_show_dialog_potion':False,
    'count_dialog_potion':50,
    'flag_show_deal':False,
    'text_potion':None,
    'gold_count_potion':0,
    'dict_order_skills':dict_order_skills,
    'count_error_bought_skill':30,
    'dict_card_path_camp':dict_card_path_camp,
    'index_text_card':0,
    'name_card_camp':None,
    'list_card_camp_civ':list_card_camp_civ,
    'dict_card_name_camp':dict_card_name_camp,
    'hero_skill_path':None,
    'hero_skill_name':None,
}

new_game_dict = dict_arguments.copy()
if os.path.exists('saves/config1.json'):
    with open('saves/config1.json','r') as file:
        dict_arguments = json.load(file)
dict_arguments['game'] = True
