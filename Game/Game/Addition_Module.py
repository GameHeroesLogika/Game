import pygame
from graphic_elements import Graphic_elements
from random import randint,choice
import json

def civ_change(dict_arguments,civ,city_scene,castle,city,card,list_card_camp):
    if civ != None:
        city_scene.path = 'images/'+civ+'/bg_city.bmp'
        castle.path = 'images/'+civ+'/castle.png'  
        city.path = 'images/'+civ+'/castle.png'  
    city_scene.image_load()
    castle.image_load()
    city.image_load()
    for i in range(len(list(dict_arguments['dict_card_path_camp'].keys()))-1):
        list_card_camp[i].path = dict_arguments['dict_card_path_camp'][list(dict_arguments['dict_card_path_camp'].keys())[i]]
    for i in range(len(list(dict_arguments['dict_card_name_camp'].keys()))-1):
        list_card_camp[i].NAME = dict_arguments['dict_card_name_camp'][list(dict_arguments['dict_card_name_camp'].keys())[i]]
def check_mouse_cor(sprite,mouse_cor):
    if mouse_cor[0] > sprite.X and mouse_cor[0] < sprite.X + sprite.WIDTH and mouse_cor[1] > sprite.Y and mouse_cor[1] < sprite.Y + sprite.HEIGHT:
        return True
def check_mouse_cor_font(sprite,mouse_cor):
    width = len(sprite.font_content)*sprite.font_size//2
    height = sprite.font_size
    if mouse_cor[0] > sprite.font_x and mouse_cor[0] < sprite.font_x + width and mouse_cor[1] > sprite.font_y and mouse_cor[1] < sprite.font_y + height:
        return True
def check_rect_cell(cell,rect):
    cell_rect = pygame.Rect(cell.X,cell.Y,cell.WIDTH,cell.HEIGHT)
    if pygame.Rect.colliderect(rect,cell_rect):
        return True
def check_rect_cell_list(list_cells,rect):
    for cell in list_cells:
        cell_rect = pygame.Rect(cell.X,cell.Y,cell.WIDTH,cell.HEIGHT)
        if pygame.Rect.colliderect(rect,cell_rect):
            return True
def text_cost(list_text_cost,finally_text = 'Купить за:',text_obj=None,settings=None):
    for resource in list_text_cost:
        resource_full_name = resource
        resource = resource.split('/')
        if resource[0] == 'gold_bullion':
            finally_text += ' '+resource[1]+' золота'
        if resource[0] == 'food':
            finally_text += ' '+resource[1]+' еды'
        if resource[0] == 'iron_bullion':
            finally_text += ' '+resource[1]+' железа'
        if resource[0] == 'crystal': 
            finally_text += ' '+resource[1]+' кристалла'
        if resource[0] == 'wood': 
            finally_text += ' '+resource[1]+' дерева'
        if resource[0] == 'stone': 
            finally_text += ' '+resource[1]+' камня'
        if len(list_text_cost[-1]) != 0:
            if list_text_cost[-1] != resource_full_name:
                finally_text +=','
    finally_text +='.'
    text_len = len(finally_text)
    text_x = settings['SCREEN_WIDTH']//2-((text_len//2)*text_obj.font_size)//2
    return finally_text,text_x
