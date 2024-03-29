from const import *
from Hero import Main_Hero
from Menu import Menu
from random import choice
from cards_class import Cards
from graphic_elements_cards import Graphic_elements_cards
from sounds import Sounds,Music
from Text import Font
import Text_cardgame
#Создаем окно, с параметром БЕЗ РАМКИ
if settings['FULLSCREEN'] == True:
    width_fullscreen = pygame.display.Info().current_w
    height_fullscreen = pygame.display.Info().current_h
    win = pygame.display.set_mode((width_fullscreen, height_fullscreen),pygame.FULLSCREEN)#
    settings_display['SCREEN_HEIGHT'] = 720
    settings_display['SCREEN_WIDTH'] = 1280
elif settings['FULLSCREEN'] == False:
    win = pygame.display.set_mode((settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT']))#
win_rect = Rect(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
player_lvl1 = Main_Hero(
                        x=0,y=0,
                        height=SCREEN_CELL_W,width=SCREEN_CELL_W,
                        path='images/player/player_front.png',
                        SCREEN_W=settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT'],
                        where_move=where_move,count_move=int(settings['COUNT_MOVE']),
                        win=win,count_step=dict_arguments['characteristic_dict']['count_step'])
dialog_book = Graphic_elements(x=SCREEN_CELL_W,y=SCREEN_CELL_H,width=SCREEN_CELL_W*14,height=SCREEN_CELL_H*7.5,path='images/dialog_book.png')
elliot_img = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9 + settings['SCREEN_WIDTH']//350,  SCREEN_CELL_W*4.74, settings['SCREEN_WIDTH']//16, settings['SCREEN_HEIGHT']//7.5, 'images/game_interface/elliot_img.png')
player_info = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//65,'white','Уровень '+str(dict_arguments['characteristic_dict']['lvl']),elliot_img.X,elliot_img.Y +elliot_img.HEIGHT+ settings['SCREEN_HEIGHT']//100)
game_icon = Graphic_elements(settings['SCREEN_WIDTH']//1.6,0,SCREEN_CELL_W*5,SCREEN_CELL_H*10,'images/game_icon.png')
#Объекты матрицы
flower0 = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/flower0.png')
flower1 = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/flower1.png')
flower2 = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/flower2.png')
flower3 = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/flower3.png')
list_forest =[]
for i in range(4):
    forest = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W*2,height=SCREEN_CELL_H*2,path='images/MatrixImage/forest'+str(i)+'.png')
    list_forest.append(forest)
field_path = Graphic_elements(x=0,y=0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/field_path.png')
mountain = Graphic_elements(0, 0, SCREEN_CELL_W*2, SCREEN_CELL_H*2, 'images/MatrixImage/mountain.png')
list_water = []
for i in range(5):
    water = Graphic_elements(0,0,width=SCREEN_CELL_W,height=SCREEN_CELL_H,path='images/MatrixImage/water'+str(i)+'.png')
    list_water.append(water)
water = choice(list_water)
bridge = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_H, 'images/MatrixImage/bridge.png')
#Помощь
button_back_help = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H*1,SCREEN_CELL_W*3,SCREEN_CELL_H*1,path='images/menu_hero_back_y.png')
button_next_help = Graphic_elements(settings['SCREEN_WIDTH']-SCREEN_CELL_W*3,settings['SCREEN_HEIGHT']-SCREEN_CELL_H*1,SCREEN_CELL_W*3,SCREEN_CELL_H*1,path='images/button_continue_story_y.png')
button_leave_help = Graphic_elements(settings['SCREEN_WIDTH']//2 - SCREEN_CELL_W*1.5,settings['SCREEN_HEIGHT']-SCREEN_CELL_H*1,SCREEN_CELL_W*3,SCREEN_CELL_H*1,path='images/button_continue_story_y.png')
help_scene1 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene1.png')
help_scene2 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene2.png')
help_scene3 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene3.png')
help_scene4 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene4.png')
help_scene5 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene5.png')
help_scene6 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene6.png')
help_scene7 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene7.png')
help_scene8 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene8.png')
help_scene9 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene9.png')
help_scene10 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene10.png')
help_scene11 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene11.png')
help_scene12 = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/help/help_scene12.png')
#Контент ошибки 
text_error_content = None
# Рамка для ошибки
frame_error = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//8, settings['SCREEN_WIDTH']//3, settings['SCREEN_HEIGHT']//4, 'images/error_sheet.png')
frame_buildings = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//7, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//8, settings['SCREEN_WIDTH']//3.5, settings['SCREEN_HEIGHT']//4, 'images/notification_sheet.png')
frame_notification = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//3.5, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//3.5, settings['SCREEN_WIDTH']//3.5*2, settings['SCREEN_HEIGHT']//3.5*2, 'images/notification_sheet.png')
frame_new_day = Graphic_elements(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//3.5, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//3.5, settings['SCREEN_WIDTH']//3.5*2, settings['SCREEN_HEIGHT']//3.5*2, 'images/notification_sheet.png')
# Объект текста ошибки
error_text_obj = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red',None,frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10)
portal = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/portal.png')
#Картинки клеточек для мини карты
green = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green.png')
black = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/fog_war.bmp')
yellow = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/yellow.png')
white = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/white.png')
green_dark = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,'images/green_dark.png')
mountain_mm = Graphic_elements(0, 0, W_CELL_MINI_MAP,H_CELL_MINI_MAP, 'images/MatrixImage/mountain.png')
water_mm = Graphic_elements(0,0,W_CELL_MINI_MAP,H_CELL_MINI_MAP,path='images/MatrixImage/water0.png')
forest_mm = Graphic_elements(x=0,y=0,width=W_CELL_MINI_MAP,height=H_CELL_MINI_MAP,path='images/forestmm.png')
field_path_mm = Graphic_elements(x=0,y=0,width=W_CELL_MINI_MAP,height=H_CELL_MINI_MAP,path='images/MatrixImage/field_path.png')
red_mm = Graphic_elements(x=0,y=0,width=W_CELL_MINI_MAP,height=H_CELL_MINI_MAP,path='images/red_mm.png')
#Строения
fountain_exp = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_H*2, 'images/buildings/fountain_exp.png')
fountain_mana = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_H, 'images/buildings/fountain_mana.png')
fountain_exp_empty = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_H*2, 'images/buildings/fountain_exp_empty.png')
fountain_mana_empty = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_H, 'images/buildings/fountain_mana_empty.png')
gemsmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(SCREEN_CELL_H*2),'images/buildings/gemsmine.png')
farm = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(SCREEN_CELL_H*2),'images/buildings/farm.png')
goldmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(SCREEN_CELL_H*2),'images/buildings/goldmine.png')
ironmine = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(SCREEN_CELL_H*2),'images/buildings/ironmine.png')
sawmill = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/sawmill.png')
stonebreaker = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/stinebreaker.png')
watchtower = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_W*1.5,'images/buildings/watchtower.png')
royal_academy = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/royal_academy.png')
tavern = Graphic_elements(0,0,int(settings['SCREEN_WIDTH']//9.5),int(settings['SCREEN_WIDTH']//9.5),'images/buildings/tavern.png')
# template = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_W*1.5,'images/buildings/template.png')
shack = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_W*1.5,'images/buildings/shack.png')
market = Graphic_elements(0,0,SCREEN_CELL_W*2, SCREEN_CELL_W*2,'images/buildings/market.png')
city = Graphic_elements(0,0,SCREEN_CELL_W*3, SCREEN_CELL_W*3,'images/buildings/castle.png')
man_potion = Graphic_elements(0,0,SCREEN_CELL_W, SCREEN_CELL_W*1.5,'images/man_potion.png')
#Строения города
castle = Graphic_elements(x=settings['SCREEN_WIDTH']//2.2,y=0,width=settings['SCREEN_WIDTH']//3.65,height=settings['SCREEN_HEIGHT']//3.6,path = 'images/city/castle.png')
camp = Graphic_elements(x=settings['SCREEN_WIDTH']//2.8,y=settings['SCREEN_HEIGHT']//3,width=settings['SCREEN_WIDTH']//6.4,height=settings['SCREEN_HEIGHT']//5.53,path = 'images/city/camp.png')
church = Graphic_elements(x=settings['SCREEN_WIDTH']//1.79,y=settings['SCREEN_HEIGHT']//1.58,width=settings['SCREEN_WIDTH']//6.73,height=settings['SCREEN_HEIGHT']//4.8,path = 'images/city/church.png')
altar = Graphic_elements(x=settings['SCREEN_WIDTH']//1.33,y=settings['SCREEN_HEIGHT']//4,width=settings['SCREEN_WIDTH']//4.57,height=settings['SCREEN_HEIGHT']//4.8,path = 'images/city/altar.png')
forge = Graphic_elements(x=settings['SCREEN_WIDTH']//1.2,y=settings['SCREEN_HEIGHT']//1.58,width=settings['SCREEN_WIDTH']//6.4,height=settings['SCREEN_HEIGHT']//4.36,path = 'images/city/forge.png')
portal_resource = Graphic_elements(x=settings['SCREEN_WIDTH']//3.72,y=settings['SCREEN_HEIGHT']//1.6,width=settings['SCREEN_WIDTH']//6.56,height=settings['SCREEN_HEIGHT']//4.5,path = 'images/city/portal.png')
#Замок гоблниа
castle_goblin = Graphic_elements(0,0,SCREEN_CELL_W*3, SCREEN_CELL_W*3,path = 'images/goblin_camp.png')
#Ресурсы
mana_img = Graphic_elements(x=settings['SCREEN_WIDTH']//1.21,y=settings['SCREEN_HEIGHT']//1.59,width=settings['SCREEN_WIDTH']//50,height=settings['SCREEN_HEIGHT']//28.125,path='images/mana.png')
gold = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/resources/gold.png')
iron = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/resources/iron.png')
crystal = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W*1.5, 'images/resources/gems.png')
wood = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/resources/wood.png')
stone = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/resources/stone_liana.png')
tree_full = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W*1.5, 'images/resources/tree_full.png')
tree = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W*1.5, 'images/resources/tree.png')

apple = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9//1, player_info.font_y+settings["SCREEN_HEIGHT"]//30, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/food.png')
iron_bullion = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*1.4//1, apple.Y, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/iron_bullion.png')
wood2 = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9//1, apple.Y+apple.HEIGHT+settings["SCREEN_HEIGHT"]//40, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/wood.png')
gold_bullion = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*1.4//1, wood2.Y, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/gold_bullion.png')
crystal_purified = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*1.4//1, wood2.Y+wood2.HEIGHT+settings["SCREEN_HEIGHT"]//40, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/crystal.png')
stone_purified = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9//1, crystal_purified.Y, settings['SCREEN_WIDTH']//30, settings['SCREEN_WIDTH']//30, 'images/resources/stone.png')

exp_img = Graphic_elements(x=settings['SCREEN_WIDTH']//1.23,y=settings['SCREEN_HEIGHT']//1.7,width=settings['SCREEN_WIDTH']//50,height=settings['SCREEN_HEIGHT']//28.125,path='images/exp.png')
exp_img.X =  exp_img.start_x+(len(str(dict_arguments['characteristic_dict']['exp']))-1)*step_exp_text
mana_img.X = mana_img.start_x+(len(str(dict_arguments['characteristic_dict']['mana']))-1)*step_exp_text
button_change = Graphic_elements(x=settings['SCREEN_WIDTH']//2.43,y=settings['SCREEN_HEIGHT']//1.69,width=settings['SCREEN_WIDTH']//12.8*2,height=settings['SCREEN_HEIGHT']//14.4*2,path='images/button_change_b.png')

button_to_hero = Graphic_elements( settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9//1 +settings['SCREEN_WIDTH']//13.5,SCREEN_CELL_W*4.7,settings['SCREEN_WIDTH']//15,settings['SCREEN_WIDTH']//30,'images/game_interface/to_hero.png')
button_pause = Graphic_elements( settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9//1 +settings['SCREEN_WIDTH']//13.5,SCREEN_CELL_W*4.7 + settings['SCREEN_WIDTH']//30,settings['SCREEN_WIDTH']//15,settings['SCREEN_WIDTH']//30,'images/game_interface/pause.png')
button_end_move = Graphic_elements(settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//7.6, settings['SCREEN_HEIGHT']-settings['SCREEN_HEIGHT']//11, settings['SCREEN_WIDTH']//9,settings['SCREEN_HEIGHT']//20 , 'images/game_interface/end_moves.png')
button_menu_hero_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2,SCREEN_CELL_H,'images/menu_hero_back_y.png')
button_city_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2,SCREEN_CELL_H,'images/menu_hero_back_y.png')
button_camp_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2,SCREEN_CELL_H,'images/menu_hero_back_y.png')
button_altar_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2,SCREEN_CELL_H,'images/menu_hero_back_y.png')
button_castle_back = Graphic_elements(0,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2,SCREEN_CELL_H,'images/menu_hero_back_y.png')
button_market_back = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//12.8,y=0,width=SCREEN_CELL_W*2,height=SCREEN_CELL_H,path='images/menu_hero_back_b.png')
button_new_game = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'black','Новая игра',settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//24)
button_play = Font( 'images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'DimGrey','Продолжить игру',settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//24*4)
button_help = Font( 'images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'black','Помощь',settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//24*8)
button_set = Font( 'images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'black','Настройки',settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//24*12)
button_exit = Font( 'images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'black','Выйти',settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//24*16)
button_menu_end = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//19,'black','Меню',settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//19*2,settings['SCREEN_HEIGHT']-settings['SCREEN_WIDTH']//19)
if dict_arguments['civ_selected'] != None:
    button_play.path = 'images/menu/play_b.png'
button_hire = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//12.8,y=settings['SCREEN_HEIGHT']//2+settings['SCREEN_HEIGHT']//4,width=settings['SCREEN_WIDTH']//12.8*2,height=settings['SCREEN_HEIGHT']//14.4*2,path='images/camp_hire_b.png')
button_change_card = Graphic_elements(x=settings['SCREEN_WIDTH']//2.48,y=settings['SCREEN_HEIGHT']-settings['SCREEN_HEIGHT']//14.4*2.5,width=settings['SCREEN_WIDTH']//12.8*2,height=settings['SCREEN_HEIGHT']//14.4*2,path='images/button_change_b.png')
button_build = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//12.8*1.5,y=settings['SCREEN_HEIGHT']-SCREEN_CELL_H*2,width=settings['SCREEN_WIDTH']//12.8*3,height=settings['SCREEN_HEIGHT']//14.4*2,path='images/button_build_b.png')
button_continue = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'white','Продолжить',settings['SCREEN_WIDTH']//2.5-SCREEN_CELL_W,settings['SCREEN_HEIGHT']//3-SCREEN_CELL_H)
button_menu = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'white','Выйти в меню',settings['SCREEN_WIDTH']//2.5-SCREEN_CELL_W*1.5,settings['SCREEN_HEIGHT']//3+SCREEN_CELL_H)
button_quit = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'white','Выйти из игры',settings['SCREEN_WIDTH']//2.5-SCREEN_CELL_W*1.5,settings['SCREEN_HEIGHT']//3+SCREEN_CELL_H*3)
button_display_size = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Разрешение:',settings['SCREEN_WIDTH']//14.2,settings['SCREEN_HEIGHT']//8)
list_buttons_display_size =[
                Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','1280x720',button_display_size.font_x,button_display_size.font_y+settings['SCREEN_HEIGHT']//8),
                Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','1600x920',button_display_size.font_x+settings['SCREEN_WIDTH']//14.2*2,button_display_size.font_y+settings['SCREEN_HEIGHT']//8),
                Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','1920x1080',button_display_size.font_x+settings['SCREEN_WIDTH']//14.2*4,button_display_size.font_y+settings['SCREEN_HEIGHT']//8),
]
text_choose_civ = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black',' Выберите;цивилизацию',SCREEN_CELL_W*2,SCREEN_CELL_H//2,index=2)
lava_icon = Graphic_elements(x=SCREEN_CELL_W,y=SCREEN_CELL_W*3,width=SCREEN_CELL_W*2,height=SCREEN_CELL_H*2,path='images/lava_icon.png')
lava_text = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','Огненная',SCREEN_CELL_W,SCREEN_CELL_H*3.3+lava_icon.HEIGHT)
ice_icon = Graphic_elements(x=SCREEN_CELL_W*4,y=SCREEN_CELL_W*3,width=SCREEN_CELL_W*2,height=SCREEN_CELL_H*2,path='images/snow_icon.png')
ice_text = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','Ледяная',SCREEN_CELL_W*4,SCREEN_CELL_H*3.3+ice_icon.HEIGHT)
earth_icon = Graphic_elements(x=SCREEN_CELL_W*7,y=SCREEN_CELL_W*3,width=SCREEN_CELL_W*2,height=SCREEN_CELL_H*2,path='images/earth_icon.png')
earth_text = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','Наземная',SCREEN_CELL_W*7,SCREEN_CELL_H*3.3+earth_icon.HEIGHT)
scene_choose_civ = Graphic_elements(x=0,y=0,width=settings['SCREEN_WIDTH'],height=settings['SCREEN_HEIGHT'],path='images/book.png')
list_icon_civ = [lava_icon,earth_icon,ice_icon]
list_text_civ = [lava_text,ice_text,earth_text]
button_civ_choose = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Выбрать',SCREEN_CELL_W*3.5,settings['SCREEN_HEIGHT']//2+SCREEN_CELL_H*2)
for obj in list_buttons_display_size:
    width = settings_display['SCREEN_WIDTH']
    height = settings_display['SCREEN_HEIGHT']
    obj_width = obj.font_content.split('x')[0]
    obj_height = obj.font_content.split('x')[1]
    if (int(obj_width) == width and int(obj_height) == height):
        obj.font_color = 'red'
        break
button_display_fullsize = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Полноэкранный режим:',settings['SCREEN_WIDTH']//14.2,settings['SCREEN_HEIGHT']//8*4)
list_button_display_fullsize = [
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Да',settings['SCREEN_WIDTH']//14.2*2,settings['SCREEN_HEIGHT']//8*5),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Нет',settings['SCREEN_WIDTH']//14.2*4,settings['SCREEN_HEIGHT']//8*5)
]
if settings_display['FULLSCREEN']:
    list_button_display_fullsize[0].font_color = 'red'
else:
    list_button_display_fullsize[1].font_color = 'red'
button_volume_sound = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Громкость звуков:',settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//8)
rect_volume_sound = Rect(settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//8*2,settings['SCREEN_WIDTH']//1.09-settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//72)
mouse_volume_sound = Rect(settings_display['SOUNDS_VOLUME']*rect_volume_sound.width/100+rect_volume_sound.x,settings['SCREEN_HEIGHT']//8*1.9,settings['SCREEN_HEIGHT']//72,settings['SCREEN_HEIGHT']//72*3)
count_volume_sound = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black',str(settings_display['SOUNDS_VOLUME']),settings['SCREEN_WIDTH']//1.09,settings['SCREEN_HEIGHT']//8)
button_volume_music = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Громкость музыки:',settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//8*2.5)
rect_volume_music = Rect(settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//8*3.5,settings['SCREEN_WIDTH']//1.09-settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//72)
mouse_volume_music = Rect(settings_display['MUSIC_VOLUME']*rect_volume_sound.width/100+rect_volume_sound.x,settings['SCREEN_HEIGHT']//8*3.4,settings['SCREEN_HEIGHT']//72,settings['SCREEN_HEIGHT']//72*3)
count_volume_music = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black',str(settings_display['MUSIC_VOLUME']),settings['SCREEN_WIDTH']//1.09,settings['SCREEN_HEIGHT']//8*2.5)
button_auto_save = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Автосохранение:',settings['SCREEN_WIDTH']//1.75,settings['SCREEN_HEIGHT']//8*4)
list_button_auto_save = [
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Да',settings['SCREEN_WIDTH']//1.75+settings['SCREEN_WIDTH']//14.2*1,settings['SCREEN_HEIGHT']//8*5),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'black','Нет',settings['SCREEN_WIDTH']//1.75+settings['SCREEN_WIDTH']//14.2*3,settings['SCREEN_HEIGHT']//8*5)
] 
if settings_display['AUTOSAVE'] == 'True':
    list_button_auto_save[0].font_color = 'red'
else:
    list_button_auto_save[1].font_color = 'red'
button_save = Font('images/Font/pixel_font.ttf', settings['SCREEN_WIDTH']//38,'black','Сохранить',settings['SCREEN_WIDTH']//1.14,settings['SCREEN_HEIGHT']//1.34)
button_fight = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Сразится',dialog_book.X+SCREEN_CELL_W*1.5,dialog_book.Y+SCREEN_CELL_H*1.3)
button_offer = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Подкупить',dialog_book.X+SCREEN_CELL_W*1.5,dialog_book.Y+SCREEN_CELL_H*2.6)
button_threat= Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Угроза',dialog_book.X+SCREEN_CELL_W*1.5,dialog_book.Y+SCREEN_CELL_H*3.9)
button_leave = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Уйти',dialog_book.X+SCREEN_CELL_W*1.5,dialog_book.Y+SCREEN_CELL_H*5.2)
list_buttons_dialog = [button_fight,button_offer,button_threat,button_leave]
button_deal = Font('images/Font/pixel_font.ttf',SCREEN_CELL_W,'black','Сделка',dialog_book.X+SCREEN_CELL_W*1.5,dialog_book.Y+SCREEN_CELL_H*2.5)
list_buttons_dialog_potion = [button_leave,button_threat,button_deal]
#Текст для кнопки гарнизона
button_post_army = Graphic_elements(settings['SCREEN_WIDTH']-SCREEN_CELL_W*2.5,settings['SCREEN_HEIGHT']-SCREEN_CELL_H,SCREEN_CELL_W*2.5,SCREEN_CELL_H,'images/post_army_b.png')
button_continue_story = Graphic_elements(settings['SCREEN_WIDTH']-SCREEN_CELL_W*4,settings['SCREEN_HEIGHT']-SCREEN_CELL_H*2,SCREEN_CELL_W*4,SCREEN_CELL_H*2,path='images/button_continue_story_y.png')
list_buttons = [button_play,button_set,button_exit,button_new_game,button_help] 
#Текст
#Текст стоимость скиллов 
text_mana_cost_click = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'blue','  Нажмите;для покупки;за '+str(skill_cost)+' маны',settings['SCREEN_WIDTH']//320,settings['SCREEN_HEIGHT']//2.21,index=3)
#Текст нового уровня
text_new_lvl = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','Поздровляем! У вас новый уровень;Выберите улучшение способности;'+'Новый уровень - '+str(characteristic_dict['lvl']+1),settings['SCREEN_WIDTH']//2-SCREEN_CELL_W*4,settings['SCREEN_HEIGHT']//2-SCREEN_CELL_W*2,index=3)
#Текст опыта и уровня
text_lvl_hero = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'yellow','Текущий уровень - '+str(characteristic_dict['lvl'])+';До следующего уровня:',settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//2,index=2)
text_exp_hero = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'green',str(characteristic_dict['exp'])+'/'+str(max_exp_lvl),settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//1.7)
#Текст количества ходов
text_step_count = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//65,'white','Осталось шагов: '+str(player_lvl1.count_step),settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//6.8,settings['SCREEN_HEIGHT']-settings['SCREEN_HEIGHT']//7.5)
#Текст нового дня
text_new_day = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','           Новый день;    Статистика по ресурсам; ;Еды - 0 Золота - 0; ;Железа - 0 Кристаллов - 0; ;Камня - 0 Дерева - 0',frame_new_day.X+SCREEN_CELL_W,frame_new_day.Y+SCREEN_CELL_H,index=8)
#Текст сундука 
chest_text_gold =  Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red','   Нет места для артефакта;   Вы забираете золото',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10,index=2)
#Текст для показа сколько осталось до побега
text_notification_goblins = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','',frame_buildings.X+settings['SCREEN_WIDTH']//40,frame_buildings.Y + settings['SCREEN_HEIGHT']//19,index=2)
#
chest_text_choice = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','Выберите награду;       или',settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//9.5,settings['SCREEN_HEIGHT']//2-SCREEN_CELL_H*2,index=2)
#Текст рынка нет места для артефакта 
text_market_aritfact_no_slots =  Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//45,'red','Нет места для артефакта',frame_error.X+ frame_error.WIDTH//10,frame_error.Y + settings['SCREEN_HEIGHT']//10)
#Текст кол-во маны
text_mana = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'blue','Мана: '+str(characteristic_dict['mana']),settings['SCREEN_WIDTH']//1.34,settings['SCREEN_HEIGHT']//1.59)
#Текст для таверны
text_tavern = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red','Вы выиграли 20 золотых: ',frame_buildings.X+settings['SCREEN_WIDTH']//40,frame_buildings.Y + settings['SCREEN_HEIGHT']//19,index=3)
#Текст для зданий
text_next_week_buildings = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red','     Сейчас недоступно!;   Приходите через неделю',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12,index=2)
#Текст ошибки нехватка золота 
text_not_enough_gold = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red',' Не хватает золота!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12)
#Текст для цены артефакта
text_price_artifact = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','',button_change.X-settings['SCREEN_WIDTH']//30,button_change.Y - settings['SCREEN_WIDTH']//18.75)
#Текст ошибки заблокированого лагеря
text_blocked_camp = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','   Сейчас недоступно!; Приходите через неделю',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12,index=2)
#Текст ошибки нет места в инвентаре
text_not_inventory = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','Нет места в инвентаре!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12)
#Текст для ошибки заблокированой карты 
text_locked_card = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','Карта заблокирована!; Прокачайте уровень',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12,index=2)
text_bought_card = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//42,'red','Вы уже купили эту карту!; Приходите через неделю',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12,index=2)
#Текст стоимость карт
text_price_card = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','',button_hire.X-settings['SCREEN_WIDTH']//30,button_hire.Y - settings['SCREEN_HEIGHT']//18.75)
#Текст стоимости обмена карты в алтаре
text_change_card = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','',button_change_card.X+settings['SCREEN_WIDTH']//19*2,settings['SCREEN_HEIGHT'] - settings['SCREEN_HEIGHT']//18.75)
#Текст стоимости здания в замке
text_cost_buildings = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','',button_build.X-settings['SCREEN_WIDTH']//30,button_build.Y - settings['SCREEN_HEIGHT']//18.75)
#Текст лагерь наемников
text_camp = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','Лагерь наемников',settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//9.5,0)
#Текст для хижины колдуна
text_shack = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red',' Вы выпили зелье маны',frame_buildings.X,frame_buildings.Y + SCREEN_CELL_H)
#Текст для колодца маны
text_fountain_mana = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//45,'red','Вы выпили воду из колодца',frame_buildings.X,frame_buildings.Y + SCREEN_CELL_H)
#Текст для дерева знаний
text_fountain_exp = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//45,'red','Вы получили знания дерева',frame_buildings.X,frame_buildings.Y + SCREEN_CELL_H)
#Текст для ошибки недостаточно ресурсов
text_not_enough_resource = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','Не хватает ресурсов!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12)
#Текст для ошибки купленого здания
text_build_alredy_bought = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red',' Здание уже куплено!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12)
#Текст для ошибки нельзя купить здание
text_buy_previous_build = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//37,'red','Нельзя купить здание!;  Купите предыдущее!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12,index=2)
#Текст для подкупа противника
text_offer_enemy = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//48,'red','',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//19)
text_offer_yes = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//30,'red','Да',frame_error.X+SCREEN_CELL_W*2,frame_error.Y + settings['SCREEN_HEIGHT']//19*2)
text_offer_no = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//30,'red','Нет',frame_error.X+SCREEN_CELL_W*4,frame_error.Y + settings['SCREEN_HEIGHT']//19*2)
text_yes = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//30,'red','Да',frame_error.X+SCREEN_CELL_W*2,frame_error.Y + settings['SCREEN_HEIGHT']//19*3)
text_no = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//30,'red','Нет',frame_error.X+SCREEN_CELL_W*4,frame_error.Y + settings['SCREEN_HEIGHT']//19*3)
#Текст недостаточно карт
text_not_enough_cards = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red',' Не хватает карт!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//12)
#Текст для карт 
text_dialog_card = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','',dialog_book.X+dialog_book.WIDTH//2+settings['SCREEN_WIDTH']//35,dialog_book.Y+SCREEN_CELL_H,index=2)
#Текст для зелья
text_dialog_potion = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','',dialog_book.X+dialog_book.WIDTH//2+settings['SCREEN_WIDTH']//35,dialog_book.Y+settings['SCREEN_HEIGHT']//19+SCREEN_CELL_H)
#Текст для события
text_daily_event =  Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','',frame_notification.X+SCREEN_CELL_W,frame_notification.Y+SCREEN_CELL_H)
#Текст для сохранения
text_save = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//45,'red','  Настройки сохранены.;  Перезайдите в игру!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//19,index=2)
#Текст для ошибки выбора расы
text_error_choose_civ = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//35,'red','    Вы не выбрали;    цивилизацию!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//18,index=2)
#текст для ошибки что недостаточно ходов
text_error_not_enoug_step = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','Шаги за день потрачены',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//14)
#текст для ошибки что недостаточно ходов
text_skill_icon = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//40,'red','   Нужен уровень - 5',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//14)
#Текст для выбора способности 
text_hero_skill = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','        Поздровляем!;Вы познали великую магию!;Вы можете изучить способность!',settings['SCREEN_WIDTH']//2-SCREEN_CELL_W*4,settings['SCREEN_HEIGHT']//2-SCREEN_CELL_H*2,index=3)
#Текст для ошибки уже купленной способности
text_error_bought_skill = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//44,'red','Способность уже куплена!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10)
#Текст для закрытия после новой игры
text_new_game = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','Для начала игры;требуется перезайти!',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//19,index=2)
text_new_game_error = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'red','Вы действительно хоти-;те начать игру заного?',frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//19,index=2)
#Картинки иконок ресурсов
amount_food = Font('images/Font/pixel_font.ttf', int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',apple.X+apple.WIDTH+settings['SCREEN_WIDTH']//160,apple.Y)
amount_iron = Font('images/Font/pixel_font.ttf', int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',iron_bullion.X+iron_bullion.WIDTH+settings['SCREEN_WIDTH']//160,iron_bullion.Y)
amount_wood = Font('images/Font/pixel_font.ttf', int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',wood2.X+wood2.WIDTH+settings['SCREEN_WIDTH']//160,wood2.Y)
amount_gold = Font('images/Font/pixel_font.ttf', int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',gold_bullion.X+gold_bullion.WIDTH+settings['SCREEN_WIDTH']//160,gold_bullion.Y)
amount_crystal=Font('images/Font/pixel_font.ttf',int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',crystal_purified.X+crystal_purified.WIDTH+settings['SCREEN_WIDTH']//160,crystal_purified.Y)
amount_stone = Font('images/Font/pixel_font.ttf',int(apple.HEIGHT-settings['SCREEN_WIDTH']//85.3),'white','0',stone_purified.X+stone_purified.WIDTH+settings['SCREEN_WIDTH']//160,stone_purified.Y)
amount_money = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*1.4//1, SCREEN_CELL_W*6.7,SCREEN_CELL_W*1.5, SCREEN_CELL_H*1.5, 'images/resources/gold_bullion.png')
#Туман войны
fog_war = Graphic_elements(None,None,SCREEN_CELL_W, SCREEN_CELL_W,'images/fog_war.bmp')
#Интерфейс
interface_bg  = Graphic_elements(settings['SCREEN_WIDTH']-SCREEN_CELL_W*3,0,SCREEN_CELL_W*3,settings['SCREEN_HEIGHT'],'images/game_interface/sheet.png')
frame = Graphic_elements(settings['SCREEN_WIDTH'] - SCREEN_CELL_W*2.9,  SCREEN_CELL_W*4.7, settings['SCREEN_WIDTH']//15, settings['SCREEN_HEIGHT']//7.03, 'images/game_interface/ramka.png')
frame_mini_map = Graphic_elements(settings['SCREEN_WIDTH']//1.175,  Y_FRAME_MM-settings['SCREEN_HEIGHT']//100 , settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1*(LENGTH_MAP_LVL1+2), settings['SCREEN_WIDTH']//6.9//LENGTH_MAP_LVL1*(LENGTH_MAP_LVL1+2), 'images/game_interface/ramka.png')
list_interface_button = [button_to_hero,button_pause,button_end_move]
menu_hero_icon_eliot = Graphic_elements(x=settings['SCREEN_WIDTH']//1.64,y=settings['SCREEN_HEIGHT']//2.08,width=settings['SCREEN_WIDTH']//8.25,height=settings['SCREEN_HEIGHT']//5.1,path='images/game_interface/elliot_img.png')
text_date = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'white','День: '+str(characteristic_dict['day'])+';Неделя: '+str(characteristic_dict['week']),X_FRAME_MM,frame_mini_map.Y+frame_mini_map.HEIGHT,index=2)
#Описание чего то
desc = Graphic_elements(settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//4,settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//4,settings['SCREEN_WIDTH']//2,settings['SCREEN_HEIGHT']//2,path=None)
desc_artifact = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//6,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_HEIGHT']/1.4,path=None)
desc_base_skill = Graphic_elements(x=SCREEN_CELL_W,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_HEIGHT']/1.4,path=None)
desc_skill_hero = Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//6,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_HEIGHT']//2,height=settings['SCREEN_HEIGHT']/1.43,path=None)
desc_buildings_city = Graphic_elements(settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//4,settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//4,settings['SCREEN_WIDTH']//2,settings['SCREEN_HEIGHT']//2,path=None)
#Рамка выбраного чего то
market_selected = Graphic_elements(x=0,y=0,width=0,height=0,path='images/market_selected.png')
camp_selected = Graphic_elements(x=0,y=0,width=0,height=0,path='images/market_selected.png')
altar_selected = Graphic_elements(x=0,y=0,width=0,height=0,path='images/market_selected.png')
castle_selected = Graphic_elements(x=0,y=0,width=0,height=0,path='images/market_selected.png')
civ_selected = Graphic_elements(x=0,y=0,width=0,height=0,path='images/market_selected.png')
#Cундук
chest = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W,path='images/chest/chest.png')
chest_open = Graphic_elements(settings['SCREEN_WIDTH']//2-SCREEN_CELL_W*3,settings['SCREEN_HEIGHT']//2-SCREEN_CELL_H*3,SCREEN_CELL_W*6,SCREEN_CELL_W*6,path='images/chest/chest_open.png')
#Сцены
book = Graphic_elements(0, 0, settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'], 'images/book.png')
menu_hero = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/hero_menuclose.bmp')
background_market = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/background_market.bmp')
city_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/city.bmp')
scene_camp = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/scene_camp.bmp')
scene_altar = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/altar_scene.png')
scene_castle = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/castle_scene.png')
scene_post_army  = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/post_army.png')
story1_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story1_scene.png')
story2_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story2_scene.png')
story3_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story3_scene.png')
story4_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story4_scene.png')
story5_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story5_scene.png')
story6_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story6_scene.png')
story7_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story7_scene.png')
story8_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story8_scene.png')
story9_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story9_scene.png')
story10_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story10_scene.png')
story11_scene = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/story/story11_scene.png')
#Звуки
#Звук открытия книги
sound_book = Sounds('sounds/book_opened.wav', settings['SOUNDS_VOLUME'])
#Звуки ресурсов
recourse_sounds = [Sounds('sounds/res1.wav',settings['SOUNDS_VOLUME']),Sounds('sounds/res2.wav',settings['SOUNDS_VOLUME']),Sounds('sounds/res3.wav',settings['SOUNDS_VOLUME'])]
#Звук нажатия
click_sound = Sounds('sounds/click.wav',settings['SOUNDS_VOLUME']/2)
#Звук нажатия  в меню героя
# click_menu_hero_sound = Sounds('sounds/click_menu_hero.wav',settings['SOUNDS_VOLUME']/2)
#Звук события
event_sound = Sounds('sounds/event.wav',settings['SOUNDS_VOLUME'])
#Звук нового дня
new_day_sound = Sounds('sounds/new_day.wav',settings['SOUNDS_VOLUME'])
#Музыка
#Фоновая музыка
background_music = Sounds('sounds/background_music.wav',settings['MUSIC_VOLUME'])
background_music.play_sound(index=-1)
#Фоновая музыка для карточного боя
background_music_card_game = Sounds('sounds/game_music.wav',settings['MUSIC_VOLUME'])
brightless_pause = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],path='images/brightless.png')
flashlight_icon = Graphic_elements(frame_notification.X+SCREEN_CELL_W,frame_notification.Y+settings['SCREEN_HEIGHT']//19*5,SCREEN_CELL_W*2,SCREEN_CELL_H*2,'images/skills_icons/flash_icon.png',name='flash_light')
healskill_Icon = Graphic_elements(frame_notification.X+SCREEN_CELL_W*4,frame_notification.Y+settings['SCREEN_HEIGHT']//19*5,SCREEN_CELL_W*2,SCREEN_CELL_H*2,'images/skills_icons/heal_icon.png',name='heal')
damageskill_Icon = Graphic_elements(frame_notification.X+SCREEN_CELL_W*7,frame_notification.Y+settings['SCREEN_HEIGHT']//19*5,SCREEN_CELL_W*2,SCREEN_CELL_H*2,'images/skills_icons/dmg_icon.png',name='damage')
list_card_camp = [
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//20*8,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//3.51,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=  dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[0]]),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//20*4.5,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//3.51,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[1]]),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//20,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//3.51,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=    dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[2]]),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2+settings['SCREEN_WIDTH']//20*2.5,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//3.51,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[3]]),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2+settings['SCREEN_WIDTH']//20*6,y=settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//3.51,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=  dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[4]]),
]
list_card_altar = [
                    Graphic_elements(x=settings['SCREEN_WIDTH']//3.7,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path= None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2.56,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.95,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.58,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.32,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.14,y=settings['SCREEN_HEIGHT']//6,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    #Резервные карты
                    Graphic_elements(x=settings['SCREEN_WIDTH']//3.71,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//2.56,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.95,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.58,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.32,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
                    Graphic_elements(x=settings['SCREEN_WIDTH']//1.14,y=settings['SCREEN_HEIGHT']//1.92,width=settings['SCREEN_WIDTH']//10,height=settings['SCREEN_HEIGHT']//3.51,path=None),
]
list_all_artifact = [   
    #Слоты героя 
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//2.18,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_HEIGHT']//20,path=dict_arguments['dict_path_artifact']['helmet'], name='helmet'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//1.71,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_HEIGHT']//20,path=dict_arguments['dict_path_artifact']['chest'], name='chest'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.15,settings['SCREEN_HEIGHT']//1.09,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_HEIGHT']//20,path=dict_arguments['dict_path_artifact']['boots'], name='boots'),
    Graphic_elements(settings['SCREEN_WIDTH']//2.43,settings['SCREEN_HEIGHT']//1.45,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_HEIGHT']//20,path=dict_arguments['dict_path_artifact']['sword'], name='sword'),
    Graphic_elements(settings['SCREEN_WIDTH']//1.92,settings['SCREEN_HEIGHT']//1.45,settings['SCREEN_WIDTH']//36.57,settings['SCREEN_HEIGHT']//20,path=dict_arguments['dict_path_artifact']['shield'], name='shield'),
    #Резевные слоты
    Graphic_elements(settings['SCREEN_WIDTH']//1.39,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,dict_arguments['dict_path_artifact']['reserv1'], name=None),
    Graphic_elements(settings['SCREEN_WIDTH']//1.39+settings['SCREEN_WIDTH']//10.49,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,dict_arguments['dict_path_artifact']['reserv2'], name=None),
    Graphic_elements(settings['SCREEN_WIDTH']//1.39+2*settings['SCREEN_WIDTH']//10.49,settings['SCREEN_HEIGHT']//1.18,settings['SCREEN_WIDTH']//12.8,settings['SCREEN_HEIGHT']//7.57,dict_arguments['dict_path_artifact']['reserv3'], name=None)
]
#Базовые скиллы
list_slots_base_skills = [
    Graphic_elements(settings['SCREEN_WIDTH']//51.2,settings['SCREEN_HEIGHT']//23.2,settings['SCREEN_WIDTH']//9.8,settings['SCREEN_HEIGHT']//5.6,path='images/skills/skill_diplomacy.png'),
    Graphic_elements(settings['SCREEN_WIDTH']//7.15,settings['SCREEN_HEIGHT']//23.2,settings['SCREEN_WIDTH']//9.8,settings['SCREEN_HEIGHT']//5.6,path='images/skills/skill_domesticpolitics.png'),
    Graphic_elements(settings['SCREEN_WIDTH']//3.85,settings['SCREEN_HEIGHT']//23.2,settings['SCREEN_WIDTH']//9.8,settings['SCREEN_HEIGHT']//5.6,path='images/skills/skill_fight.png')
]
list_choice_base_skill = [
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-SCREEN_CELL_W-SCREEN_CELL_W*3,frame_notification.Y+SCREEN_CELL_W*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_HEIGHT']//4.61,path='images/skills/skill_diplomacy.png'),
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-SCREEN_CELL_W,frame_notification.Y+SCREEN_CELL_W*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_HEIGHT']//4.61,path='images/skills/skill_domesticpolitics.png'),
    Graphic_elements(frame_notification.X+frame_notification.WIDTH//2-SCREEN_CELL_W+SCREEN_CELL_W*3,frame_notification.Y+SCREEN_CELL_W*3,settings['SCREEN_WIDTH']//9.84,settings['SCREEN_HEIGHT']//4.61,path='images/skills/skill_fight.png')
]
list_text_lvl_base_skills = [
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_diplomacy']),settings['SCREEN_WIDTH']//51.2,0),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_domesticpolitics']),settings['SCREEN_WIDTH']//7.11,0),
    Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//51,'red','Уровень: '+str(characteristic_dict['lvl_skill_fight']),settings['SCREEN_WIDTH']//3.87,0)
]
list_slots_skills_hero = [
    Graphic_elements(x=settings['SCREEN_WIDTH']//12.69,y=settings['SCREEN_HEIGHT']//1.63,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//10.5,path=dict_arguments['dict_path_skills']['skill_earth_blessing']),
    Graphic_elements(x=settings['SCREEN_WIDTH']//5.71,y=settings['SCREEN_HEIGHT']//1.63,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//10.5,path=dict_arguments['dict_path_skills']['skill_lumberjack']),
    Graphic_elements(x=settings['SCREEN_WIDTH']//12.69,y=settings['SCREEN_HEIGHT']//1.35,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//10.5,path=dict_arguments['dict_path_skills']['skill_forest_path']),
    Graphic_elements(x=settings['SCREEN_WIDTH']//5.71,y=settings['SCREEN_HEIGHT']//1.35,width=settings['SCREEN_WIDTH']//18.28,height=settings['SCREEN_HEIGHT']//10.5,path=dict_arguments['dict_path_skills']['skill_idol_people']),
    
    Graphic_elements(x=settings['SCREEN_WIDTH']//8.25,y=settings['SCREEN_HEIGHT']//2.23,width=settings['SCREEN_WIDTH']//13.9,height=settings['SCREEN_HEIGHT']//8,path=dict_arguments['dict_path_skills']['skill_leader'])
    ]
artifact_chest = Graphic_elements(0,0,0,0,dict_arguments['path_artifact_chest'])
dict_price_artifact = {
    'boots_fire':randint(20,30),
    'boots_hero':randint(30,35),
    'boots_ice':randint(20,30),
    'chest_fire':randint(30,35),
    'chest_ice':randint(10,20),
    'helmet_ice':randint(20,30),
    'shield_ice':randint(20,30),
    'sword_ice':randint(20,30),
    'chest_hero':randint(10,20),
    'helmet_hero':randint(10,20),
    'shield_hero':randint(20,30),
    'sword_hero':randint(25,35),
    'shield_fire':randint(15,20),
    'sword_fire':randint(25,35),
    'helmet_fire':randint(10,20)
}
dict_arguments['dict_price_artifact'] = dict_price_artifact
dict_price_resource = {
    'wood':'1_4',
    'iron_bullion':'1_2',
    'stone':'1_3',
    'crystal':'2_1',
    'food':'1_5',
}
dict_arguments['dict_price_resource'] = dict_price_resource
list_buildings_castle = [
                            Graphic_elements(x=settings['SCREEN_WIDTH']//49.2,y=settings['SCREEN_HEIGHT']//2.2,width=settings['SCREEN_WIDTH']//8.1,height=settings['SCREEN_HEIGHT']//4.61,path=None),
                            Graphic_elements(x=settings['SCREEN_WIDTH']//49.2,y=settings['SCREEN_HEIGHT']//2.2,width=settings['SCREEN_WIDTH']//8.1,height=settings['SCREEN_HEIGHT']//4.61,path=None),
                            Graphic_elements(x=settings['SCREEN_WIDTH']//49.2,y=settings['SCREEN_HEIGHT']//2.2,width=settings['SCREEN_WIDTH']//8.1,height=settings['SCREEN_HEIGHT']//4.61,path=None),
                            Graphic_elements(x=settings['SCREEN_WIDTH']//49.2,y=settings['SCREEN_HEIGHT']//2.2,width=settings['SCREEN_WIDTH']//8.1,height=settings['SCREEN_HEIGHT']//4.61,path=None),
                            Graphic_elements(x=settings['SCREEN_WIDTH']//49.2,y=settings['SCREEN_HEIGHT']//2.2,width=settings['SCREEN_WIDTH']//8.1,height=settings['SCREEN_HEIGHT']//4.61,path=None),
]
for i in range(len(list_buildings_castle)):
    list_buildings_castle[i].NAME = list(dict_arguments['dict_bought_city'].keys())[i]
    list_buildings_castle[i].X += i*settings['SCREEN_WIDTH']//4.78
    if not dict_arguments['dict_bought_city'][list_buildings_castle[i].NAME]:
        list_buildings_castle[i].path = 'images\city\castle\\'+list(dict_arguments['dict_bought_city'].keys())[i]+'_locked.png'
    else:
        list_buildings_castle[i].path = 'images\city\castle\\'+list(dict_arguments['dict_bought_city'].keys())[i]+'.png'
    
    list_buildings_castle[i].image_load()
list_slots_market_hero = [
    #Артефакты 
    Graphic_elements(x=settings['SCREEN_WIDTH']//36.57-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path=None),
    Graphic_elements(x=settings['SCREEN_WIDTH']//7.52-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path=None),
    Graphic_elements(x=settings['SCREEN_WIDTH']//4.19-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path=None),
    #Ресурсы сверху
    Graphic_elements(x=settings['SCREEN_WIDTH']//42.6-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/food.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//7.75-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/crystal.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//4.26-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/iron_bullion.png'),
    #Ресурсы снизу
    Graphic_elements(x=settings['SCREEN_WIDTH']//12.8-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.2265,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/stone.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//5.49-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.2265,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/wood.png'),
]
list_slots_market = [
    #Артефакты 
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.46-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path='images/artifacts/'+dict_arguments['list_choice_slots_market'][0]+'.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.27-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path='images/artifacts/'+dict_arguments['list_choice_slots_market'][1]+'.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.12-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//3.13,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='artifact',path='images/artifacts/'+dict_arguments['list_choice_slots_market'][2]+'.png'),
    #Ресурсы сверху
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.46-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/food.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.26-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/crystal.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.11-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.57,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/iron_bullion.png'),
    #Ресурсы снизу
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.35-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.22,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/stone.png'),
    Graphic_elements(x=settings['SCREEN_WIDTH']//1.18-settings['SCREEN_WIDTH']//1280,y=settings['SCREEN_HEIGHT']//1.22,width=settings['SCREEN_WIDTH']//12.3,height=settings['SCREEN_HEIGHT']//7,name='resource',path='images/resources/wood.png'),
]
amount_gold_market = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'red','0',settings['SCREEN_WIDTH']//1.8, settings['SCREEN_HEIGHT']//1.07)
list_cards_post_army = []
for i in range(6):
    card = Graphic_elements(x=settings['SCREEN_WIDTH']//37.64+i*settings['SCREEN_WIDTH']//5.75,y=settings['SCREEN_HEIGHT']//5.07,width=settings['SCREEN_WIDTH']//13.06,height=settings['SCREEN_HEIGHT']//4,path=None)
    list_cards_post_army.append(card)
for i in range(6):
    card = Graphic_elements(x=settings['SCREEN_WIDTH']//37.64+i*settings['SCREEN_WIDTH']//5.75,y=settings['SCREEN_HEIGHT']//1.68,width=settings['SCREEN_WIDTH']//13.06,height=settings['SCREEN_HEIGHT']//4,path=None)
    list_cards_post_army.append(card)
list_artifact_graphic_elements = list()
for i in dict_arguments['list_matrix_artifact']:
    artifact = Graphic_elements(0,0,SCREEN_CELL_W*1.5,SCREEN_CELL_H*1.5,path='images/artifacts/'+i+'.png')
    list_artifact_graphic_elements.append(artifact)
#Карты на матрице
crossbowman = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/арбалетчик.png',name='А')#А
druid = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/друид.png',name='Д')#Д
bard = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/бард.png',name='Б')#Б
giant = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/гигант.png',name='Г')#Г
golem = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/голем.png',name='Е')#Е
centaur = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/кентавр.png',name='К')#К
klaus = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/клаус.png',name='М')#М
ludorn = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/лудорн.png',name='Л')#Л
ork = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/орк.png',name='О')#О
bomb_man = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/подрывник.png',name='П')#П
roggy = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/рогги.png',name='Р')#Р
surtur = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/суртур.png',name='С')#С
yamy = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/ями.png',name='Я')#Я
dvorf = Graphic_elements(0,0,SCREEN_CELL_W,SCREEN_CELL_W*1.5,path='images/cards/Heroes/дворф.png',name='В')#В
list_card_matrix = [crossbowman,druid,bard,giant,golem,centaur,klaus,ludorn,ork,bomb_man,roggy,surtur,yamy,dvorf]
#Картинка зеленого флага
flag_green = Graphic_elements(0, 0, SCREEN_CELL_W, SCREEN_CELL_W, 'images/flags/flag_g.png')
dict_text_credits = {
                    'Дизайнеры:':['Срибный Дима','Устич Паша', 'Мальцева Лиза', 'Ильченко Ксюша', 'Алексеенко Егор', 'Гайдар Паша', 'Ткаченко Прохор'],
                    'Разработчики:':['Семёнов Рома','Дмитрий Ларин','Кикот Сергей','Скрипник Николай'],
                    'Сюжет:':['Дмитрий Ларин','Илья Подрез','Смирнов Тимофей','Глеб Фурсенко']
}
skill_icon = Graphic_elements(settings['SCREEN_WIDTH']//1.099,settings['SCREEN_HEIGHT']//1.692,settings['SCREEN_WIDTH']//12.6,settings['SCREEN_HEIGHT']//7.2,dict_arguments['hero_skill_path'])
if dict_arguments['hero_skill_path'] != None:
    skill_icon.path = dict_arguments['hero_skill_path']
    menu_hero.path = 'images/hero_menu.bmp'
    menu_hero.image_load()
text_credits = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black','За игру отвечали:',settings['SCREEN_WIDTH']//2.5,0)
list_text_credits_object = list()
x_text = SCREEN_CELL_W*2
y_text = SCREEN_CELL_H
for key in dict_text_credits.keys():
    text = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black',key,x_text,y_text,font_name=key)
    list_text_credits_object.append(text)
    y_text += SCREEN_CELL_H
    for name in dict_text_credits[key]:
        text = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//38,'black',name,x_text,y_text,font_name=key)
        list_text_credits_object.append(text)
        y_text += SCREEN_CELL_H
    y_text=SCREEN_CELL_H
    x_text += settings['SCREEN_WIDTH']//3-settings['SCREEN_WIDTH']//38
bg_story = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/bg.bmp')
#Карточный бой
#Создаем объект фона
bg = Graphic_elements(0,0,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],'images/bg1.png')
#Создаем объекты карт
card_pl_1 = Cards(settings['SCREEN_WIDTH']//12*3.2,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_1')
card_pl_2 = Cards(settings['SCREEN_WIDTH']//12*4.6,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_2')
card_pl_3 = Cards(settings['SCREEN_WIDTH']//12*6,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_3')
card_pl_4 = Cards(settings['SCREEN_WIDTH']//12*7.4,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_4')
card_pl_5 = Cards(settings['SCREEN_WIDTH']//12*8.9,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_5')
card_pl_6 = Cards(settings['SCREEN_WIDTH']//12*10.4,settings['SCREEN_HEIGHT']//1.5, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='pl_6')
card_en_1 = Cards(settings['SCREEN_WIDTH']//12*3.2,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_1')
card_en_2 = Cards(settings['SCREEN_WIDTH']//12*4.6,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_2')
card_en_3 = Cards(settings['SCREEN_WIDTH']//12*6,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_3')
card_en_4 = Cards(settings['SCREEN_WIDTH']//12*7.4,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_4')
card_en_5 = Cards(settings['SCREEN_WIDTH']//12*8.9,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_5')
card_en_6 = Cards(settings['SCREEN_WIDTH']//12*10.4,settings['SCREEN_HEIGHT']//20, settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//3.28,path = None,hp = None,damage = None,desc_path = None,name='en_6')
#Списки объектов карт
list_objects_cards_pl = [card_pl_1,card_pl_2,card_pl_3,card_pl_4,card_pl_5,card_pl_6]
list_objects_cards_en = [card_en_1,card_en_2,card_en_3,card_en_4,card_en_5,card_en_6]
# Картинка взрыва для способности подрывника
img_boom = Graphic_elements_cards(None,None,settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//12,'images/boom.png')
#Картинка иссцеляющего облака
heal_cloud = Graphic_elements_cards(0,0,settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//12,'images/hill_cloud.png')
#Картинка "Оглушение" 
stun_img = Graphic_elements_cards(0,0,settings['SCREEN_WIDTH']//9, settings['SCREEN_HEIGHT']//9,'images/stun.png')
#Картинка меча
dmg_img = Graphic_elements_cards(0,0,settings['SCREEN_WIDTH']//12, settings['SCREEN_HEIGHT']//12,'images/dmg_symb2.png')
#Иконка способностей
flash_light_icon = Graphic_elements_cards(settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//1.3,settings['SCREEN_WIDTH']//15,settings['SCREEN_HEIGHT']//7.03,'images/skills_icons/flash_icon.png', name='flash_light')
heal_skill_Icon = Graphic_elements_cards(settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//1.3,settings['SCREEN_WIDTH']//15,settings['SCREEN_HEIGHT']//7.03,'images/skills_icons/heal_icon.png', name='heal')
damage_skill_Icon = Graphic_elements_cards(settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//1.3,settings['SCREEN_WIDTH']//15,settings['SCREEN_HEIGHT']//7.03,'images/skills_icons/dmg_icon.png', name='damage')
dict_skills = {
                'flash_light':flash_light_icon,
                'heal':heal_skill_Icon,
                'damage':damage_skill_Icon,
                }
hero_skill = dict_skills['damage']
hero_skill.path = dict_arguments['hero_skill_path']
hero_skill.NAME = dict_arguments['hero_skill_name']
#Описание скилла героя 
desc_skill = Graphic_elements_cards(settings['SCREEN_WIDTH']//2.5,settings['SCREEN_HEIGHT']//4,settings['SCREEN_WIDTH']//4,settings['SCREEN_HEIGHT']//2,None)

#Картинка молнии
flash_light_image = Graphic_elements_cards(0,0,settings['SCREEN_WIDTH']//12,settings['SCREEN_HEIGHT']//5.66,None)
# Рамка для ошибки
frame_error = Graphic_elements_cards(settings['SCREEN_WIDTH']//2 - settings['SCREEN_WIDTH']//6, settings['SCREEN_HEIGHT']//2 - settings['SCREEN_HEIGHT']//8, settings['SCREEN_WIDTH']//3, settings['SCREEN_HEIGHT']//4, 'images/error_sheet.png')
# Объект текста ошибки
error_text_obj = Text_cardgame.Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//50,'red',None,frame_error.X+settings['SCREEN_WIDTH']//40,frame_error.Y + settings['SCREEN_HEIGHT']//10)

# Подгружаем звуки для игры
sound_hit = Sounds('sounds/sword.wav',settings['SOUNDS_VOLUME'])
sound_heal = Sounds('sounds/healsound.wav',settings['SOUNDS_VOLUME'])
sound_flashlight = Sounds('sounds/flashlight.wav',settings['SOUNDS_VOLUME'])
sound_explosion = Sounds('sounds/explosion.wav',settings['SOUNDS_VOLUME'])
sound_paper = Sounds('sounds/book_opened.wav',settings['SOUNDS_VOLUME'])

# Объект карты для отображения потерь в сцене результата боя
card_for_result_screen =Graphic_elements_cards(None,None,settings['SCREEN_WIDTH']//12,settings['SCREEN_HEIGHT']//3.28124,None)

#Иконки ресурсов для сцены результата боя
gold_icon = Graphic_elements_cards(settings['SCREEN_WIDTH']//12*3.2,settings['SCREEN_HEIGHT']//1.15,settings['SCREEN_WIDTH']//15,settings['SCREEN_HEIGHT']//9.375,'images/gold_bullion.png')
exp_icon = Graphic_elements_cards(settings['SCREEN_WIDTH']//12*6,settings['SCREEN_HEIGHT']//1.15,settings['SCREEN_WIDTH']//20,settings['SCREEN_HEIGHT']//9.375,'images/exp.png')
# Текст для кол-ва ресурсов для сцены результата боя
trophy_recourse_text = Text_cardgame.Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//20,'white',None,None,None)
# Кнопка завершения боя
button_end_fight = Graphic_elements_cards(settings['SCREEN_WIDTH']//12*10,settings['SCREEN_HEIGHT']//1.2, settings['SCREEN_WIDTH']//8, settings['SCREEN_WIDTH']//15,'images/buttons/end_fight_y.png')
#Экраны для победы и поражения
bg_win = Graphic_elements_cards(0,0, settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'],'images/bg_win.png')
bg_lose = Graphic_elements_cards(0,0, settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'],'images/bg_lose.png')

music_win = Sounds('sounds/music_win.wav',settings['MUSIC_VOLUME'])
music_lose = Sounds('sounds/music_lose.wav',settings['MUSIC_VOLUME'])

list_cards_on_table_pl = []
# Объект текста хода
text_move = Text_cardgame.Font('images/Font/pixel_font.ttf',60,'white','Твой ход!',settings['SCREEN_WIDTH']//2.5, settings['SCREEN_HEIGHT']//2.3)


