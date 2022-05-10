from const import *
from Hero import Main_Hero
from Menu import Menu
#Создаем окно, с параметром БЕЗ РАМКИ
if settings['FULLSCREEN'] == True:
    win = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']),pygame.FULLSCREEN)#
elif settings['FULLSCREEN'] == False:
    win = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))#

player_lvl1 = Main_Hero(
                        x=0,y=0,
                        height=settings['SCREEN_WIDTH']//19,width=settings['SCREEN_WIDTH']//19,
                        path='images/player/player_front.png',
                        SCREEN_W=settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT'],
                        where_move=where_move,count_move=int(settings['COUNT_MOVE']),
                        win=win,count_step=int(settings['COUNT_STEP_HERO']))
#Контент ошибки 
text_error_content = None
# Рамка для ошибки
frame_error = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//8, settings['SCREEN_WIDTH']//3, settings['SCREEN_HEIGHT']//4, 'images/error_sheet.png')
frame_notification = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//3.5, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//3.5, settings['SCREEN_WIDTH']//3.5*2, settings['SCREEN_HEIGHT']//3.5*2, 'images/notification_sheet.png')
frame_new_day = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//3.5, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//3.5, settings['SCREEN_WIDTH']//3.5*2, settings['SCREEN_HEIGHT']//3.5*2, 'images/notification_sheet.png')

# Объект текста ошибки
error_text_obj = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red',None,frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10)
portal = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/portal.png')
#Картинки клеточек для мини карты
green = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green.png')
black = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/black.png')
yellow = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/yellow.png')
white = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/white.png')
green_dark = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green_dark.png')

#Строения

fountain_exp = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/buildings/fountain_exp.png')
fountain_mana = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/buildings/fountain_mana.png')
gemsmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/gemsmine.png')
farm = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/farm.png')
goldmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/goldmine.png')
ironmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/ironmine.png')
sawmill = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/sawmill.png')
stonebreaker = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/stinebreaker.png')
watchtower = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5,'images/buildings/watchtower.png')
# royal_academy = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5,'images/buildings/royal_academy.png')
# tavern = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5,'images/buildings/tavern.png')
# template = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5,'images/buildings/template.png')
# shack = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5,'images/buildings/shack.png')

#Ресурсы
mana_img = Graphic_elements(x=settings['SCREEN_WIDTH']//1.15,y=settings['SCREEN_HEIGHT']//1.59,width=settings['SCREEN_WIDTH']//50,height=settings['SCREEN_WIDTH']//50,path='images/mana.png')
gold = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/resources/gold.png')
iron = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/resources/iron.png')
crystal = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5, 'images/resources/gems.png')
wood = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/resources/wood.png')
stone = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/resources/stone.png')
apple = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1, settings['SCREEN_WIDTH']//19*6.7, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/apple.png')
iron_bullion = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1, settings['SCREEN_WIDTH']//19*7.5, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/iron_bullion.png')
wood2 = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1, settings['SCREEN_WIDTH']//19*8.3, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/wood.png')
gold_bullion = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*1.4//1, settings['SCREEN_WIDTH']//19*6.7, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/gold_bullion.png')
exp_img = Graphic_elements(x=settings['SCREEN_WIDTH']//1.23,y=settings['SCREEN_HEIGHT']//1.7,width=settings['SCREEN_WIDTH']//50,height=settings['SCREEN_WIDTH']//50,path='images/exp.png')
crystal_purified = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*1.4//1, settings['SCREEN_WIDTH']//19*7.5, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/cristal.png')
stone_purified = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*1.4//1, settings['SCREEN_WIDTH']//19*8.3, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/stone2.png')
tree_full = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5, 'images/resources/tree_full.png')
tree = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19*1.5, 'images/resources/tree.png')