def move_map(event, list_map,SCREEN_W,SCREEN_H):
    #Изменяем координаты каждой клетки
    for cell in list_map:
        cell.X += event.rel[0]
        cell.Y += event.rel[1]
    #Если игровое поле ушло вправо от границы экрана
    if list_map[0].X > 0:
        change_x = list_map[0].X * -1
        #Возвращаем его к правой стороне экрана
        for cell in list_map:
            cell.X += change_x
    #Если игровое поле ушло влево от границы экрана
    elif  list_map[-1].X + list_map[-1].WIDTH    < SCREEN_W - SCREEN_W//19*3: 
        change_x = SCREEN_W - (list_map[-1].X + list_map[-1].WIDTH + SCREEN_W//19*3)
        #Возвращаем его к левой стороне экрана
        for cell in list_map:
            cell.X += change_x
    #Если игровое поле ушло вниз от границы экрана       
    if list_map[0].Y > 0:
        change_y = list_map[0].Y * -1
        #Возвращаем его к верхней стороне экрана
        for cell in list_map:
            cell.Y += change_y
    #Если игровое поле ушло вверх от границы экрана      
    elif  list_map[-1].Y + list_map[-1].WIDTH < SCREEN_H:
        change_y = SCREEN_H - (list_map[-1].Y + list_map[-1].WIDTH)
        #Возвращаем его к нижней стороне экрана
        for cell in list_map:
            cell.Y += change_y
def matrix_image(win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, 
                tree,mat_objetcs_lvl1,list_objects_cells_lvl1,SCREEN_W,
                SCREEN_H,count_move,changed_x,changed_y,
                ironmine, goldmine, farm, gemsmine,sawmill, stonebreaker,flag_green,list_studied_map,portal, fog_war,
                list_cor_player_xy,W_CELL_MINI_MAP ,H_CELL_MINI_MAP,X_FRAME_MM,Y_FRAME_MM,list_cells_MM,list_cor_portals,
                LENGTH_MAP,chest,fountain_exp,fountain_mana,watchtower,royal_academy,shack,tavern,market,castle,list_cor_castle_xy,
                dvorf,klaus,bard,golem,giant,yamy,ork,bomb_man,crossbowman,druid,centaur,ludorn,roggy,surtur,fountain_mana_empty,fountain_exp_empty,
                mountain,water,list_forest,win_rect,castle_goblin,man_potion):
    list_xy = [0,0]
    list_object = [player_lvl1, gold, iron, crystal, wood, stone, tree_full,tree,ironmine, goldmine, farm, gemsmine,sawmill, stonebreaker,portal,chest,fountain_exp,fountain_mana,watchtower,royal_academy,shack,tavern,market,castle,dvorf,klaus,bard,golem,giant,yamy,ork,bomb_man,crossbowman,druid,centaur,ludorn,roggy,surtur,fountain_mana_empty,fountain_exp_empty,
                mountain,water]
    #Индекс клетки, к которой привязан объект
    index_cells = 0
    # Координата конкретной клетки для миникарты
    X_CELL_MM = X_FRAME_MM
    Y_CELL_MM = Y_FRAME_MM
    # Нужно ли добавлять клетку для мини-карты
    flag_cell_MM = True
    #Перебераем список объектов
    for obj_list1 in mat_objetcs_lvl1:
        for obj in obj_list1:        
            flag_cell_MM =True
            if obj != '0':
                if check_rect_cell_list(list_object,win_rect):
                    if obj == 'p':   
                        #Привязываем координаты персонажа к клетке
                        player_lvl1.X = list_objects_cells_lvl1[index_cells].X+changed_x
                        player_lvl1.Y = list_objects_cells_lvl1[index_cells].Y+changed_y
                        list_cor_player_xy[0] = list_objects_cells_lvl1[index_cells].X+changed_x
                        list_cor_player_xy[1] = list_objects_cells_lvl1[index_cells].Y+changed_y
                        #отображаем персонажа
                        player_lvl1.show_image(win)
                        flag_cell_MM = False
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'yellow'))
                    #Отрисовуем ресурсы
                    elif obj == 'i':
                        iron.X = list_objects_cells_lvl1[index_cells].X
                        iron.Y = list_objects_cells_lvl1[index_cells].Y
                        iron.show_image(win)
                    elif obj == 'g':
                        gold.X = list_objects_cells_lvl1[index_cells].X
                        gold.Y = list_objects_cells_lvl1[index_cells].Y
                        gold.show_image(win)
                    elif obj == 'w':
                        wood.X = list_objects_cells_lvl1[index_cells].X
                        wood.Y = list_objects_cells_lvl1[index_cells].Y
                        wood.show_image(win)
                    elif obj == 'b':
                        stone.X = list_objects_cells_lvl1[index_cells].X
                        stone.Y = list_objects_cells_lvl1[index_cells].Y
                        stone.show_image(win)
                    elif obj == 'c':
                        crystal.X = list_objects_cells_lvl1[index_cells].X
                        crystal.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                        crystal.show_image(win)
                    elif obj == 'T':
                        tree_full.X = list_objects_cells_lvl1[index_cells].X
                        tree_full.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                        tree_full.show_image(win)
                    elif obj == 't':
                        tree.X = list_objects_cells_lvl1[index_cells].X
                        tree.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        tree.show_image(win)
                    elif obj == 'г':
                        mountain.X = list_objects_cells_lvl1[index_cells].X 
                        mountain.Y = list_objects_cells_lvl1[index_cells].Y 
                        mountain.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'mountain'))
                        flag_cell_MM = False
                    elif obj == 'в':
                        water.X = list_objects_cells_lvl1[index_cells].X 
                        water.Y = list_objects_cells_lvl1[index_cells].Y 
                        water.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'water'))
                        flag_cell_MM = False
                    elif obj == 'И':
                        man_potion.X = list_objects_cells_lvl1[index_cells].X
                        man_potion.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        man_potion.show_image(win)
                    elif obj == 'л':
                        list_forest[0].X = list_objects_cells_lvl1[index_cells].X 
                        list_forest[0].Y = list_objects_cells_lvl1[index_cells].Y
                        list_forest[0].show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'forest'))
                        flag_cell_MM = False
                        flag_cell_MM = False
                    elif obj == '\\':
                        list_forest[1].X = list_objects_cells_lvl1[index_cells].X 
                        list_forest[1].Y = list_objects_cells_lvl1[index_cells].Y 
                        list_forest[1].show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'forest'))
                        flag_cell_MM = False
                        flag_cell_MM = False
                    elif obj == '/':
                        list_forest[2].X = list_objects_cells_lvl1[index_cells].X 
                        list_forest[2].Y = list_objects_cells_lvl1[index_cells].Y 
                        list_forest[2].show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'forest'))
                        flag_cell_MM = False
                        flag_cell_MM = False
                    elif obj == '|':
                        list_forest[3].X = list_objects_cells_lvl1[index_cells].X 
                        list_forest[3].Y = list_objects_cells_lvl1[index_cells].Y 
                        list_forest[3].show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'forest'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'forest'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'forest'))
                        flag_cell_MM = False
                        flag_cell_MM = False
                    #Начало отрисовка на матрице карт 
                    elif obj =='А':
                        crossbowman.X = list_objects_cells_lvl1[index_cells].X
                        crossbowman.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        crossbowman.show_image(win)
                    elif obj =='Б':
                        bard.X = list_objects_cells_lvl1[index_cells].X
                        bard.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        bard.show_image(win)
                    elif obj =='В':
                        dvorf.X = list_objects_cells_lvl1[index_cells].X
                        dvorf.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        dvorf.show_image(win)
                    elif obj =='Г':
                        giant.X = list_objects_cells_lvl1[index_cells].X
                        giant.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        giant.show_image(win)
                    elif obj =='Д':
                        druid.X = list_objects_cells_lvl1[index_cells].X
                        druid.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        druid.show_image(win)
                    elif obj =='Е':
                        golem.X = list_objects_cells_lvl1[index_cells].X
                        golem.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        golem.show_image(win)
                    elif obj =='К':
                        centaur.X = list_objects_cells_lvl1[index_cells].X
                        centaur.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        centaur.show_image(win)
                    elif obj =='М':
                        klaus.X = list_objects_cells_lvl1[index_cells].X
                        klaus.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        klaus.show_image(win)
                    elif obj =='Л':
                        ludorn.X = list_objects_cells_lvl1[index_cells].X
                        ludorn.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        ludorn.show_image(win)
                    elif obj =='Р':
                        roggy.X = list_objects_cells_lvl1[index_cells].X
                        roggy.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        roggy.show_image(win)
                    elif obj =='С':
                        surtur.X = list_objects_cells_lvl1[index_cells].X
                        surtur.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        surtur.show_image(win)
                    elif obj =='Я':
                        yamy.X = list_objects_cells_lvl1[index_cells].X
                        yamy.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        yamy.show_image(win)
                    elif obj =='П':
                        bomb_man.X = list_objects_cells_lvl1[index_cells].X
                        bomb_man.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        bomb_man.show_image(win)
                    elif obj =='О':
                        ork.X = list_objects_cells_lvl1[index_cells].X
                        ork.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        ork.show_image(win)
                    ##Конец отрисовки на матрице карт
                    elif obj == 'M':
                        fountain_mana.X = list_objects_cells_lvl1[index_cells].X
                        fountain_mana.Y = list_objects_cells_lvl1[index_cells].Y
                        fountain_mana.show_image(win)
                    elif obj == 'E':
                        fountain_exp.X = list_objects_cells_lvl1[index_cells].X
                        fountain_exp.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19
                        fountain_exp.show_image(win)
                    elif obj == 'm':
                        fountain_mana_empty.X = list_objects_cells_lvl1[index_cells].X
                        fountain_mana_empty.Y = list_objects_cells_lvl1[index_cells].Y
                        fountain_mana_empty.show_image(win)
                    elif obj == 'e':
                        fountain_exp_empty.X = list_objects_cells_lvl1[index_cells].X
                        fountain_exp_empty.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19
                        fountain_exp_empty.show_image(win)
                    elif obj == 'F':
                        farm.X = list_objects_cells_lvl1[index_cells].X
                        farm.Y = list_objects_cells_lvl1[index_cells].Y 
                        farm.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'A':
                        royal_academy.X = list_objects_cells_lvl1[index_cells].X
                        royal_academy.Y = list_objects_cells_lvl1[index_cells].Y 
                        royal_academy.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    # elif obj == 'B':
                    #     tavern.X = list_objects_cells_lvl1[index_cells].X
                    #     tavern.Y = list_objects_cells_lvl1[index_cells].Y 
                    #     tavern.show_image(win)
                    elif obj == 'K':
                        castle.X = list_objects_cells_lvl1[index_cells].X
                        castle.Y = list_objects_cells_lvl1[index_cells].Y 
                        castle.show_image(win)
                        list_cor_castle_xy[0] = list_objects_cells_lvl1[index_cells].X+SCREEN_W//19
                        list_cor_castle_xy[1] = list_objects_cells_lvl1[index_cells].Y+SCREEN_W//19
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP*2,Y_CELL_MM,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP*2,Y_CELL_MM+H_CELL_MINI_MAP,'green_dark'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'green_dark'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'green_dark'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP*2,'green_dark'))
                        list_cells_MM.append((X_CELL_MM+W_CELL_MINI_MAP*2,Y_CELL_MM + H_CELL_MINI_MAP*2,'green_dark'))
                        list_cells_MM.append((X_CELL_MM+W_CELL_MINI_MAP,Y_CELL_MM + H_CELL_MINI_MAP*2,'green_dark'))
                        flag_cell_MM = False
                    elif obj == 'З':
                        castle_goblin.X = list_objects_cells_lvl1[index_cells].X
                        castle_goblin.Y = list_objects_cells_lvl1[index_cells].Y 
                        castle_goblin.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'red'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'red'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP*2,Y_CELL_MM,'red'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP*2,Y_CELL_MM+H_CELL_MINI_MAP,'red'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'red'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'red'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP*2,'red'))
                        list_cells_MM.append((X_CELL_MM+W_CELL_MINI_MAP*2,Y_CELL_MM + H_CELL_MINI_MAP*2,'red'))
                        list_cells_MM.append((X_CELL_MM+W_CELL_MINI_MAP,Y_CELL_MM + H_CELL_MINI_MAP*2,'red'))
                        flag_cell_MM = False
                    elif obj == 'O':
                        market.X = list_objects_cells_lvl1[index_cells].X
                        market.Y = list_objects_cells_lvl1[index_cells].Y 
                        market.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'J':
                        tavern.X = list_objects_cells_lvl1[index_cells].X
                        tavern.Y = list_objects_cells_lvl1[index_cells].Y 
                        tavern.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'S':
                        shack.X = list_objects_cells_lvl1[index_cells].X
                        shack.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                        shack.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        flag_cell_MM = False
                    elif obj == 's':
                        shack.X = list_objects_cells_lvl1[index_cells].X
                        shack.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2 
                        shack.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        flag_cell_MM = False
                    elif obj == 'N':
                        stonebreaker.X = list_objects_cells_lvl1[index_cells].X
                        stonebreaker.Y = list_objects_cells_lvl1[index_cells].Y 
                        stonebreaker.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'W':
                        watchtower.X = list_objects_cells_lvl1[index_cells].X
                        watchtower.Y = list_objects_cells_lvl1[index_cells].Y - SCREEN_W//19/2
                        watchtower.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        flag_cell_MM = False
                    elif obj == 'X':
                        gemsmine.X = list_objects_cells_lvl1[index_cells].X
                        gemsmine.Y = list_objects_cells_lvl1[index_cells].Y 
                        gemsmine.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'R':
                        goldmine.X = list_objects_cells_lvl1[index_cells].X
                        goldmine.Y = list_objects_cells_lvl1[index_cells].Y 
                        goldmine.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'H':
                        sawmill.X = list_objects_cells_lvl1[index_cells].X
                        sawmill.Y = list_objects_cells_lvl1[index_cells].Y 
                        sawmill.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'D':
                        ironmine.X = list_objects_cells_lvl1[index_cells].X
                        ironmine.Y = list_objects_cells_lvl1[index_cells].Y 
                        ironmine.show_image(win)
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'white'))
                        list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'white'))
                        list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'white'))
                        flag_cell_MM = False
                    elif obj == 'P':
                        portal.X = list_objects_cells_lvl1[index_cells].X
                        portal.Y = list_objects_cells_lvl1[index_cells].Y
                        portal.show_image(win)
                    elif obj == 'C':
                        chest.X = list_objects_cells_lvl1[index_cells].X
                        chest.Y = list_objects_cells_lvl1[index_cells].Y
                        chest.show_image(win)
            for i in player_lvl1.list_capture_buildings:
                if list_xy[0] == i[1] and list_xy[1] == i[0]:
                    flag_green.X = list_objects_cells_lvl1[index_cells].X + SCREEN_W // 38
                    flag_green.Y = list_objects_cells_lvl1[index_cells].Y  - SCREEN_W // 40
                    flag_green.show_image(win)
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'green_dark'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM,'green_dark'))
                    list_cells_MM.append((X_CELL_MM,Y_CELL_MM + H_CELL_MINI_MAP,'green_dark'))
                    list_cells_MM.append((X_CELL_MM + W_CELL_MINI_MAP,Y_CELL_MM+ H_CELL_MINI_MAP,'green_dark'))
                    flag_cell_MM = False
            for c in list_cells_MM:
                if c[0] == X_CELL_MM and c[1] == Y_CELL_MM:
                    flag_cell_MM = False
                    break
            if flag_cell_MM ==True :
                list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'green'))
            """"Индексы текущей клетки по циклу"""
            
            list_xy[0]+= 1
            if list_xy[0] == LENGTH_MAP:
                list_xy[0] = 0
                list_xy[1] += 1
            index_cells += 1

            X_CELL_MM += W_CELL_MINI_MAP
        Y_CELL_MM += H_CELL_MINI_MAP
        X_CELL_MM = X_FRAME_MM
