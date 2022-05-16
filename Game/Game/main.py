from const import*
from objects import*
from Addition_Module import*
from Menu import*
pygame.init()
#Основная фунуция
def run_game(dict_arguments):
    time = pygame.time.Clock()
    while dict_arguments['game']:
        
        #Цикл проверки событий
        for event in pygame.event.get():
            #Услове выхода из игры
            mouse_cor = pygame.mouse.get_pos() 
            if event.type == pygame.QUIT:
                dict_arguments['game'] = False
            if dict_arguments['scene'] == 'market':
            # if dict_arguments['scene'] == 'sandwich':
                if check_mouse_cor(button_market_back,mouse_cor):
                    button_market_back.path = 'images/market_back_b.png'
                    button_market_back.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dict_arguments['scene'] = 'lvl1'
                        player_lvl1.flag_market = False
                else:
                    button_market_back.path = 'images/market_back_y.png'
                    button_market_back.image_load()
                if check_mouse_cor(button_market_back,mouse_cor) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                    dict_arguments['scene'] = 'lvl1'
            if dict_arguments['scene'] == 'menu_hero':
                menu_hero.show_image(win)
                button_menu_hero_back.show_image(win)
                #Условия кнопки назад
                if check_mouse_cor(button_menu_hero_back,mouse_cor):
                    button_menu_hero_back.path = 'images/menu_hero_back_b.png'
                    button_menu_hero_back.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dict_arguments['scene'] = 'lvl1'
                else:
                    button_menu_hero_back.path = 'images/menu_hero_back_y.png'
                    button_menu_hero_back.image_load()


                if event.type == pygame.MOUSEMOTION:
                    pos  = pygame.mouse.get_pos()
                    if dict_arguments['card_pressed'] != None:
                        dict_arguments['card_pressed'].X = pos[0] - dict_arguments['card_pressed'].WIDTH//2
                        dict_arguments['card_pressed'].Y = pos[1] - dict_arguments['card_pressed'].HEIGHT//2
                        dict_arguments['index_card'] = list_cards_menu_hero.index(dict_arguments['card_pressed'])
                    if dict_arguments['artifact_pressed'] != None:
                        dict_arguments['artifact_pressed'].X = pos[0] - dict_arguments['artifact_pressed'].WIDTH//2
                        dict_arguments['artifact_pressed'].Y = pos[1] - dict_arguments['artifact_pressed'].HEIGHT//2
                        dict_arguments['index_card'] = list_all_artifact.index(dict_arguments['artifact_pressed'])

                if event.type == pygame.MOUSEBUTTONUP:
                    if dict_arguments['card_pressed'] != None:
                        for sprite in list_cards_menu_hero:
                            if check_mouse_cor(sprite,mouse_cor=mouse_cor) and dict_arguments['index_card'] != list_cards_menu_hero.index(sprite):
                                if dict_arguments['card_pressed'].path != None:
                                    change_x_y_width_height(dict_arguments['card_pressed'], sprite)
                                    break
                            else:
                                dict_arguments['card_pressed'].X = dict_arguments['card_pressed'].start_x
                                dict_arguments['card_pressed'].Y = dict_arguments['card_pressed'].start_y
                        dict_arguments['card_pressed'] = None
                    #Условия для взаимодействия между артефактами
                    dict_arguments['name_art_res'] = None
                    if dict_arguments['artifact_pressed'] != None:
                        if dict_arguments['artifact_pressed'].NAME == None:
                            dict_arguments['name_art_res'] = dict_arguments['artifact_pressed'].path.split('/')[-1]
                            dict_arguments['name_art_res'] = dict_arguments['name_art_res'].split('.')[0]
                            dict_arguments['name_art_res'] = dict_arguments['name_art_res'].split('_')[0]
                        for sprite in list_all_artifact:
                            if check_mouse_cor(sprite,mouse_cor=mouse_cor) and list_all_artifact.index(dict_arguments['artifact_pressed']) != list_all_artifact.index(sprite):
                                #Резервные артефакты между мобой 
                                if sprite.NAME == None and dict_arguments['artifact_pressed'].NAME == None:
                                    change_images(dict_arguments['artifact_pressed'],sprite)
                                    break
                                #Резервный артефакт с активным 
                                if dict_arguments['name_art_res'] == sprite.NAME and dict_arguments['artifact_pressed'].NAME == None and sprite.NAME != None:
                                    change_images(dict_arguments['artifact_pressed'],sprite)
                                    break
                                #Активный с пустой резервной клеткой 
                                if dict_arguments['artifact_pressed'].NAME != None and sprite.NAME == None and sprite.path == None:
                                    change_images(dict_arguments['artifact_pressed'],sprite)
                                    break
                                # Активный с резервным артефактом
                                if  dict_arguments['artifact_pressed'].NAME != None and sprite.NAME == None and sprite.path != None:
                                    name_art_act = sprite.path.split('/')[-1]
                                    name_art_act = name_art_act.split('.')[0]
                                    name_art_act= name_art_act.split('_')[0]
                                    if name_art_act == dict_arguments['artifact_pressed'].NAME:
                                        change_images(dict_arguments['artifact_pressed'],sprite)
                                        break
                            else:
                                dict_arguments['artifact_pressed'].X = dict_arguments['artifact_pressed'].start_x
                                dict_arguments['artifact_pressed'].Y = dict_arguments['artifact_pressed'].start_y
                                dict_arguments['artifact_pressed'].WIDTH = dict_arguments['artifact_pressed'].start_width
                                dict_arguments['artifact_pressed'].HEIGHT = dict_arguments['artifact_pressed'].start_height
                    dict_arguments['artifact_pressed'] = None
                
                text_lvl_hero.show_text(win)
                if len(str(characteristic_dict['exp'])) > dict_arguments['change_exp_x']:
                    exp_img.X = exp_img.start_x+(len(str(characteristic_dict['exp']))-1)*step_exp_text
                    dict_arguments['change_exp_x'] = len(str(characteristic_dict['exp']))
                if len(str(characteristic_dict['exp']))  < dict_arguments['change_exp_x']:
                    exp_img.X = exp_img.start_x+(len(str(characteristic_dict['exp']))-1)*step_exp_text
                    dict_arguments['change_exp_x'] = len(str(characteristic_dict['exp']))
                text_exp_hero.font_content = str(characteristic_dict['exp'])+'/'+str(dict_arguments['max_exp_lvl'])
                text_exp_hero.show_text(win)
                if len(str(characteristic_dict['mana'])) > dict_arguments['change_mana_x']:
                    mana_img.X = mana_img.start_x+(len(str(characteristic_dict['mana']))-1)*step_exp_text
                    dict_arguments['change_mana_x'] = len(str(characteristic_dict['mana']))
                if len(str(characteristic_dict['mana'])) < dict_arguments['change_mana_x']:
                    mana_img.X = mana_img.start_x+(len(str(characteristic_dict['mana']))-1)*step_exp_text
                    dict_arguments['change_mana_x'] = len(str(characteristic_dict['mana']))
                text_mana.font_content = 'Мана: '+str(characteristic_dict['mana'])+'/'+str(dict_arguments['max_mana'])
                text_mana.show_text(win)
                menu_hero_icon_eliot.show_image(win)
                exp_img.show_image(win)
                mana_img.show_image(win)
                text_mana_cost_click.show_text(win)
                for obj in list_slots_base_skills:
                    obj.show_image(win)
                
                for obj in list_slots_skills_hero:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if check_mouse_cor(obj,mouse_cor=mouse_cor):
                            path_skill = obj.path.split('/')[-1]
                            path_skill = path_skill.split('.')[0]
                            if  path_skill in list_order_skills:
                                past_index_skill = list_order_skills.index(path_skill) - 1
                                if past_index_skill < 0:
                                    past_index_skill = None
                                if past_index_skill != None:
                                    if list_order_skills[past_index_skill].split('_')[-1] == 'learn':
                                        dict_arguments['flag_buy_skill'] = True
                                    else:
                                        dict_arguments['flag_buy_skill'] = False
                                else:
                                    dict_arguments['flag_buy_skill'] = True
                                if  dict_arguments['flag_buy_skill']:
                                    if characteristic_dict['mana'] >= dict_arguments['skill_cost'] and path_skill.split('_')[-1] != 'learn':
                                        
                                        characteristic_dict['mana']-=dict_arguments['skill_cost']
                                        list_order_skills[list_order_skills.index(path_skill)] = path_skill+'_learn'
                                        path_skill = obj.path.split('/')[-1]
                                        
                                        path_skill = path_skill.split('.')[0]
                                        obj.path = 'images/skills/eliot/'+path_skill+'_learn.png'
                                        list_learn_skills.append(path_skill+'_learn')
                                        obj.image_load()
                    obj.show_image(win)
                for obj in list_cards_menu_hero:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if check_mouse_cor(obj,mouse_cor=mouse_cor):
                            dict_arguments['card_pressed'] = obj
                    if obj != dict_arguments['card_pressed'] and obj.path != None:
                        obj.show_image(win)
                    if dict_arguments['card_pressed'] != None and dict_arguments['card_pressed'].path != None:
                        dict_arguments['card_pressed'].show_image(win)
                #Условия взятия и отрисовки артефакта
                for obj in list_all_artifact:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if check_mouse_cor(obj,mouse_cor=mouse_cor) and obj.path != None:
                            dict_arguments['artifact_pressed'] = obj
                    if obj != dict_arguments['artifact_pressed'] and obj.path != None:
                        obj.WIDTH, obj.HEIGHT = obj.start_width,obj.start_height
                        obj.image_load()
                        obj.show_image(win)     
                if dict_arguments['artifact_pressed'] != None:
                    dict_arguments['artifact_pressed'].WIDTH = settings['SCREEN_WIDTH']//12.8
                    dict_arguments['artifact_pressed']. HEIGHT = settings['SCREEN_HEIGHT']//7.57
                    dict_arguments['artifact_pressed'].image_load()
                    dict_arguments['artifact_pressed'].show_image(win)
                for obj in list_cards_menu_hero:
                    if check_mouse_cor(obj,mouse_cor) and dict_arguments['card_pressed'] == None and obj.NAME != None:
                        desc.path = 'images/cards/desc/desc_'+obj.NAME+'.png'
                        desc.image_load()
                        desc.show_image(win)
                        break
                    else:
                        desc.path = None
                for obj in list_all_artifact:
                    if check_mouse_cor(obj,mouse_cor) and dict_arguments['artifact_pressed'] == None and obj.path != None :
                        path = obj.path.split('/')[-1]
                        desc_artifact.path = 'images/artifacts/desc/desc_'+path
                        desc_artifact.image_load()
                        desc_artifact.show_image(win)
                        break
                    else:
                        desc_artifact.path = None
                for desc_obj in list_slots_base_skills:
                    if check_mouse_cor(desc_obj,mouse_cor):
                        path_desc = desc_obj.path.split('/')[-1]
                        desc_base_skill.path = 'images/skills/desc/desc_'+path_desc
                        desc_base_skill.image_load()
                        desc_base_skill.show_image(win)
                    else:
                        desc_base_skill.path = None
                for desc_obj in list_slots_skills_hero:
                    if check_mouse_cor(desc_obj,mouse_cor):
                        path_desc = desc_obj.path.split('/')[-1]
                        path_desc_learn = path_desc.split('_')[-1]
                        if path_desc_learn == 'learn.png':
                            path_desc = path_desc.split('_learn')[0]
                            desc_skill_hero.path = 'images/skills/eliot/desc/desc_'+path_desc+'.png'
                        else:
                            desc_skill_hero.path = 'images/skills/eliot/desc/desc_'+path_desc
                        desc_skill_hero.image_load()
                        desc_skill_hero.show_image(win)
                    else:
                        desc_skill_hero.path = None
                for obj in list_text_lvl_base_skills:
                    obj.show_text(win)
                
                        
                #############################################################################   
            if dict_arguments['scene'] == 'menu':
                book.show_image(win)
                #Изменяем размер кнопки при наводке
                for button in list_buttons:
                    button.resize_button_menu(mouse_cor=mouse_cor,SCREEN_W = settings['SCREEN_WIDTH'],SCREEN_H = settings['SCREEN_HEIGHT'])
                    button.show_image(win)
                # Реакция на нажатие кнопок
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if check_mouse_cor(button_play,mouse_cor):
                        sound_book.play_sound()
                        dict_arguments['scene'] = 'lvl1'
                    elif check_mouse_cor(button_exit,mouse_cor):
                        sound_book.play_sound()
                        dict_arguments['game'] = False
                            #Отрисовуем книгу
                
                #Отрисовуем кнопки
            
            effect_hero(list_all_artifact,dict_artifact_on,dict_arguments['dict_artifact_on_past'],characteristic_dict,list_learn_skills,player_lvl1)
            dict_arguments['dict_artifact_on_past'] = dict_artifact_on.copy()
            if dict_arguments['scene'] == 'lvl1':
                
                #Если нажата левая кнопка мыши
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Если заканчиваем ход
                    if check_mouse_cor(button_end_move,mouse_cor) and (player_lvl1.where_move == None or player_lvl1.count_step == 0) and player_lvl1.flag_move:
                        #Обновляем количество ходов игрока
                        player_lvl1.count_step = characteristic_dict['count_step']
                        player_lvl1.where_move = None
                        dict_arguments['flag_button_end'] = True
                        dict_arguments['flag_show_new_day'] = 0
                        #Начисляем русурсы за захваченые здания
                        resourse_accural(player_lvl1.list_capture_buildings_symbol, dict_arguments['resources_dict'])
                    if dict_arguments['artifact_chest'] != None and check_mouse_cor(dict_arguments['artifact_chest'],mouse_cor):
                        name_artifact = dict_arguments['artifact_chest'].path.split('/')[-1]
                        name_artifact = name_artifact.split('.')[0]
                        name_artifact= name_artifact.split('_')[0]
                        for obj in list_all_artifact:
                            if obj.path == None:
                                if obj.NAME != None:
                                    if name_artifact == obj.NAME:
                                        obj.path = dict_arguments['artifact_chest'].path
                                        obj.image_load()
                                        break
                                if obj.NAME == None:
                                    obj.path = dict_arguments['artifact_chest'].path
                                    obj.image_load()
                                    break
                        else:
                            dict_arguments['flag_show_error'] = 0
                            dict_arguments['resources_dict']['gold'] += 20
                        dict_arguments['artifact_chest'] = None
                        player_lvl1.flag_draw_chest = False
                        mat_objetcs_lvl1[player_lvl1.chest_cor[0]][player_lvl1.chest_cor[1]] = '0'
                        player_lvl1.flag_move = True
                    if check_mouse_cor(amount_money,mouse_cor):
                        dict_arguments['artifact_chest'] = None
                        player_lvl1.flag_draw_chest = False
                        mat_objetcs_lvl1[player_lvl1.chest_cor[0]][player_lvl1.chest_cor[1]] = '0'
                        player_lvl1.flag_move = True
                        dict_arguments['resources_dict']['gold'] += 20
                    for obj in list_choice_base_skill:
                        if check_mouse_cor(obj,mouse_cor) and dict_arguments['flag_use_royal_academy'] and player_lvl1.flag_academy:
                            name_skill = obj.path.split('/')[-1]
                            name_skill = name_skill.split('.')[0]
                            characteristic_dict['lvl_'+name_skill]+=1
                            player_lvl1.flag_move = True
                            dict_arguments['flag_use_royal_academy'] = False
                            
                    for obj in list_choice_base_skill:
                        if check_mouse_cor(obj,mouse_cor) and characteristic_dict['exp']>=dict_arguments['max_exp_lvl']:
                            name_skill = obj.path.split('/')[-1]
                            name_skill = name_skill.split('.')[0]
                            characteristic_dict['lvl_'+name_skill]+=1
                            player_lvl1.flag_move = True
                            characteristic_dict['exp'] -=dict_arguments['max_exp_lvl']
                            characteristic_dict['lvl']+=1
                            dict_arguments['max_exp_lvl']+=100
                            text_new_lvl.font_content = ('Поздровляем! У вас новый уровень;Выберите улучшение способности;'+'Новый уровень - '+str(characteristic_dict['lvl']+1)).split(';')
                            text_lvl_hero.font_content = ('Текущий уровень - '+str(characteristic_dict['lvl'])+';До следующего уровня:').split(';')
                    for obj in list_text_lvl_base_skills:
                        name_skill = list_text_lvl_base_skills.index(obj)
                        name_skill = list_choice_base_skill[name_skill]
                        name_skill = name_skill.path.split('/')[-1].split('.')[0]
                        obj.font_content = "Уровень: "+str(characteristic_dict['lvl_'+name_skill])
                        
                    #Когда нажали на кнопку "К ГЕРОЮ" 
                    if check_mouse_cor(button_to_hero,mouse_cor):
                        #Перемещаемся к герою 
                        move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
                    if check_mouse_cor(frame,mouse_cor):
                        dict_arguments['scene'] = 'menu_hero'
                    dict_arguments['buttonIsPressed'] = True
                #Кнопка мыши отпущена
                if event.type == pygame.MOUSEBUTTONUP:
                    dict_arguments['buttonIsPressed'] = False
                #Если двигаем мышью и кнопка мыши зажата
                if event.type == pygame.MOUSEMOTION and dict_arguments['buttonIsPressed']:
                    #Вызываем функцию перемещения карты
                    if player_lvl1.flag_move:
                        move_map(event, list_objects_cells_lvl1,SCREEN_W=settings['SCREEN_WIDTH'],SCREEN_H=settings['SCREEN_HEIGHT'])

                if event.type == pygame.MOUSEMOTION:
                    if dict_arguments['scene'] == 'lvl1':
                        i=0
                        for b in list_interface_button:
                            if check_mouse_cor(b,mouse_cor):
                                b.path = list_paths_pressed[i][1]
                                b.image_load()
                            else:
                                b.path = list_paths_pressed[i][0]
                                b.image_load()
                            

                            i+=1
        # if dict_arguments['scene'] == 'sandwich':
        if dict_arguments['scene'] == 'market':
            win.fill('blue')
            background_market.show_image(win)
            button_market_back.show_image(win)
            
        if dict_arguments['scene'] == 'lvl1':
            amount_crystal.font_content = str(dict_arguments['resources_dict']['crystal'])
            amount_food.font_content = str(dict_arguments['resources_dict']['food'])
            amount_iron.font_content = str(dict_arguments['resources_dict']['iron'])
            amount_gold.font_content = str(dict_arguments['resources_dict']['gold'])
            amount_wood.font_content = str(dict_arguments['resources_dict']['wood'])
            amount_stone.font_content = str(dict_arguments['resources_dict']['stone'])
            win.fill('black')
            # Отрисовуем клетки
            list_xy = [0,0]
            for cell in list_objects_cells_lvl1:
                
                for cor in player_lvl1.list_studied_map:
                    if list_xy == cor:
                        dict_arguments['draw_cells']=True
                        break
                    else: 
                        dict_arguments['draw_cells'] = False
                list_xy[0]+= 1
                if list_xy[0] == LENGTH_MAP_LVL1:
                    list_xy[0] = 0
                    list_xy[1] += 1
                if dict_arguments['draw_cells']:
                    cell.show_image(win)
            
            #Индекс строки, где находиться объект
            player_lvl1.blind_move(index=int(settings['INDEX_FOG']),flag_player=[0,0,True])
            dict_arguments['list_cells_MM'] = []
            matrix_image(
                        win, player_lvl1, gold, iron, crystal, wood, stone, tree_full, tree,
                        mat_objetcs_lvl1,list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],
                        player_lvl1.count_move,player_lvl1.changed_x,player_lvl1.changed_y,
                        ironmine, goldmine, farm, gemsmine,sawmill, stonebreaker,flag_green,
                        list_studied_map=player_lvl1.list_studied_map,portal = portal,
                        fog_war=fog_war,list_cor_player_xy=list_cor_player_xy,W_CELL_MINI_MAP=W_CELL_MINI_MAP,
                        H_CELL_MINI_MAP=H_CELL_MINI_MAP,X_FRAME_MM=X_FRAME_MM,
                        Y_FRAME_MM=Y_FRAME_MM, list_cells_MM = dict_arguments['list_cells_MM'], list_cor_portals = list_cor_portals,
                        LENGTH_MAP = LENGTH_MAP_LVL1,chest=chest,fountain_mana=fountain_mana,fountain_exp=fountain_exp,watchtower=watchtower,
                        shack=shack,royal_academy=royal_academy,tavern=tavern,market=market)
            
            # matrix_image_blind(list_objects_cells_lvl1,mat_objetcs_lvl1,player_lvl1,list_objects_cells_lvl1,player_lvl1.changed_x,player_lvl1.changed_y,win)
            #Отрисовуем полоску справа
            # pygame.draw.rect(win, (255,223,196), (settings['SCREEN_WIDTH']-settings['SCREEN_WIDTH']//19*3,0,settings['SCREEN_WIDTH']//19*3,settings['SCREEN_HEIGHT']))
            interface_bg.show_image(win)
            frame.show_image(win)
            button_to_hero.show_image(win)
            button_to_castle.show_image(win)
            frame_mini_map.show_image(win)
            text_date.show_text(win)
            elliot_img.show_image(win)
            player_info.show_text(win)
            #Новый день
            if player_lvl1.flag_market:
                # dict_arguments['scene'] = 'sandwich'
                dict_arguments['scene'] = 'market'
            if dict_arguments['flag_button_end'] and player_lvl1.where_move == None and player_lvl1.flag_move:
                player_lvl1.flag_move = False
                if characteristic_dict['day'] == 7:
                    characteristic_dict['week']+=1
                    characteristic_dict['day'] = 0
                    fountain_mana.path = 'images/buildings/fountain_mana.png'
                    fountain_mana.image_load()
                    fountain_exp.path = 'images/buildings/fountain_exp.png'
                    fountain_exp.image_load()
                    dict_arguments['flag_use_fountain_exp'] = True
                    dict_arguments['flag_use_fountain_mana'] = True
                    dict_arguments['flag_use_tavern'] = True
                    dict_arguments['flag_use_royal_academy'] = True
                    dict_arguments['flag_use_shack'] = True
                characteristic_dict['day']+=1
                if 'skill_idol_people_learn' in list_learn_skills:
                    if randint(0,4) == 4:
                        resources_dict['gold']+=characteristic_dict['contribution']*characteristic_dict['lvl_skill_domesticpolitics']
                resources_dict['gold']+=characteristic_dict['contribution']*characteristic_dict['lvl_skill_domesticpolitics']
                text_date.font_content = ('День: '+str(characteristic_dict['day'])+';Неделя: '+str(characteristic_dict['week'])).split(';')
                dict_arguments['flag_button_end'] = False
                for obj in list_all_artifact:
                    if obj.NAME != None and obj.path != None:
                        effect_resource(resources_dict, obj,effect_art_skills_name_dict,characteristic_dict)
                for obj in list_slots_skills_hero:
                    effect_resource(resources_dict, obj,effect_art_skills_name_dict,characteristic_dict)
                        
            if dict_arguments['flag_show_new_day'] < 100:
                player_lvl1.flag_move = False
                if dict_arguments['flag_show_new_day'] == 0:
                    text_new_day.font_content = ('           Новый день;        Получено за день; ;Яблок - '+str(dict_arguments['resources_dict']['food']-dict_arguments['past_resources_dict']['food'])+'      Золота - '+str(dict_arguments['resources_dict']['gold']-dict_arguments['past_resources_dict']['gold'])+'; ;Железа - '+str(dict_arguments['resources_dict']['iron']-dict_arguments['past_resources_dict']['iron'])+'      Кристаллов - '+str(dict_arguments['resources_dict']['crystal']-dict_arguments['past_resources_dict']['crystal'])+'; ;Камня - '+str(dict_arguments['resources_dict']['stone']-dict_arguments['past_resources_dict']['stone'])+'      Дерева - '+str(dict_arguments['resources_dict']['wood']-dict_arguments['past_resources_dict']['wood'])).split(';')
                    dict_arguments['past_resources_dict'] = dict_arguments['resources_dict'].copy()
                frame_new_day.show_image(win)        
                text_new_day.show_text(win)
                dict_arguments['flag_show_new_day'] += 1
            else:
                player_lvl1.flag_move = True
            #Условие нового уровня              
            if characteristic_dict['exp'] >= dict_arguments['max_exp_lvl']:
                dict_arguments['flag_new_lvl'] = True
            if  dict_arguments['flag_new_lvl'] and player_lvl1.flag_move:
                frame_notification.show_image(win)
                player_lvl1.flag_move = False
                for obj in list_choice_base_skill:
                    obj.show_image(win)
                    if check_mouse_cor(obj,mouse_cor):
                        path_desc = obj.path.split('/')[-1]
                        desc_base_skill.path = 'images/skills/desc/desc_'+path_desc
                        desc_base_skill.X = 0
                        desc_base_skill.Y = frame_notification.Y
                        desc_base_skill.WIDTH = desc_base_skill.start_width-settings['SCREEN_WIDTH']//19
                        desc_base_skill.image_load()
                        desc_base_skill.show_image(win)
                    else:
                        desc_base_skill.path = None
                        desc_base_skill.X = desc_base_skill.start_x
                        desc_base_skill.Y = desc_base_skill.start_y
                        desc_base_skill.WIDTH = desc_base_skill.start_width
            # Условие Академии         
            if  dict_arguments['flag_use_royal_academy'] and player_lvl1.flag_academy:
                text_new_lvl.index = 1
                text_new_lvl.font_content = ('Вы пришли в королевскую академи!;  Выберите какой навык улучшить').split(';')
                frame_notification.show_image(win)
                player_lvl1.flag_move = False
                for obj in list_choice_base_skill:
                    obj.show_image(win)
                    if check_mouse_cor(obj,mouse_cor):
                        path_desc = obj.path.split('/')[-1]
                        desc_base_skill.path = 'images/skills/desc/desc_'+path_desc
                        desc_base_skill.X = 0
                        desc_base_skill.Y = frame_notification.Y
                        desc_base_skill.WIDTH = desc_base_skill.start_width-settings['SCREEN_WIDTH']//19
                        desc_base_skill.image_load()
                        desc_base_skill.show_image(win)
                    else:
                        desc_base_skill.path = None
                        desc_base_skill.X = desc_base_skill.start_x
                        desc_base_skill.Y = desc_base_skill.start_y
                        desc_base_skill.WIDTH = desc_base_skill.start_width
                text_new_lvl.index = 2
                text_new_lvl.show_text(win)
            #Условие открытого сундука
            if player_lvl1.flag_draw_chest and player_lvl1.flag_move:
                player_lvl1.flag_move = False
                dict_arguments['flag_button_end'] = False
                player_lvl1.near_chest = False
                chest_open.show_image(win)
                chest_text_choice.show_text(win)
                if dict_arguments['artifact_chest'] == None :
                    dict_arguments['artifact_chest'] = choice(list_artifact_graphic_elements)
                    player_lvl1.flag_choice_artifact = True
                    name_artifact = dict_arguments['artifact_chest'].path.split('/')[-1]
                    name_artifact = name_artifact.split('.')[0]
                dict_arguments['artifact_chest'].X = (settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//19*3)+settings['SCREEN_WIDTH']//19
                dict_arguments['artifact_chest'].Y = (settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//19*3)+settings['SCREEN_WIDTH']//19
                dict_arguments['artifact_chest'].show_image(win)
                amount_money.X = (settings['SCREEN_WIDTH']//2-settings['SCREEN_WIDTH']//19*3)+settings['SCREEN_WIDTH']//19*3.5
                amount_money.Y = (settings['SCREEN_HEIGHT']//2-settings['SCREEN_HEIGHT']//19*3)+settings['SCREEN_WIDTH']//19
                amount_money.show_image(win)
                if check_mouse_cor(dict_arguments['artifact_chest'],mouse_cor):
                    dict_arguments['artifact_chest'].WIDTH = settings['SCREEN_WIDTH']//19*1.9
                    dict_arguments['artifact_chest'].HEIGHT = settings['SCREEN_WIDTH']//19*1.9
                    desc_artifact.path = 'images/artifacts/desc/desc_'+name_artifact+'.png'
                    desc_artifact.X = settings['SCREEN_WIDTH']//19
                    desc_artifact.Y = chest_open.Y
                    desc_artifact.image_load()
                    desc_artifact.show_image(win)
                else:
                    dict_arguments['artifact_chest'].WIDTH = settings['SCREEN_WIDTH']//19*1.5
                    dict_arguments['artifact_chest'].HEIGHT = settings['SCREEN_WIDTH']//19*1.5
                    desc_artifact.X = desc_artifact.start_x
                    desc_artifact.Y = desc_artifact.start_y
                    desc_artifact.path = None
                dict_arguments['artifact_chest'].image_load()
                if check_mouse_cor(amount_money,mouse_cor):
                    amount_money.WIDTH = settings['SCREEN_WIDTH']//19*1.9
                    amount_money.HEIGHT = settings['SCREEN_WIDTH']//19*1.9
                else:
                    amount_money.WIDTH = settings['SCREEN_WIDTH']//19*1.5
                    amount_money.HEIGHT = settings['SCREEN_WIDTH']//19*1.5
                amount_money.image_load()
            if player_lvl1.flag_fountain_exp and dict_arguments['flag_use_fountain_exp']:
                characteristic_dict['exp']+=exp_fountain
                dict_arguments['flag_use_fountain_exp'] = False
                player_lvl1.flag_fountain_exp = False
                fountain_exp.path = 'images/buildings/fountain_exp_empty.png'
                fountain_exp.image_load()
            elif player_lvl1.flag_fountain_mana and dict_arguments['flag_use_fountain_mana']:
                characteristic_dict['mana']+=mana_fountain*characteristic_dict['change_mana']
                dict_arguments['flag_use_fountain_mana'] = False
                player_lvl1.flag_fountain_mana = False
                fountain_mana.path = 'images/buildings/fountain_mana_empty.png'
                fountain_mana.image_load()
            if player_lvl1.flag_tavern  and player_lvl1.flag_draw_chest == False and player_lvl1.flag_tower==False and dict_arguments['flag_use_tavern']:
                player_lvl1.flag_tavern = False
                dict_arguments['flag_button_end'] = False
                dict_arguments['flag_use_tavern'] = False
                random = randint(0,2)
                if random == 0:
                    text_tavern.font_content =( '    Вы выиграли!; 20  золотых в карты. ;Приходите через неделю;').split(';')
                    resources_dict['gold']+=20
                if random == 1:
                    text_tavern.font_content = ('; Вы ничего не получили. ; Приходите через неделю').split(';')
                if random == 2:
                    if resources_dict['gold'] <20:
                        if resources_dict['gold'] == 1:
                            text_tavern.font_content =( '    Вас ограбили!;    На 1 золотую;Приходите через неделю').split(';')
                        else:
                            text_tavern.font_content =( '    Вас ограбили!;    На '+str(resources_dict['gold'])+' золотых;Приходите через неделю').split(';')
                        resources_dict['gold'] = 0
                    else:
                        resources_dict['gold'] -=20
                        text_tavern.font_content =( '    Вас ограбили!;    На 20 золотых;Приходите через неделю').split(';')
                dict_arguments['flag_show_tavern'] = 0
            if player_lvl1.flag_tower:
                player_lvl1.blind_move(index=6,flag_player=[player_lvl1.tower_cor[1],player_lvl1.tower_cor[0],False])
                player_lvl1.flag_tower = False
            if player_lvl1.flag_shack and dict_arguments['flag_use_shack']:
                characteristic_dict['mana']+=mana_shack*characteristic_dict['change_mana']
                dict_arguments['flag_use_shack'] = False
                player_lvl1.flag_shack = False
            
            if player_lvl1.flag_shack and dict_arguments['flag_use_shack'] == False and player_lvl1.flag_pressed:
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_shack = False
            if player_lvl1.flag_fountain_exp and dict_arguments['flag_use_fountain_exp'] == False and player_lvl1.flag_pressed:
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_fountain_exp = False
            if player_lvl1.flag_fountain_mana and dict_arguments['flag_use_fountain_mana'] == False and player_lvl1.flag_pressed:
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_fountain_mana = False
            if player_lvl1.flag_academy and dict_arguments['flag_use_royal_academy'] == False and player_lvl1.flag_pressed :
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_academy = False
            if player_lvl1.flag_tavern and dict_arguments['flag_use_tavern'] == False and player_lvl1.flag_pressed :
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_tavern = False
            # отрисовуем клетки на мини-карте
            for cor in dict_arguments['list_cells_MM']:
                if cor[2] == 'green':
                    green.X = cor[0]
                    green.Y = cor[1]
                    green.show_image(win)
                elif cor[2] == 'black':
                    black.X = cor[0]
                    black.Y = cor[1]
                    black.show_image(win)
                elif cor[2] == 'yellow':
                    yellow.X = cor[0]
                    yellow.Y = cor[1]
                    yellow.show_image(win)
                elif cor[2] == 'white':
                    white.X = cor[0]
                    white.Y = cor[1]
                    white.show_image(win)
                elif cor[2] == 'green_dark':
                    green_dark.X = cor[0]
                    green_dark.Y = cor[1]
                    green_dark.show_image(win)
            #Отображаем кол-во ресурсов на экране
            if dict_arguments['resources_dict']['food'] != 0:
                apple.show_image(win)
                amount_food.show_text(win)
            if dict_arguments['resources_dict']['iron'] != 0:
                iron_bullion.show_image(win)
                amount_iron.show_text(win)
            if dict_arguments['resources_dict']['gold'] != 0:
                gold_bullion.show_image(win)
                amount_gold.show_text(win)
            if dict_arguments['resources_dict']['crystal'] != 0:
                crystal_purified.show_image(win)
                amount_crystal.show_text(win)
            if dict_arguments['resources_dict']['stone'] != 0:
                stone_purified.show_image(win)
                amount_stone.show_text(win)
            if dict_arguments['resources_dict']['wood'] != 0:
                wood2.show_image(win)
                amount_wood.show_text(win)
            text_step_count.show_text(win)
            button_end_move.show_image(win)
            text_step_count.font_content = 'Осталось ходов: '+str(player_lvl1.count_step)
            
            player_lvl1.move_sprite(mat_objetcs_lvl1, LENGTH_MAP_LVL1,dict_arguments['resources_dict'],recourse_sounds,list_cor_portals=list_cor_portals,
                                    )
            # Перемещение к игроку после телепорта
            if player_lvl1.need_to_move_to_hero:
                if dict_arguments['flag_to_move_to_hero'] == 12:
                    move_to_hero(CENTER_CELL_COR, list_cor_player_xy, list_objects_cells_lvl1, settings['SCREEN_WIDTH'], settings['SCREEN_HEIGHT'])
                    player_lvl1.need_to_move_to_hero = False
                    dict_arguments['flag_to_move_to_hero'] = 0
                dict_arguments['flag_to_move_to_hero']+=1
        if dict_arguments['flag_show_error'] < 100:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            chest_text_gold.show_text(win)
            dict_arguments['flag_show_error'] += 1
        if dict_arguments['flag_show_tavern'] < 30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_tavern.show_text(win)
            dict_arguments['flag_show_tavern'] += 1
        if dict_arguments['flag_show_error_next_week'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_next_week_buildings.show_text(win)
            dict_arguments['flag_show_error_next_week'] +=1
        time.tick(int(settings['FPS']))
        #Обновляем экран
        pygame.display.flip()


run_game(dict_arguments)