button_to_hero = Graphic_elements( settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1 +settings['SCREEN_WIDTH']//13.5,settings['SCREEN_WIDTH']//19*4.7,settings['SCREEN_WIDTH']//15,settings['SCREEN_WIDTH']//30,'images/game_interface/to_hero.png')
button_to_castle = Graphic_elements( settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1 +settings['SCREEN_WIDTH']//13.5,settings['SCREEN_WIDTH']//19*4.7 + settings['SCREEN_WIDTH']//30,settings['SCREEN_WIDTH']//15,settings['SCREEN_WIDTH']//30,'images/game_interface/to_castle.png')
button_end_move = Graphic_elements(settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//7.6, settings['SCREEN_HEIGHT']-settings['SCREEN_HEIGHT']//11, settings['SCREEN_WIDTH']//9,settings['SCREEN_HEIGHT']//20 , 'images/game_interface/end_moves.png')
button_menu_hero_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-settings['SCREEN_WIDTH']//19,settings['SCREEN_WIDTH']//19*2,settings['SCREEN_WIDTH']//19,'images/menu_hero_back_y.png')
button_play = Menu(settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//10, settings['SCREEN_WIDTH']//8, settings['SCREEN_HEIGHT']//9,path='images/menu/play_b.png',image_button_b='images/menu/play_b.png',image_button_y='images/menu/play_y.png',x_divider=15,y_divider=10)
button_help = Menu(settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//3.5, settings['SCREEN_WIDTH']//8, settings['SCREEN_HEIGHT']//9, 'images/menu/help_b.png',image_button_b='images/menu/help_b.png',image_button_y='images/menu/help_y.png',x_divider=15,y_divider=3.5)
button_set = Menu(settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//2.1, settings['SCREEN_WIDTH']//8, settings['SCREEN_HEIGHT']//9, 'images/menu/settings_b.png',image_button_b='images/menu/settings_b.png',image_button_y='images/menu/settings_y.png',x_divider=15,y_divider=2.1)
button_exit = Menu(settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//8, settings['SCREEN_HEIGHT']//9, 'images/menu/exit_b.png',image_button_b='images/menu/exit_b.png',image_button_y='images/menu/exit_y.png',x_divider=15,y_divider=1.5)
list_buttons = [button_play,button_help,button_set,button_exit] 



#Текст
#Текст стоимость скиллов 
text_mana_cost_click = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'blue','  Нажмите;для покупки;за '+str(skill_cost)+' маны',settings['SCREEN_WIDTH']//320,settings['SCREEN_HEIGHT']//2.21,index=3)
#Текст нового уровня
text_new_lvl = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','Поздровляем! У вас новый уровень;Выберите улучшение способности;'+'Новый уровень - '+str(characteristic_dict['lvl']+1),settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//19*4,settings['SCREEN_HEIGHT']//2-settings['SCREEN_WIDTH']//19*2,index=3)
#Текст опыта и уровня
text_lvl_hero = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'yellow','Текущий уровень - '+str(characteristic_dict['lvl'])+';До следующего уровня:',settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//2,index=2)
text_exp_hero = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'green',str(characteristic_dict['exp'])+'/'+str(max_exp_lvl),settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//1.7)
#Текст количества ходов
text_step_count = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//65,'white','Осталось ходов: '+str(player_lvl1.count_step),settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//6.8,settings['SCREEN_HEIGHT']-settings['SCREEN_HEIGHT']//7.5)
#Текст нового дня
text_new_day = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','           Новый день;        Получено за день; ;Яблок - 0 Золота - 0; ;Железа - 0 Кристаллов - 0; ;Камня - 0 Дерева - 0',frame_new_day.X+settings['SCREEN_WIDTH']//19,frame_new_day.Y+settings['SCREEN_WIDTH']//19,index=8)
#Текст сундука 
chest_text_gold =  Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red','   Нет места для артефакта;   Вы забираете золото',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10,index=2)
chest_text_choice = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','Выберите награду;       или',settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//9.5,settings['SCREEN_HEIGHT']//2-settings['SCREEN_WIDTH']//19*2,index=2)
#Текст даты 
text_date = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'white','День: '+str(characteristic_dict['day'])+';Неделя: '+str(characteristic_dict['week']),settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1,  settings['SCREEN_WIDTH']//19+settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1*(LENGTH_MAP_LVL1+2),index=2)
#Текст кол-во маны
text_mana = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'blue','Мана: '+str(characteristic_dict['mana'])+'/'+str(max_mana),settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//1.59)
#Картинки иконок ресурсов
amount_food = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.2//1,settings['SCREEN_WIDTH']//19*6.9)
amount_iron = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.2//1,settings['SCREEN_WIDTH']//19*7.7)
amount_wood = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.2//1,settings['SCREEN_WIDTH']//19*8.4)
amount_gold = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//29, settings['SCREEN_WIDTH']//19*6.9)
amount_crystal=Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//29, settings['SCREEN_WIDTH']//19*7.7)
amount_stone = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//43,'white','0',settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//29, settings['SCREEN_WIDTH']//19*8.4)
amount_money = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*1.4//1, settings['SCREEN_WIDTH']//19*6.7,settings['SCREEN_WIDTH']//19*1.5, settings['SCREEN_WIDTH']//19*1.5, 'images/resources/gold_bullion.png')
#Туман войны
fog_war = Graphic_elements(None,None,settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19,'images/fog_war.bmp')
#Интерфейс
interface_bg  = Graphic_elements(settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//19*3,0,settings['SCREEN_WIDTH']//19*3,settings['SCREEN_HEIGHT'],'images/game_interface/sheet.png')
frame = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1,  settings['SCREEN_WIDTH']//19*4.7, settings['SCREEN_WIDTH']//15, settings['SCREEN_WIDTH']//15, 'images/game_interface/ramka.png')
frame_mini_map = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1,  settings['SCREEN_WIDTH']//19 , settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1*(LENGTH_MAP_LVL1+2), settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1*(LENGTH_MAP_LVL1+2), 'images/game_interface/ramka.png')
elliot_img = Graphic_elements(settings['SCREEN_WIDTH'] - settings['SCREEN_WIDTH']//19*2.9//1 + settings['SCREEN_WIDTH']//350,  settings['SCREEN_WIDTH']//19*4.74, settings['SCREEN_WIDTH']//16, settings['SCREEN_WIDTH']//16, 'images/game_interface/elliot_img.png')
player_info = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//65,'white','Эллиот, ур 1',settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//19*3 + settings['SCREEN_WIDTH']//350,settings['SCREEN_WIDTH']//19*4.7 + settings['SCREEN_WIDTH']//15)
list_interface_button = [button_to_hero,button_to_castle,button_end_move]
menu_hero_icon_eliot = Graphic_elements(x=settings['SCREEN_WIDTH']//1.64,y=settings['SCREEN_HEIGHT']//2.08,width=settings['SCREEN_WIDTH']//8.25,height=settings['SCREEN_HEIGHT']//5.1,path='images/game_interface/elliot_img.png')

desc = Graphic_elements(settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//4,settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//4,settings['SCREEN_WIDTH']//2,settings['SCREEN_HEIGHT']//2,path=None)
desc_artifact = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//6,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_WIDTH']/3,path=None)
desc_base_skill = Graphic_elements(x=settings['SCREEN_WIDTH']//19,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_WIDTH']/3,path=None)
desc_skill_hero = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//6,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_WIDTH']/3,path=None)
#Cундук
chest = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19,settings['SCREEN_WIDTH']//19,path='images/chest/chest.png')
chest_open = Graphic_elements(settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//19*3,settings['SCREEN_HEIGHT']//2-settings['SCREEN_WIDTH']//19*3,settings['SCREEN_WIDTH']//19*6,settings['SCREEN_WIDTH']//19*6,path='images/chest/chest_open.png')

#Сцены
book = Graphic_elements(0, 0, settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'], 'images/book.png')
menu_hero = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/hero_menu.bmp')


#Звук отткрытия книги
sound_book = Sounds('sounds/book_opened.wav', settings['SOUNDS_VOLUME'])



list_all_artifact = [
    #Слоты героя 
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//2.18,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_WIDTH']//36.57,'images/artifacts/helmet_hero.png', name='helmet'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//1.71,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_WIDTH']//36.57,None, name='chest'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//1.09,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_WIDTH']//36.57,'images/artifacts/boots_fire.png', name='boots'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.43,settings['SCREEN_HEIGHT']//1.45,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_WIDTH']//36.57,None, name='sword'),
    Graphic_elements(settings['SCREEN_WIDTH']//1.92,settings['SCREEN_HEIGHT']//1.45,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_WIDTH']//36.57,'images/artifacts/shield_ice.png', name='shield'),
    #Резевные слоты
    Graphic_elements(settings['SCREEN_WIDTH']//1.39,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,None, name=None),
    Graphic_elements(settings['SCREEN_WIDTH']//1.39+settings['SCREEN_WIDTH']//10.49,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,None, name=None),
    Graphic_elements(settings['SCREEN_WIDTH']//1.39+2*settings['SCREEN_WIDTH']//10.49,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,'images/artifacts/boots_ice.png', name=None)
]
#Базовые скиллы
list_slots_base_skills = [
    Graphic_elements(settings['SCREEN_WIDTH']//51.2,settings['SCREEN_HEIGHT']//24,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_diplomacy.png'),
    Graphic_elements(settings['SCREEN_WIDTH']//7.11,settings['SCREEN_HEIGHT']//24,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_domesticpolitics.png'),
    Graphic_elements(settings['SCREEN_WIDTH']//3.87,settings['SCREEN_HEIGHT']//24,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_fight.png')
]





list_choice_base_skill = [
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-settings['SCREEN_WIDTH']//19.68-settings['SCREEN_WIDTH']//19*3,frame_notification.Y+settings['SCREEN_WIDTH']//19*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_diplomacy.png'),
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-settings['SCREEN_WIDTH']//19.68,frame_notification.Y+settings['SCREEN_WIDTH']//19*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_domesticpolitics.png'),
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-settings['SCREEN_WIDTH']//19.68+settings['SCREEN_WIDTH']//19*3,frame_notification.Y+settings['SCREEN_WIDTH']//19*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_WIDTH']//9.84,path='images/skills/skill_fight.png')
]
list_text_lvl_base_skills = [
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_diplomacy']),settings['SCREEN_WIDTH']//51.2,0),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_domesticpolitics']),settings['SCREEN_WIDTH']//7.11,0),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_fight']),settings['SCREEN_WIDTH']//3.87,0)
]

list_slots_skills_hero = [
    Graphic_elements(x=settings['SCREEN_WIDTH']//12.8,y=settings['SCREEN_HEIGHT']//1.61,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//11.07,path='images/skills/eliot/skill_earth_blessing.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//5.68,y=settings['SCREEN_HEIGHT']//1.61,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//11.07,path='images/skills/eliot/skill_lumberjack.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//12.8,y=settings['SCREEN_HEIGHT']//1.34,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//11.07,path='images/skills/eliot/skill_forest_path.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//5.68,y=settings['SCREEN_HEIGHT']//1.34,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//11.07,path='images/skills/eliot/skill_idol_people.png'),
    
    Graphic_elements(x=settings['SCREEN_WIDTH']//8.25,y=settings['SCREEN_HEIGHT']//2.21,width=settings['SCREEN_WIDTH']//14.22,height=settings['SCREEN_WIDTH']//14.22,path='images/skills/eliot/skill_leader.png')
    ]



with open('images/artifacts/artifact_list.txt','r') as file:
    for text in file:
        text = text.split(',')
    list_matrix_artifact = text

list_artifact_graphic_elements = list()
for i in list_matrix_artifact:
    artifact = Graphic_elements(0,0,settings['SCREEN_WIDTH']//19*1.5,settings['SCREEN_WIDTH']//19*1.5,path='images/artifacts/'+i+'.png')
    list_artifact_graphic_elements.append(artifact)

#Картинка зеленого флага
flag_green = Graphic_elements(0, 0, settings['SCREEN_WIDTH']//19, settings['SCREEN_WIDTH']//19, 'images/flags/flag_g.png')