def fog_war_func(mat_objetcs_lvl1,X_FRAME_MM,Y_FRAME_MM,list_studied_map,fog_war,list_objects_cells_lvl1,win,list_cells_MM,LENGTH_MAP,W_CELL_MINI_MAP,H_CELL_MINI_MAP):
    X_CELL_MM = X_FRAME_MM
    Y_CELL_MM = Y_FRAME_MM
    list_xy = [0,0]
    #Индекс клетки, к которой привязан объект
    index_cells = 0
    # Цикл для отрисовки тумана
    for obj_list1 in mat_objetcs_lvl1:#961
        for obj_list2 in obj_list1:
            #Перебираем список с изучеными клетками и проверяем с текущей клеткой 
            for cor in list_studied_map:#0-961
                if list_xy == cor:
                    draw_frog = False
                    break
                else: 
                    draw_frog = True
            if draw_frog:

                fog_war.X = list_objects_cells_lvl1[index_cells].X
                fog_war.Y = list_objects_cells_lvl1[index_cells].Y
                fog_war.show_image(win)

                list_cells_MM.append((X_CELL_MM,Y_CELL_MM,'black'))
            list_xy[0]+= 1
            if list_xy[0] == LENGTH_MAP:
                list_xy[0] = 0
                list_xy[1] += 1
                
            index_cells += 1

            X_CELL_MM += W_CELL_MINI_MAP
        Y_CELL_MM += H_CELL_MINI_MAP
        X_CELL_MM = X_FRAME_MM         
def create_map(list_cells, list_objects_cells,SCREEN_W,SCREEN_H):
    #Стартовые координаты клеток
    x = 0
    y = 0
    #Перебераем ряды уровня
    for el in list_cells:
        #Перебераем каждую клетку
        for cell in el:
            #Если значение клетки равно нулю
            if cell == '0':
                #В список клеток добавляем объект клетки
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/cell.jpg'))
            if cell == 'd':
                #В список клеток добавляем объект клетки
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/cell.jpg'))
            if cell == 't':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/MatrixImage/field_path.png'))
            if cell == '1':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/MatrixImage/flower0.png'))
            if cell == '2':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/MatrixImage/flower1.png'))
            if cell == '3':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/MatrixImage/flower2.png'))
            if cell == '4':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19,SCREEN_W//19,'images/MatrixImage/flower3.png'))
            if cell == 'a':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand2.png'))
            if cell == 'b':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand1.png'))
            if cell == 'c':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand5.png'))
            if cell == 'e':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand8.png'))
            if cell == 'f':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand6.png'))
            if cell == 'o':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand9.png'))
            if cell == 'k':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand10.png'))
            if cell == 'h':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand4.png'))
            if cell == 'j':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand7.png'))
            if cell == 'g':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand11.png'))
            if cell == 'l':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand3.png'))
            if cell == 'm':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand12.png'))
            if cell == 'n':
                list_objects_cells.append(Graphic_elements(x,y,width=SCREEN_W//19,height=SCREEN_W//19,path='images/MatrixImage/sand13.png'))
            if cell == 'б':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19, SCREEN_W//19, 'images/MatrixImage/bridge.png'))
            if cell == 'Б':
                list_objects_cells.append(Graphic_elements(x,y,SCREEN_W//19, SCREEN_W//19, 'images/MatrixImage/bridge2.png'))
            #Увеличиваем х, двигаясь по ряду
            x += SCREEN_W//19
        #Увеличиваем y, двигаясь по столбцамя
        y += SCREEN_W //19
        #Обнуляем x
        x = 0
#Перебираем список захваченый зданий и игроку начесляем ресурсы
def resourse_accural(list_capture_buildings_symbol, resources_dict):
    for i in list_capture_buildings_symbol:
        if i == 'F':
            resources_dict['food'] += randint(5,6)
        elif i == 'H':
            resources_dict['wood'] += randint(4,5)
        elif i == 'D':
            resources_dict['iron_bullion'] += randint(2,3)
        elif i == 'N':
            resources_dict['stone'] += randint(3,4)
        elif i == 'R':
            resources_dict['gold_bullion'] += randint(1,2)
        elif i == 'X':
            resources_dict['crystal'] += 1
def move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,SCREEN_W,SCREEN_H):
    #Перемещаемся к герою по X
    if CENTER_CELL_COR[0] >= list_cor_player_xy[0]:
        difference = CENTER_CELL_COR[0] - list_cor_player_xy[0]
        for cell in list_objects_cells_lvl1:
            cell.X += difference
    elif CENTER_CELL_COR[0] <= list_cor_player_xy[0]:
        difference = list_cor_player_xy[0] - CENTER_CELL_COR[0]  
        for cell in list_objects_cells_lvl1:
            cell.X -= difference
    #Перемещаемся к герою по Y
    if CENTER_CELL_COR[1] >= list_cor_player_xy[1]:
        difference = CENTER_CELL_COR[1] - list_cor_player_xy[1]
        for cell in list_objects_cells_lvl1:
            cell.Y += difference
    elif CENTER_CELL_COR[1] <= list_cor_player_xy[1]:
        difference = list_cor_player_xy[1] - CENTER_CELL_COR[1]  
        for cell in list_objects_cells_lvl1:
            cell.Y -= difference
    #Если игровое поле ушло вправо от границы экрана
    if list_objects_cells_lvl1[0].X > 0:
        change_x = list_objects_cells_lvl1[0].X * -1
        #Возвращаем его к правой стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.X += change_x
    #Если игровое поле ушло влево от границы экрана
    elif  list_objects_cells_lvl1[-1].X + list_objects_cells_lvl1[-1].WIDTH < SCREEN_W:
        change_x = SCREEN_W - (list_objects_cells_lvl1[-1].X + list_objects_cells_lvl1[-1].WIDTH)
        #Возвращаем его к левой стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.X += change_x
    #Если игровое поле ушло вниз от границы экрана       
    if list_objects_cells_lvl1[0].Y > 0:
        change_y = list_objects_cells_lvl1[0].Y * -1
        #Возвращаем его к верхней стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.Y += change_y
    #Если игровое поле ушло вверх от границы экрана      
    elif  list_objects_cells_lvl1[-1].Y + list_objects_cells_lvl1[-1].WIDTH < SCREEN_H:
        change_y = SCREEN_H - (list_objects_cells_lvl1[-1].Y + list_objects_cells_lvl1[-1].WIDTH)
        #Возвращаем его к нижней стороне экрана
        for cell in list_objects_cells_lvl1:
            cell.Y += change_y
def create_icon_card(SCREEN_W,SCREEN_H,list_cards_pl,list_cards_menu_hero,list_card_pl_reserv):
    list_cards_menu_hero.clear()
    x = SCREEN_W//2.133
    y = SCREEN_H//44
    width = SCREEN_W//1.8666 - x
    for i in range(len(list_cards_pl)):#
        if list_cards_pl[i][0] != None:
            path = 'images/cards/'+str(list_cards_pl[i][0])+'.png'
            card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=path,name=list_cards_pl[i][0])
            card.image_load()
        else:
            card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=None,name=list_cards_pl[i][0])
        if not card in list_cards_menu_hero:
            list_cards_menu_hero.append(card)
        x+= SCREEN_W//11
    y = SCREEN_H//5.333
    x = SCREEN_W//2.133
    for i in range(len(list_card_pl_reserv)):
        if list_card_pl_reserv[i][0] != None:
            path = 'images/cards/'+str(list_card_pl_reserv[i][0])+'.png'
            card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=path,name=list_card_pl_reserv[i][0])
        else:
            card = Graphic_elements(x=x,y=y,width=width,height=SCREEN_H//7.5,path=list_card_pl_reserv[i][0],name=list_card_pl_reserv[i][0])
        if not card in list_cards_menu_hero:
            list_cards_menu_hero.append(card)
        x+= SCREEN_W//11
def create_icon_card_post_army(list_cards_post_army,list_cards_pl,list_cards_pl_post_army):
    for obj in list_cards_pl_post_army:
        if obj[0] != None:
            index = list_cards_pl_post_army.index(obj)
            list_cards_post_army[index].path = 'images/cards/'+str(obj[0])+'.png'
            list_cards_post_army[index].image_load()
    for obj in list_cards_pl:
        if obj[0] != None:
            index = list_cards_pl.index(obj)+6
            list_cards_post_army[index].path = 'images/cards/'+str(obj[0])+'.png'
            list_cards_post_army[index].image_load()
def change_x_y_width_height(artifact_pressed, sprite):
    sprite.X = artifact_pressed.start_x
    sprite.Y = artifact_pressed.start_y
    sprite.WIDTH = artifact_pressed.start_width
    sprite.HEIGHT = artifact_pressed.start_height
    artifact_pressed.X = sprite.start_x
    artifact_pressed.Y = sprite.start_y
    artifact_pressed.WIDTH = sprite.start_width
    artifact_pressed.HEIGHT = sprite.start_height
    sprite.start_x = sprite.X
    sprite.start_y = sprite.Y
    sprite.start_width = sprite.WIDTH
    sprite.start_height = sprite.HEIGHT
    artifact_pressed.start_x = artifact_pressed.X
    artifact_pressed.start_y = artifact_pressed.Y
    artifact_pressed.start_width = artifact_pressed.WIDTH
    artifact_pressed.start_height = artifact_pressed.HEIGHT
    if sprite.path != None:
        sprite.image_load()
    if artifact_pressed.path != None:
        artifact_pressed.image_load()
def generate_error(frame_error,error_text_obj,error_content,win):
    frame_error.show_image(win)
    error_text_obj.font_content = error_content
    error_text_obj.show_text(win)
def change_images(artifact_pressed,sprite):
    art_pr_img = artifact_pressed.path
    artifact_pressed.path = sprite.path
    sprite.path = art_pr_img
    sprite.image_load()
    if artifact_pressed.path != None:
        artifact_pressed.image_load()
    artifact_pressed.X = artifact_pressed.start_x
    artifact_pressed.Y = artifact_pressed.start_y
def effect_resource(resources_dict, obj,effect_art_skills_name_dict,dict_arguments):
    name_obj = obj.path.split('/')[-1]
    if name_obj in effect_art_skills_name_dict.keys():
        value_dict = effect_art_skills_name_dict[name_obj].split(';')
        if value_dict[-1] == 'resourcesdict':
            if value_dict[-2] == '+':
                resources_dict[value_dict[0]] += int(value_dict[1])
            elif value_dict[-2] == '-':
                resources_dict[value_dict[0]] -= int(value_dict[1])
            elif value_dict[-2] == '*':
                resources_dict[value_dict[0]] *= int(value_dict[1])
            elif value_dict[-2] == '/':
                resources_dict[value_dict[0]] /= int(value_dict[1])
        if value_dict[-1] == 'characteristicdict':
            if value_dict[-2] == '+':
                dict_arguments['characteristic_dict'][value_dict[0]] += int(value_dict[1])
            elif value_dict[-2] == '-':
                dict_arguments['characteristic_dict'][value_dict[0]] -= int(value_dict[1])
            elif value_dict[-2] == '*':
                if name_obj == 'skill_idol_people_learn.png':
                    if randint(0,4) == 4:
                        dict_arguments['characteristic_dict'][value_dict[0]] *= int(value_dict[1])
                else:
                    dict_arguments['characteristic_dict'][value_dict[0]] *= int(value_dict[1])

            elif value_dict[-2] == '/':
                dict_arguments['characteristic_dict'][value_dict[0]] /= int(value_dict[1])
def effect_hero(list_all_artifact,dict_artifact_on,dict_artifact_on_past,list_learn_skills,player_lvl1,dict_card_characteristics,dict_card_price,dict_arguments):
    for obj in list_all_artifact:
        if obj.NAME != None and obj.path != None:
            dict_artifact_on[obj.NAME] = obj.path.split('/')[-1]
        if obj.path == None and obj.NAME != None:
            dict_artifact_on[obj.NAME] = None
    if dict_artifact_on['helmet'] != dict_artifact_on_past['helmet'] :
        if dict_artifact_on['helmet'] == 'helmet_ice.png' and dict_artifact_on_past['helmet'] != 'helmet_ice.png':
            dict_arguments['characteristic_dict']['lvl_skill_diplomacy'] +=2
        if dict_artifact_on['helmet'] != 'helmet_ice.png' and dict_artifact_on_past['helmet'] == 'helmet_ice.png':
            dict_arguments['characteristic_dict']['lvl_skill_diplomacy'] -=2
        if dict_artifact_on['helmet'] == 'helmet_fire.png' and dict_artifact_on_past['helmet'] != 'helmet_fire.png':
            dict_arguments['index_fog'] += 1
        if dict_artifact_on['helmet'] != 'helmet_fire.png' and dict_artifact_on_past['helmet'] == 'helmet_fire.png':
            dict_arguments['index_fog'] -= 1
        
    if dict_artifact_on['boots'] != dict_artifact_on_past['boots']:
        if dict_artifact_on['boots'] == 'boots_ice.png' and dict_artifact_on_past['boots'] != 'boots_ice.png':
            dict_arguments['characteristic_dict']['count_step'] +=2
            player_lvl1.count_step +=2
        if dict_artifact_on['boots'] != 'boots_ice.png' and dict_artifact_on_past['boots'] == 'boots_ice.png':
            dict_arguments['characteristic_dict']['count_step'] -=2
            player_lvl1.count_step -=2
        if dict_artifact_on['boots'] == 'boots_hero.png' and dict_artifact_on_past['boots'] != 'boots_hero.png':
            dict_arguments['characteristic_dict']['lvl_skill_domesticpolitics'] +=2
        if dict_artifact_on['boots'] != 'boots_hero.png' and dict_artifact_on_past['boots'] == 'boots_hero.png':
            dict_arguments['characteristic_dict']['lvl_skill_domesticpolitics'] -=2
    if dict_artifact_on['chest'] != dict_artifact_on_past['chest']:
        if dict_artifact_on['chest'] == 'chest_fire.png' and dict_artifact_on_past['chest'] != 'chest_fire.png':
            dict_arguments['characteristic_dict']['change_mana'] +=1
        if dict_artifact_on['chest'] != 'chest_fire.png' and dict_artifact_on_past['chest'] == 'chest_fire.png':
            dict_arguments['characteristic_dict']['change_mana'] -=1
        if dict_artifact_on['chest'] == 'chest_ice.png' and dict_artifact_on_past['chest'] != 'chest_ice.png':
            for jey in dict_card_characteristics.keys():
                dict_card_characteristics[jey][1]+=1
        if dict_artifact_on['chest'] != 'chest_ice.png' and dict_artifact_on_past['chest'] == 'chest_ice.png':
            for jey in dict_card_characteristics.keys():
                dict_card_characteristics[jey][1]-=1
    if dict_artifact_on['sword'] != dict_artifact_on_past['sword']:
        if dict_artifact_on['sword'] == 'sword_fire.png' and dict_artifact_on_past['sword'] != 'sword_fire.png':
            dict_arguments['characteristic_dict']['lvl_skill_fight'] +=2
        if dict_artifact_on['sword'] != 'sword_fire.png' and dict_artifact_on_past['sword'] == 'sword_fire.png':
            dict_arguments['characteristic_dict']['lvl_skill_fight'] -=2
        if dict_artifact_on['sword'] == 'sword_hero.png' and dict_artifact_on_past['sword'] != 'sword_hero.png':
            dict_arguments['changed_dmg'] +=5
        if dict_artifact_on['sword'] != 'sword_hero.png' and dict_artifact_on_past['sword'] == 'sword_hero.png':
            dict_arguments['changed_dmg'] -=5
        if dict_artifact_on['sword'] == 'sword_ice.png' and dict_artifact_on_past['sword'] != 'sword_ice.png':
            for key in dict_card_characteristics.keys():
                if dict_card_characteristics[key][2] == 'mountain':
                    dict_card_characteristics[key][1] += 2
        if dict_artifact_on['sword'] != 'sword_ice.png' and dict_artifact_on_past['sword'] == 'sword_ice.png':
            for key in dict_card_characteristics.keys():
                if dict_card_characteristics[key][2] == 'mountain':
                    dict_card_characteristics[key][1] -= 2
    if dict_artifact_on['shield'] != dict_artifact_on_past['shield']:
        if dict_artifact_on['shield'] == 'shield_fire.png' and dict_artifact_on_past['shield'] != 'shield_fire.png':
            dict_arguments['changed_hp'] += 5
        if dict_artifact_on['shield'] != 'shield_fire.png' and dict_artifact_on_past['shield'] == 'shield_fire.png':
            dict_arguments['changed_hp'] -= 5
        if dict_artifact_on['shield'] == 'shield_hero.png' and dict_artifact_on_past['shield'] != 'shield_hero.png':
            for key in dict_card_characteristics.keys():
                if dict_card_characteristics[key][2] == 'earth':
                    dict_card_characteristics[key][0] += 2
        if dict_artifact_on['shield'] != 'shield_hero.png' and dict_artifact_on_past['shield'] == 'shield_hero.png':
            for key in dict_card_characteristics.keys():
                if dict_card_characteristics[key][2] == 'earth':
                    dict_card_characteristics[key][0] -= 2
        if dict_artifact_on['shield'] == 'shield_ice.png' and dict_artifact_on_past['shield'] != 'shield_ice.png':
            for key in dict_card_characteristics.keys():
                dict_card_characteristics[key][0] += 1
        if dict_artifact_on['shield'] != 'shield_ice.png' and dict_artifact_on_past['shield'] == 'shield_ice.png':
            for key in dict_card_characteristics.keys():
                dict_card_characteristics[key][0] -= 1
    if 'skill_forest_path_learn' in list_learn_skills:
        dict_arguments['characteristic_dict']['count_step'] +=2
        player_lvl1.count_step +=2
        list_learn_skills.remove('skill_forest_path_learn')
    if 'skill_leader_learn' in list_learn_skills:
        for key in dict_card_price.keys():
            name_card = dict_card_price[key].split(';')
            del name_card[0]
            for text in name_card:
                dict_card_price[key] = 'gold_bullion/'+str(int(dict_card_price[key].split(';')[0].split('/')[-1])-1)+';'+text
        list_learn_skills.remove('skill_leader_learn')
    if 'skill_earth_blessing_learn' in list_learn_skills:
        for key in dict_card_characteristics.keys():
            dict_card_characteristics[key][0] +=1
            dict_card_characteristics[key][1] +=1
        list_learn_skills.remove('skill_earth_blessing_learn')
def save_game(dict_arguments,list_all_artifact,player_lvl1,list_slots_skills_hero,list_card_camp):
    for key in list_all_artifact:
        if key.NAME !=None:
            key_dict = key.NAME
            dict_arguments['dict_path_artifact'][key_dict] = key.path
        if key.NAME == None:
            key_dict = list_all_artifact.index(key)-4
            dict_arguments['dict_path_artifact']['reserv'+str(key_dict)] = key.path
    for key in list_slots_skills_hero:
        key_dict = key.path.split('/')[-1].split('_learn')[0]
        dict_arguments['dict_path_skills'][key_dict] = key.path
    for key in list_card_camp:
        if 'locked' in key.path:
            dict_arguments['dict_card_path_camp'][key.path.split('/')[-1].split('_')[0]] = key.path
        else:
            dict_arguments['dict_card_path_camp'][key.path.split('/')[-1].split('.')[0]] = key.path
        
    dict_arguments['characteristic_dict']['count_step'] = player_lvl1.count_step
    dict_arguments['list_capture_buildings'] = player_lvl1.list_capture_buildings
    dict_arguments['list_capture_buildings_symbol'] = player_lvl1.list_capture_buildings_symbol
    dict_arguments['cardgame_variables']['card_attacker'] = None
    dict_arguments['cardgame_variables']['card_that_move_pl'] = None
    dict_arguments['cardgame_variables']['card_victim'] = None
    dict_arguments['cardgame_variables']['picked_card'] = None
    dict_arguments['cardgame_variables']['card_that_showing_desc'] = None
    dict_arguments['cardgame_variables']['healed_card'] = None
    dict_arguments['cardgame_variables']['hp_text'] = None
    dict_arguments['cardgame_variables']['card_that_move_en'] = None
    with open('saves/config1.json','w') as file:
        json.dump(dict_arguments,file,indent=4,ensure_ascii=True)
def change_story(dict_arguments,story_scene,story,mouse_cor,next_story,event,win,bg,button_continue_story,sound_book):
    if dict_arguments['scene'] == story:
        bg.show_image(win)
        story_scene.show_image(win)
        button_continue_story.show_image(win)
        if check_mouse_cor(button_continue_story,mouse_cor):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dict_arguments['scene'] = next_story
                sound_book.play_sound()
                return True
            button_continue_story.path = 'images/button_continue_story_b.png'
            button_continue_story.image_load()
        else:
            button_continue_story.path = 'images/button_continue_story_y.png'
            button_continue_story.image_load()
def change_help(dict_arguments,help_scene,help_name,mouse_cor,next_help,event,win,bg,sound_book,button_back,button_next,button_leave,previous_help):
    if dict_arguments['scene'] == help_name:
        bg.show_image(win)
        help_scene.show_image(win)
        if button_back != None:
            button_back.show_image(win)
        if button_next != None:
            button_next.show_image(win)
        button_leave.show_image(win)
        if  button_next != None:
            if check_mouse_cor(button_next,mouse_cor):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dict_arguments['scene'] = next_help
                    sound_book.play_sound()
                    return True
                button_next.path = 'images/button_continue_story_b.png'
                button_next.image_load()
            else:
                button_next.path = 'images/button_continue_story_y.png'
                button_next.image_load()
        if button_back != None:
            if check_mouse_cor(button_back,mouse_cor):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    dict_arguments['scene'] = previous_help
                    sound_book.play_sound()
                    return True
                button_back.path = 'images/menu_hero_back_b.png'
                button_back.image_load()
            else:
                button_back.path = 'images/menu_hero_back_y.png'
                button_back.image_load()
        if check_mouse_cor(button_leave,mouse_cor):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                dict_arguments['scene'] = 'menu'
                sound_book.play_sound()
                return True
            button_leave.path = 'images/button_continue_story_b.png'
            button_leave.image_load()
        else:
            button_leave.path = 'images/button_continue_story_y.png'
            button_leave.image_load()
