from const import*
from objects import*
from Addition_Module import*
from Menu import*
from constants_cardgame import*
from additional_functions_cardgame import*
from battle_functions_cardgame import*
from event_functions_cardgame import*
from sounds_cardgame import*
from Text_cardgame import*
from draw_function import draw_all
from profilehooks import profile
pygame.init()
@profile
#Основная фунуция
def run_main(dict_arguments):
    index = 0
    water = choice(list_water)
    time = pygame.time.Clock()
    while dict_arguments['game']:
        if dict_arguments['cardgame_variables']['who_won'] == 'enemy' and dict_arguments['flag_fight_start_post'] : 
            dict_arguments['flag_fight_start_post'] = False
            for i in dict_arguments['resources_dict'].keys():
                if dict_arguments['resources_dict'][i] != 0:
                    dict_arguments['resources_dict'][i] = dict_arguments['resources_dict'][i]//2
        effect_hero(list_all_artifact,dict_artifact_on,dict_arguments['dict_artifact_on_past'],characteristic_dict,list_learn_skills,player_lvl1,dict_card_characteristics,dict_card_price,dict_arguments)
        dict_arguments['dict_artifact_on_past'] = dict_artifact_on.copy()
        for obj in list_text_lvl_base_skills:
            name_skill = list_text_lvl_base_skills.index(obj)
            name_skill = list_choice_base_skill[name_skill]
            name_skill = name_skill.path.split('/')[-1].split('.')[0]
            obj.font_content = "Уровень: "+str(characteristic_dict['lvl_'+name_skill])
        #Цикл проверки событий
        for event in pygame.event.get():
            #Услове выхода из игры
            mouse_cor = pygame.mouse.get_pos() 
            if event.type == pygame.QUIT:
                dict_arguments['game'] = False
            if dict_arguments['scene'] == 'result_screen':
                # Если навелись на кнопку окончания боя
                if event.type == pygame.MOUSEMOTION:
                    if check_mouse_cor(button_end_fight,mouse_cor):
                        button_end_fight.path = 'images/buttons/end_fight_w.png'
                    else:
                        button_end_fight.path = 'images/buttons/end_fight_y.png'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Если нажали на кнопку окончания боя
                    if check_mouse_cor(button_end_fight,mouse_cor):
                        dict_arguments['scene'] = 'lvl1'
                        if dict_arguments['cardgame_variables']['who_won'] == 'player':
                            dict_arguments['resources_dict']['gold_bullion']+=dict_arguments['trophy_gold']
                            characteristic_dict['exp']+=dict_arguments['trophy_exp']
                            if dict_arguments['flag_fight_start_post'] != True:
                                mat_objetcs_lvl1[player_lvl1.card_cor[0]][player_lvl1.card_cor[1]] = '0'
                        if dict_arguments['cardgame_variables']['who_won'] != 'player':
                            mat_objetcs_lvl1[player_lvl1.player_cor[0]][player_lvl1.player_cor[1]] = '0'
                            player_lvl1.player_cor = city_cor_enter
                            mat_objetcs_lvl1[city_cor_enter[0]][city_cor_enter[1]] = 'p'
                        player_lvl1.flag_card = False
                        dict_arguments['trophy_exp'] = 0
                        dict_arguments['trophy_gold'] = 0
                        dict_arguments['cardgame_variables'] = {
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
                        dict_arguments['cardgame_variables']['hero_skill'] = dict_skills[str(settings['SKILL'])]
                        if '_bw' in dict_arguments['cardgame_variables']['hero_skill'].path:
                            dict_arguments['cardgame_variables']['hero_skill'].path = dict_arguments['cardgame_variables']['hero_skill'].path.split('_bw')[0]+'.png'
                        dict_arguments['cardgame_variables']['hero_skill'].image_load()
                        for card_losed in dict_arguments['list_losed_card_pl']:
                            for card_pl in list_cards_pl:
                                if card_losed == card_pl[0]:
                                    list_cards_pl[list_cards_pl.index(card_pl)][0] = None
                                    break
                        for i in range(len(dict_arguments['list_cards_en'])):
                            dict_arguments['list_cards_en'][i][0] = None
                        dict_arguments['list_losed_card_enemy'] = list()
                        dict_arguments['list_losed_card_pl'] = list()
                        create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
                        player_lvl1.flag_move = True
                        dict_arguments['flag_fight_start_post'] = False
            if dict_arguments['scene'] == 'city':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if check_mouse_cor(castle,mouse_cor):
                        dict_arguments['scene'] = 'castle'
                    if check_mouse_cor(camp,mouse_cor) and dict_arguments['dict_bought_city']['camp']:
                        dict_arguments['scene'] = 'camp'
                    if check_mouse_cor(camp,mouse_cor) == False and dict_arguments['dict_bought_city']['camp']:
                        dict_arguments['flag_show_error_blocked_camp'] = 0
                    if check_mouse_cor(altar,mouse_cor) and dict_arguments['dict_bought_city']['altar']:
                        dict_arguments['scene'] = 'altar'
                    if check_mouse_cor(button_city_back,mouse_cor):
                        player_lvl1.flag_city = False
                        dict_arguments['scene'] = 'lvl1'
                    if check_mouse_cor(button_post_army,mouse_cor):
                        dict_arguments['scene'] = 'post_army'
                        create_icon_card_post_army(list_cards_post_army,list_cards_pl,list_cards_pl_post_army)
                if check_mouse_cor(button_city_back,mouse_cor):
                    button_city_back.path = 'images/menu_hero_back_b.png'
                    button_city_back.image_load()
                else:
                    button_city_back.path = 'images/menu_hero_back_y.png'
                    button_city_back.image_load()
                if check_mouse_cor(button_post_army,mouse_cor):
                    button_post_army.path = 'images/post_army_y.png'
                    button_post_army.image_load()
                else:
                    button_post_army.path = 'images/post_army_b.png'
                    button_post_army.image_load()
                if dict_arguments['dict_bought_city']['church'] and dict_arguments['flag_church']:
                    characteristic_dict['lvl_skill_domesticpolitics']+=5 
                    dict_arguments['flag_church'] = False
                if dict_arguments['dict_bought_city']['forge'] and dict_arguments['flag_forge']:
                    for key in dict_card_characteristics.keys():
                        dict_card_characteristics[key][0]+=3
                        dict_card_characteristics[key][1]+=3
                    dict_arguments['flag_forge'] = False

            if dict_arguments['scene'] == 'post_army':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if check_mouse_cor(button_city_back,mouse_cor):
                        dict_arguments['scene'] = 'city'
                if check_mouse_cor(button_city_back,mouse_cor):
                    button_city_back.path = 'images/menu_hero_back_b.png'
                    button_city_back.image_load()
                else:
                    button_city_back.path = 'images/menu_hero_back_y.png'
                    button_city_back.image_load()
                if event.type == pygame.MOUSEMOTION:
                    pos  = pygame.mouse.get_pos()
                    if dict_arguments['card_pressed'] != None:
                        dict_arguments['card_pressed'].X = pos[0] - dict_arguments['card_pressed'].WIDTH//2
                        dict_arguments['card_pressed'].Y = pos[1] - dict_arguments['card_pressed'].HEIGHT//2
                        dict_arguments['index_card'] = list_cards_post_army.index(dict_arguments['card_pressed'])
                for obj in list_cards_post_army:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if check_mouse_cor(obj,mouse_cor=mouse_cor):
                            dict_arguments['card_pressed'] = obj
                    if obj != dict_arguments['card_pressed'] and obj.path != None:
                        obj.show_image(win)
                    if dict_arguments['card_pressed'] != None and dict_arguments['card_pressed'].path != None:
                        dict_arguments['card_pressed'].show_image(win)
                if event.type == pygame.MOUSEBUTTONUP:
                    if dict_arguments['card_pressed'] != None:
                        for sprite in list_cards_post_army:
                            if check_mouse_cor(sprite,mouse_cor=mouse_cor) and dict_arguments['index_card'] != list_cards_post_army.index(sprite):
                                if dict_arguments['card_pressed'].path != None:
                                    change_images(dict_arguments['card_pressed'], sprite)
                                    index_choice_card = list_cards_post_army.index(sprite)
                                    index_pressed_card = list_cards_post_army.index(dict_arguments['card_pressed'])
                                    if index_choice_card > 5:
                                        if index_pressed_card > 5:
                                            name_card = list_cards_pl[index_pressed_card-6][0]
                                            list_cards_pl[index_pressed_card-6][0] = list_cards_pl[index_choice_card-6][0]
                                            list_cards_pl[index_choice_card-6][0] = name_card
                                        if index_pressed_card <= 5:
                                            name_card = list_cards_pl_post_army[index_pressed_card][0]
                                            list_cards_pl_post_army[index_pressed_card][0] = list_cards_pl[index_choice_card-6][0]
                                            list_cards_pl[index_choice_card-6][0] = name_card
                                    if index_choice_card <= 5:
                                        if index_pressed_card <= 5:#Армия в армию
                                            name_card = list_cards_pl_post_army[index_pressed_card][0]
                                            list_cards_pl_post_army[index_pressed_card][0] = list_cards_pl_post_army[index_choice_card][0]
                                            list_cards_pl_post_army[index_choice_card][0] = name_card

                                        if index_pressed_card > 5:#резерв Армию 
                                            name_card = list_cards_pl[index_pressed_card-6][0]
                                            list_cards_pl[index_pressed_card-6][0] = list_cards_pl_post_army[index_choice_card][0]
                                            list_cards_pl_post_army[index_choice_card][0] = name_card
                                    create_icon_card_post_army(list_cards_post_army,list_cards_pl,list_cards_pl_post_army)
                                    break
                            else:
                                dict_arguments['card_pressed'].X = dict_arguments['card_pressed'].start_x
                                dict_arguments['card_pressed'].Y = dict_arguments['card_pressed'].start_y
                        dict_arguments['card_pressed'] = None
            if dict_arguments['scene'] == 'castle':
                if check_mouse_cor(button_build,mouse_cor):
                    button_build.path = 'images/button_build_w.png'
                    button_build.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if castle_selected.NAME != 'name' and castle_selected.NAME != None and  dict_arguments['dict_bought_city'][castle_selected.NAME.NAME] == False:
                            name_resource = dict_price_city[castle_selected.NAME.NAME]
                            list_text_cost = name_resource.split(';')
                            for resource in list_text_cost:
                                resource = resource.split('/')
                                if dict_arguments['resources_dict'][resource[0]] < int(resource[1]):
                                   dict_arguments ['flag_not_enough_resource'] = 0
                            if dict_arguments ['flag_not_enough_resource'] == 30:
                                name_build = list_buildings_castle[list_buildings_castle.index(castle_selected.NAME)].path
                                list_buildings_castle[list_buildings_castle.index(castle_selected.NAME)].path = name_build.split('_locked')[0]+'.png'
                                list_buildings_castle[list_buildings_castle.index(castle_selected.NAME)].image_load()
                                dict_arguments['dict_bought_city'][castle_selected.NAME.NAME] = True
                                for resource in list_text_cost:
                                    resource = resource.split('/')
                                    dict_arguments['resources_dict'][resource[0]] -= int(resource[1])
                                castle_selected.NAME = None 
                        if castle_selected.NAME != 'name' and castle_selected.NAME != None and dict_arguments['dict_bought_city'][castle_selected.NAME.NAME]:
                            dict_arguments['flag_build_alredy_bought'] = 0  
                        

                            
                else:
                    button_build.path = 'images/button_build_b.png'
                    button_build.image_load()
                if check_mouse_cor(button_castle_back,mouse_cor):
                    button_castle_back.path = 'images/menu_hero_back_b.png'
                    button_castle_back.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        dict_arguments['scene'] = 'city'
                else:
                    button_castle_back.path = 'images/menu_hero_back_y.png'
                    button_castle_back.image_load()
                for obj in list_buildings_castle:
                    if check_mouse_cor(obj,mouse_cor) and obj.path != None:
                        # print(obj.path.split('/')[-1])
                        if not '_locked' in obj.path:
                            name_build = obj.path.split('/')[-1]
                            name_build = name_build.split('\\')[-1]
                            desc_buildings_city.path = 'images/city/desc/desc_'+name_build
                            desc_buildings_city.image_load()
                            break
                        if '_locked' in obj.path:
                            name_build = obj.path.split('/')[-1]
                            name_build = name_build.split('\\')[-1]
                            name_build = name_build.split('_')[0]
                            desc_buildings_city.path = 'images/city/desc/desc_'+name_build+'.png'
                            desc_buildings_city.image_load()

                            break
                    else:
                        desc_buildings_city.path = None
                    
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for obj in list_buildings_castle:
                        not_locked = (list_buildings_castle[0] == list_buildings_castle[list_buildings_castle.index(obj)] or not 'locked' in list_buildings_castle[list_buildings_castle.index(obj)-1].path)
                        locked = ( not (list_buildings_castle[0] == list_buildings_castle[list_buildings_castle.index(obj)]) and 'locked' in list_buildings_castle[list_buildings_castle.index(obj)-1].path)
                        if check_mouse_cor(obj,mouse_cor) and not_locked :
                            castle_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                            castle_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                            castle_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                            castle_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                            castle_selected.NAME = obj
                            castle_selected.image_load()
                        if check_mouse_cor(obj,mouse_cor) and locked:
                            dict_arguments['flag_buy_previous_build'] = 0
                        
            if dict_arguments['scene'] == 'altar':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if check_mouse_cor(button_altar_back,mouse_cor):
                        dict_arguments['scene'] = 'city'
                        altar_selected.NAME = None
                    for obj in list_card_altar:
                        if check_mouse_cor(obj,mouse_cor) and obj.path != None:
                            altar_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                            altar_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                            altar_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                            altar_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                            altar_selected.NAME = obj
                            altar_selected.image_load()
                    if check_mouse_cor(button_change_card,mouse_cor) and altar_selected.NAME != None and altar_selected.NAME.path != None and altar_selected.NAME.path != 'name':
                        name_card = dict_card_price[altar_selected.NAME.path.split('/')[-1].split('.')[0]]
                        list_text_cost = name_card.split(';')
                        for resource in list_text_cost:
                            resource = resource.split('/')
                            if len(resource[0]) != 0:
                                dict_arguments['resources_dict'][resource[0]]+=int(resource[1])
                        list_card_altar[list_card_altar.index(altar_selected.NAME)].path = None
                        if list_card_altar.index(altar_selected.NAME) <=5:
                            list_cards_pl[list_card_altar.index(altar_selected.NAME)][0] = None
                        if list_card_altar.index(altar_selected.NAME) > 5:
                            list_card_pl_reserv[list_card_altar.index(altar_selected.NAME)-6][0] =  None
                        create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
                        altar_selected.NAME = None
                for card in list_cards_pl:
                    if card[0] != None:
                        list_card_altar[list_cards_pl.index(card)].path = 'images/cards/'+card[0]+'.png'
                        list_card_altar[list_cards_pl.index(card)].image_load()
                    if card[0] == None:
                        list_card_altar[list_cards_pl.index(card)].path = None
                for card in list_card_pl_reserv:
                    if card[0] != None:
                        list_card_altar[list_card_pl_reserv.index(card)+6].path = 'images/cards/'+card[0]+'.png'
                        list_card_altar[list_card_pl_reserv.index(card)+6].image_load()
                    if card[0] == None:
                        list_card_altar[list_card_pl_reserv.index(card)+6].path = None
                if check_mouse_cor(button_altar_back,mouse_cor):
                    button_altar_back.path = 'images/menu_hero_back_b.png'
                    button_altar_back.image_load()
                else:
                    button_altar_back.path = 'images/menu_hero_back_y.png'
                    button_altar_back.image_load()
                if check_mouse_cor(button_change_card,mouse_cor):
                    button_change_card.path = 'images/button_change_b.png'
                    button_change_card.image_load()
                else:
                    button_change_card.path = 'images/button_change_y.png'
                    button_change_card.image_load()
                
                
                
                
            if dict_arguments['scene'] == 'camp':
                for i in range(dict_arguments['number_opened_card']) :
                    if 'locked' in list_card_camp[i].path and list_card_camp[i].NAME != 'locked':
                        list_card_camp[i].path = list_card_camp[i].path.split('_locked')[0]+'.png'
                        list_card_camp[i].image_load()
                    
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for obj in list_card_camp:
                        if check_mouse_cor(obj,mouse_cor) and not 'locked' in obj.path :
                            camp_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                            camp_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                            camp_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                            camp_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                            camp_selected.NAME = obj
                            camp_selected.image_load()
                        if check_mouse_cor(obj,mouse_cor) and 'locked' in obj.path and obj.NAME == 'name':
                            dict_arguments['flag_show_error_locked'] = 0 
                        if check_mouse_cor(obj,mouse_cor) and 'locked' in obj.path and obj.NAME != 'name':
                            dict_arguments['flag_show_error_bought_card'] = 0
                    if check_mouse_cor(button_camp_back,mouse_cor):
                        dict_arguments['scene'] = 'city'
                    if check_mouse_cor(button_hire,mouse_cor) and camp_selected.NAME != None:
                        name_card = dict_card_price[camp_selected.NAME.path.split('/')[-1].split('.')[0]]
                        list_text_cost = name_card.split(';')
                        for resource in list_text_cost:
                            resource = resource.split('/')
                            if len(resource[0]) != 0:
                                if dict_arguments['resources_dict'][resource[0]] < int(resource[1]):
                                    dict_arguments ['flag_not_enough_resource'] = 0
                        if dict_arguments ['flag_not_enough_resource'] == 30:
                            for card in list_cards_pl:
                                if card[0] == None:
                                    list_cards_pl[list_cards_pl.index(card)][0] = camp_selected.NAME.path.split('/')[-1].split('.')[0]
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].path = camp_selected.NAME.path.split('.')[0]+'_locked.png'
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].NAME = 'locked'
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].image_load()
                                    for resource in list_text_cost:
                                        resource = resource.split('/')
                                        if len(resource[0]) != 0:
                                            dict_arguments['resources_dict'][resource[0]] -= int(resource[1])
                                    camp_selected.NAME = None
                                    create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
                                    break
                            
                            for card in list_card_pl_reserv:
                                if card[0] == None and camp_selected.NAME != None:
                                    list_card_pl_reserv[list_card_pl_reserv.index(card)][0] = camp_selected.NAME.path.split('/')[-1].split('.')[0]
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].path = camp_selected.NAME.path.split('.')[0]+'_locked.png'
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].NAME = 'locked'
                                    list_card_camp[list_card_camp.index(camp_selected.NAME)].image_load()
                                    for resource in list_text_cost:
                                        resource = resource.split('/')
                                        if len(resource[0]) != 0:
                                            dict_arguments['resources_dict'][resource[0]] -= int(resource[1])
                                    camp_selected.NAME = None
                                    create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
                                    break
                            if camp_selected.NAME != None:
                                dict_arguments['flag_show_error_not_inventory'] = 0
                if check_mouse_cor(button_camp_back,mouse_cor):
                    button_camp_back.path = 'images/menu_hero_back_b.png'
                    button_camp_back.image_load()
                else:
                    button_camp_back.path = 'images/menu_hero_back_y.png'
                    button_camp_back.image_load()
                if check_mouse_cor(button_hire,mouse_cor):
                    button_hire.path = 'images/camp_hire_b.png'
                    button_hire.image_load()
                else:
                    button_hire.path = 'images/camp_hire_r.png'
                    button_hire.image_load()
                        
                        
                                
            
                
            if dict_arguments['scene'] == 'market':
            # if dict_arguments['scene'] == 'sandwich':
                background_market.show_image(win)
                button_market_back.show_image(win)
                #Кнопка назад
                if check_mouse_cor(button_market_back,mouse_cor):
                    button_market_back.path = 'images/menu_hero_back_y.png'
                    button_market_back.image_load()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        dict_arguments['scene'] = 'lvl1'
                        player_lvl1.flag_market = False
                else:
                    button_market_back.path = 'images/menu_hero_back_b.png'
                    button_market_back.image_load()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if check_mouse_cor(button_market_back,mouse_cor): 
                        dict_arguments['scene'] = 'lvl1'
                    for obj in list_slots_market_hero:
                        if dict_arguments['flag_market_selected'] and check_mouse_cor(button_change,mouse_cor) and market_selected.NAME.path != None:
                            if market_selected.NAME.NAME == 'artifact':
                                price_artifact = dict_arguments['dict_price_artifact'][market_selected.NAME.path.split('/')[-1].split('.')[0]]
                                if dict_arguments['resources_dict']['gold_bullion'] < price_artifact and market_selected.NAME in list_slots_market:
                                    dict_arguments['flag_not_enough_gold'] = 0
                                
                                elif dict_arguments['resources_dict']['gold_bullion'] >= price_artifact and market_selected.NAME in list_slots_market:
                                    name_artifact = market_selected.NAME.path.split('/')[-1]
                                    name_artifact = name_artifact.split('.')[0]
                                    name_artifact= name_artifact.split('_')[0]
                                    for artifact in list_all_artifact:
                                        if artifact.path == None:
                                            if artifact.NAME != None:
                                                if name_artifact == artifact.NAME:
                                                    artifact.path = market_selected.NAME.path
                                                    artifact.image_load()
                                                    break
                                            if artifact.NAME == None:
                                                artifact.path = market_selected.NAME.path
                                                artifact.image_load()
                                                break
                                    else:
                                        dict_arguments['flag_market_aritfact_no_slots'] = 0
                                    if dict_arguments['flag_market_aritfact_no_slots'] != 0:
                                        dict_arguments['resources_dict']['gold_bullion'] -= price_artifact
                                        list_slots_market[list_slots_market.index(market_selected.NAME)].path = None
                                        dict_arguments['flag_market_selected'] = False
                                elif market_selected.NAME in list_slots_market_hero:
                                    dict_arguments['resources_dict']['gold_bullion'] += price_artifact-5
                                    list_slots_market_hero[list_slots_market_hero.index(market_selected.NAME)].path = None
                                    list_all_artifact[list_slots_market_hero.index(market_selected.NAME)+5].path = None
                                    dict_arguments['flag_market_selected'] = False
                                
                            if market_selected.NAME.NAME == 'resource':
                                name_resource = market_selected.NAME.path.split('/')[-1]
                                name_resource = name_resource.split('.')[0]
                                price_resource = (dict_arguments['dict_price_resource'][market_selected.NAME.path.split('/')[-1].split('.')[0]]).split('_')
                                if dict_arguments['resources_dict']['gold_bullion'] < int(price_resource[0]) and market_selected.NAME in list_slots_market:
                                    dict_arguments['flag_not_enough_gold'] = 0
                                elif dict_arguments['resources_dict']['gold_bullion'] >= int(price_resource[0]) and market_selected.NAME in list_slots_market:
                                    dict_arguments['resources_dict'][name_resource] += int(price_resource[1])
                                    dict_arguments['resources_dict']['gold_bullion'] -= int(price_resource[0])
                                    dict_arguments['dict_count_resource'][name_resource] -= int(price_resource[1])
                                    if dict_arguments['dict_count_resource'][name_resource] <= 0 :
                                        list_slots_market[list_slots_market.index(market_selected.NAME)].path = None
                                    dict_arguments['flag_market_selected'] = False
                                elif market_selected.NAME in list_slots_market_hero and dict_arguments['resources_dict'][name_resource] >= int(price_resource[1]):
                                    dict_arguments['resources_dict'][name_resource] -= int(price_resource[1])
                                    dict_arguments['resources_dict']['gold_bullion'] += int(price_resource[0])
                                    if dict_arguments['resources_dict'][name_resource] <= 0 :
                                        list_slots_market_hero[list_slots_market_hero.index(market_selected.NAME)].path = None
                                    dict_arguments['flag_market_selected'] = False
                                
                        if check_mouse_cor(obj,mouse_cor) and obj.path != None :
                            if obj.NAME == 'resource':
                                name_resource = obj.path.split('/')[-1].split('.')[0]
                                if dict_arguments['resources_dict'][name_resource] > 0:
                                    if obj.path != None:
                                        market_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                                        market_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                                        market_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                                        market_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                                        market_selected.NAME = obj
                                        dict_arguments['flag_market_selected'] = True
                            if obj.NAME == 'artifact':
                                if obj.path != None:
                                    market_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                                    market_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                                    market_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                                    market_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                                    market_selected.NAME = obj
                                    dict_arguments['flag_market_selected'] = True
                    for obj in list_slots_market:
                        if check_mouse_cor(obj,mouse_cor) and obj.path != None :
                            if obj.NAME == 'resource':
                                if obj.path != None:
                                    market_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                                    market_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                                    market_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                                    market_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                                    market_selected.NAME = obj
                                    dict_arguments['flag_market_selected'] = True
                            if obj.NAME == 'artifact':
                                if obj.path != None:
                                    market_selected.X = obj.X-settings['SCREEN_WIDTH']//106.6
                                    market_selected.Y=obj.Y-settings['SCREEN_WIDTH']//106.6
                                    market_selected.WIDTH=obj.WIDTH+settings['SCREEN_WIDTH']//53.3
                                    market_selected.HEIGHT=obj.HEIGHT+settings['SCREEN_WIDTH']//53.3
                                    market_selected.NAME = obj
                                    dict_arguments['flag_market_selected'] = True
                if dict_arguments['flag_market_selected'] and market_selected.NAME  in list_slots_market:
                    market_selected.image_load()
                    market_selected.show_image(win)
                    button_change.show_image(win)
                    if market_selected.NAME.path.split('/')[-1].split('.')[0] in dict_price_artifact.keys():
                        price = str(dict_arguments['dict_price_artifact'][market_selected.NAME.path.split('/')[-1].split('.')[0]])
                        text_price_artifact.font_content = 'Купить за: '+price+' золота'
                    if market_selected.NAME.path.split('/')[-1].split('.')[0] in dict_price_resource.keys():
                        price = (dict_arguments['dict_price_resource'][market_selected.NAME.path.split('/')[-1].split('.')[0]]).split('_')
                        if price[0] != str(1):
                            text_price_artifact.font_content = 'Купить '+price[1] + ' за '+price[0]+' золота'
                        else:
                            text_price_artifact.font_content = 'Купить '+price[1] + ' за '+price[0]+' золото'
                    text_price_artifact.show_text(win)
                if dict_arguments['flag_market_selected'] and market_selected.NAME  in list_slots_market_hero:
                    market_selected.image_load()
                    market_selected.show_image(win)
                    button_change.show_image(win)
                    if market_selected.NAME.path.split('/')[-1].split('.')[0] in dict_price_artifact.keys():
                        price = str(dict_arguments['dict_price_artifact'][market_selected.NAME.path.split('/')[-1].split('.')[0]])
                        text_price_artifact.font_content = 'Продать за: '+str(int(price)-5)+' золота'
                    if market_selected.NAME.path.split('/')[-1].split('.')[0] in dict_price_resource.keys():
                        price = (dict_arguments['dict_price_resource'][market_selected.NAME.path.split('/')[-1].split('.')[0]]).split('_')
                        if price[0] != str(1):
                            text_price_artifact.font_content = 'Продать '+price[1] + ' за '+price[0]+' золота'
                        else:
                            text_price_artifact.font_content = 'Продать '+price[1] + ' за '+price[0]+' золото'
                    text_price_artifact.show_text(win)
                    
                for obj in list_slots_market_hero:
                    
                    if obj.NAME == 'artifact':
                        list_path_artifact_reserv = list()
                        index_obj = list_slots_market_hero.index(obj)
                        for artifact in list_all_artifact:
                            if artifact.NAME == None:
                                list_path_artifact_reserv.append(artifact.path)
                        obj.path = list_path_artifact_reserv[index_obj]
                        if obj.path != None:
                            obj.image_load()
                            obj.show_image(win)
                        if check_mouse_cor(obj,mouse_cor) and obj.path != None:
                            path = obj.path.split('/')[-1]
                            desc_artifact.X = desc_artifact.start_x+settings['SCREEN_WIDTH']//38
                            desc_artifact.Y = 0
                            desc_artifact.path = 'images/artifacts/desc/desc_'+path
                            desc_artifact.image_load()
                            desc_artifact.show_image(win)
                        else:
                            desc_artifact.path = None
                            desc_artifact.X = desc_artifact.start_x
                            desc_artifact.Y = desc_artifact.start_y
                    if obj.NAME == 'resource' and obj.path != None:
                        name_resource = obj.path.split('/')[-1].split('.')[0]
                        if dict_arguments['resources_dict'][name_resource] > 0:
                            obj.show_image(win)
                            text_count = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'green',str(dict_arguments['resources_dict'][name_resource]),obj.X,obj.Y+obj.HEIGHT//1.7)
                            text_count.show_text(win)
                    
                for obj in list_slots_market:
                    if obj.NAME == 'artifact' and obj.path != None:
                        obj.image_load()
                        obj.show_image(win)
                        if check_mouse_cor(obj,mouse_cor) and obj.path != None:
                            path = obj.path.split('/')[-1]
                            desc_artifact.Y = 0
                            desc_artifact.X = desc_artifact.start_x+settings['SCREEN_WIDTH']//38
                            desc_artifact.path = 'images/artifacts/desc/desc_'+path
                            desc_artifact.image_load()
                            desc_artifact.show_image(win)
                        else:
                            desc_artifact.path = None
                            desc_artifact.X = desc_artifact.start_x
                            desc_artifact.Y = desc_artifact.start_y
                    if obj.NAME == 'resource' and obj.path != None:
                        name_resource = obj.path.split('/')[-1].split('.')[0]
                        if dict_arguments['dict_count_resource'][name_resource] > 0:
                            obj.image_load()
                            obj.show_image(win)
                            text_count = Font('images/Font/pixel_font.ttf',settings['SCREEN_WIDTH']//25,'green',str(dict_arguments['dict_count_resource'][name_resource]),obj.X,obj.Y+obj.HEIGHT//1.55)
                            text_count.show_text(win)
                    
                amount_gold_market.font_content = str(dict_arguments['resources_dict']['gold_bullion'])
                amount_gold_market.show_text(win)
                
            if dict_arguments['scene'] == 'castle':
                scene_castle.show_image(win)
                if castle_selected.path != None and castle_selected.NAME != None and castle_selected.NAME != 'name':
                    castle_selected.show_image(win)
                    name_build = castle_selected.NAME.NAME
                    list_text_cost = dict_price_city[name_build].split(';')
                    finally_text, text_x = text_cost(list_text_cost,finally_text = 'Купить за:',text_obj=text_cost_buildings,settings=settings)
                    text_cost_buildings.font_x = text_x
                    text_cost_buildings.font_content = str(finally_text)
                    text_cost_buildings.show_text(win)
                button_build.show_image(win)
                button_castle_back.show_image(win)
                for obj in list_buildings_castle:
                    if  obj.path != None:
                        obj.show_image(win)
                if desc_buildings_city.path != None:
                    desc_buildings_city.show_image(win)
                
                
            if dict_arguments['scene'] == 'camp':
                scene_camp.show_image(win)
                text_camp.show_text(win)
                if camp_selected.NAME != None:
                    camp_selected.show_image(win)
                for obj in list_card_camp:
                    obj.show_image(win)
                if button_hire.path != None and camp_selected.NAME != None and camp_selected.path != None and camp_selected.NAME != 'name':
                    name_card = camp_selected.NAME.path.split('/')[-1].split('.')[0]
                    list_text_cost = dict_card_price[name_card].split(';')
                    finally_text, text_x = text_cost(list_text_cost,finally_text = 'Купить за:',text_obj=text_price_card,settings=settings)
                    text_price_card.font_content = finally_text
                    text_price_card.font_x = text_x
                    text_price_card.show_text(win)
                button_hire.show_image(win)
                button_camp_back.show_image(win)

            if dict_arguments['scene'] == 'altar':
                scene_altar.show_image(win)
                if altar_selected.NAME != None:
                    altar_selected.show_image(win)
                button_altar_back.show_image(win)
                button_change_card.show_image(win)
                if button_change_card.path != None and altar_selected.NAME != None and altar_selected.NAME != 'name' and altar_selected.NAME.path != None:
                    name_card = dict_card_price[altar_selected.NAME.path.split('/')[-1].split('.')[0]]
                    list_text_cost = name_card.split(';')
                    finally_text,text_x = text_cost(list_text_cost,finally_text='Продать за:',text_obj=text_change_card,settings=settings)
                    text_change_card.font_content = finally_text
                    text_change_card.font_x = text_x
                    text_change_card.show_text(win)
                for obj in list_card_altar:
                    if obj.path != None:
                        obj.show_image(win)
                

            if dict_arguments['scene'] == 'city':
                city_scene.show_image(win)
                button_post_army.show_image(win)
                button_city_back.show_image(win)
                castle.show_image(win)
                if dict_arguments['dict_bought_city']['camp']:
                    camp.show_image(win)
                if dict_arguments['dict_bought_city']['church']:
                    church.show_image(win)
                if dict_arguments['dict_bought_city']['altar']:
                    altar.show_image(win)
                if dict_arguments['dict_bought_city']['forge']:
                    forge.show_image(win)
                if dict_arguments['dict_bought_city']['portal_resource']:
                    portal_resource.show_image(win)


            if dict_arguments['scene'] == 'post_army':
                scene_post_army.show_image(win)
                button_city_back.show_image(win)
                for obj in list_cards_post_army:
                    if obj.path != None:
                        obj.show_image(win)

            #Условие Меню Героя
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
                                    change_images(dict_arguments['card_pressed'], sprite)
                                    index_choice_card = list_cards_menu_hero.index(sprite)
                                    index_pressed_card = list_cards_menu_hero.index(dict_arguments['card_pressed'])
                                    if index_choice_card > 5:
                                        if index_pressed_card > 5:
                                            name_card = list_card_pl_reserv[index_pressed_card-6][0]
                                            list_card_pl_reserv[index_pressed_card-6][0] = list_card_pl_reserv[index_choice_card-6][0]
                                            list_card_pl_reserv[index_choice_card-6][0] = name_card
                                        if index_pressed_card <= 5:
                                            name_card = list_cards_pl[index_pressed_card][0]
                                            list_cards_pl[index_pressed_card][0] = list_card_pl_reserv[index_choice_card-6][0]
                                            list_card_pl_reserv[index_choice_card-6][0] = name_card
                                    if index_choice_card <= 5:
                                        if index_pressed_card <= 5:#Армия в армию
                                            name_card = list_cards_pl[index_pressed_card][0]
                                            list_cards_pl[index_pressed_card][0] = list_cards_pl[index_choice_card][0]
                                            list_cards_pl[index_choice_card][0] = name_card

                                        if index_pressed_card > 5:#резерв Армию 
                                            name_card = list_card_pl_reserv[index_pressed_card-6][0]
                                            list_card_pl_reserv[index_pressed_card-6][0] = list_cards_pl[index_choice_card][0]
                                            list_cards_pl[index_choice_card][0] = name_card
                                    create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
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
                    if check_mouse_cor(obj,mouse_cor) and dict_arguments['card_pressed'] == None and obj.NAME != None and obj.path != None:
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
            if dict_arguments['flag_show_dialog'] == False:
                text_card = None
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
                    elif check_mouse_cor(button_set,mouse_cor):
                        dict_arguments['scene'] = 'settings_scene'
            if dict_arguments['scene'] == 'settings_scene':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if check_mouse_cor(button_menu_hero_back,mouse_cor):
                        dict_arguments['scene'] = 'menu'
                    for obj in list_buttons_display_size:
                        if list_button_display_fullsize[0].font_color != 'red':
                            if check_mouse_cor_font(obj,mouse_cor):
                                for obj2 in  list_buttons_display_size:
                                    obj2.font_color = 'black'
                                obj.font_color = 'red'
                                break
                    for obj in list_button_display_fullsize:
                        if check_mouse_cor_font(obj,mouse_cor):
                            for obj2 in  list_button_display_fullsize:
                                obj2.font_color = 'black'
                            obj.font_color = 'red'
                            break
                    for obj in list_button_auto_save:
                        if check_mouse_cor_font(obj,mouse_cor):
                            for obj2 in  list_button_auto_save:
                                obj2.font_color = 'black'
                            obj.font_color = 'red'
                            break
                    if check_mouse_cor_font(button_save,mouse_cor):
                        with open('saves/settings_display.json','w') as file:
                            for obj in list_buttons_display_size:
                                if obj.font_color == 'red':
                                    width = obj.font_content.split('x')[0]
                                    height = obj.font_content.split('x')[1]
                            if list_button_auto_save[0].font_color == 'red':
                                settings_display['AUTOSAVE'] = "True"
                            if list_button_auto_save[1].font_color == 'red':
                                settings_display['AUTOSAVE'] = "False"
                            if list_button_display_fullsize[0].font_color == 'red':
                                settings_display['FULLSCREEN'] = "True"
                                width = 0
                                height = 0
                            elif list_button_display_fullsize[1].font_color == 'red':
                                settings_display['FULLSCREEN'] = "False"
                            settings_display['SCREEN_WIDTH'] = int(width)
                            settings_display['SCREEN_HEIGHT'] = int(height)
                            settings_display['SOUNDS_VOLUME'] = int(count_volume_sound.font_content)
                            json.dump(settings_display,file,indent=4)
                        dict_arguments['flag_save'] = 0

                            

                    if pygame.Rect.collidepoint(mouse_volume_sound,mouse_cor[0],mouse_cor[1]):
                        dict_arguments['flag_mouse_volume_sound'] = True

                
                if event.type == pygame.MOUSEBUTTONUP:
                    if dict_arguments['flag_mouse_volume_sound']:
                        dict_arguments['flag_mouse_volume_sound'] = False
                
                #Отрисовуем кнопки
            if dict_arguments['past_lvl_skill_fight'] == 3:
                dict_arguments['past_lvl_skill_fight'] = 0 
                for key in dict_card_characteristics.keys():
                    dict_card_characteristics[key][0]+=1
                    dict_card_characteristics[key][1]+=1

            if dict_arguments['scene'] =='card_game':
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    if dict_arguments['cardgame_variables']['who_move'] == 'player':
                        dict_arguments['cardgame_variables']['index_picked_card'] = 0
                        #Функция взятия карты в руки
                        take_card(dict_arguments['cardgame_variables'],list_objects_cards_pl,check_mouse_cor,mouse_cor)
                        #Функция приминения скилла  героя
                        activate_hero_skill(dict_arguments['cardgame_variables'],heal_cloud,dmg_img,check_mouse_cor,dict_arguments['cardgame_variables']['hero_skill'],mouse_cor)
                    dict_arguments['cardgame_variables']['card_that_showing_desc'] = None

                #Если отпущена ЛКМ                
                if  event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    #Отвечает за обнаружение цели, которую выбрал игрок, когда отпустил карту или скилл
                    target_searching(dict_arguments['cardgame_variables'],list_objects_cards_en,list_objects_cards_pl,check_mouse_cor,mouse_cor,dict_card_characteristics)
                      
                #Условие движения мыши
                if event.type == pygame.MOUSEMOTION:
                    mousemoution_react(dict_arguments['cardgame_variables'],mouse_cor,list_objects_cards_en,check_mouse_cor,
                    list_objects_cards_pl,desc_skill,heal_cloud,dmg_img)


            if dict_arguments['scene'] == 'lvl1':
                
                #Если нажата левая кнопка мыши
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    #Окно предложения сделки 
                    if dict_arguments['flag_show_offer']:
                        
                        if check_mouse_cor_font(text_offer_yes,mouse_cor):
                            
                            if dict_arguments['resources_dict']['gold_bullion'] >= gold_count_enemy:
                                dict_arguments['flag_dialog_offer_yes'] = True
                                dict_arguments['resources_dict']['gold_bullion']-=gold_count_enemy
                                dict_arguments['flag_show_offer'] = False
                                text_card = 'Заскамил мамонта бб '
                                dict_arguments['count_dialog'] = 0
                                dict_arguments['flag_offer'] = False
                                dict_arguments['flag_show_dialog'] = True

                            elif dict_arguments['resources_dict']['gold_bullion'] < gold_count_enemy:
                                dict_arguments['flag_not_enough_gold'] = 0
                                dict_arguments['flag_show_offer'] = False
                        if check_mouse_cor_font(text_offer_no,mouse_cor):
                            dict_arguments['flag_dialog_offer_no'] = True
                            dict_arguments['flag_show_offer'] = False
                            dict_arguments['flag_offer'] = False
                            dict_arguments['count_dialog'] = 0
                            text_card = 'Чел ты...'
                            dict_arguments['flag_show_dialog'] = True
                    if dict_arguments['flag_show_dialog']:
                        if check_mouse_cor_font(button_leave,mouse_cor) and dict_arguments['count_dialog'] == 50:
                            dict_arguments['flag_show_dialog'] = False
                            player_lvl1.flag_card = False
                            player_lvl1.flag_move = True
                            player_lvl1.near_card = False
                            text_card = None
                        elif check_mouse_cor_font(button_fight,mouse_cor) and dict_arguments['count_dialog'] == 50:
                            dict_arguments['flag_dialog_fight'] = True
                            text_card = 'Кровавая арена смерти'
                            dict_arguments['flag_show_dialog'] = True
                            dict_arguments['count_dialog'] = 0
                        elif check_mouse_cor_font(button_offer,mouse_cor) and dict_arguments['flag_offer'] and dict_arguments['count_dialog'] == 50:
                            dict_arguments['flag_show_offer'] = True
                            player_lvl1.flag_card = False
                            player_lvl1.near_card = False
                            dict_arguments['flag_show_dialog'] = False
                            gold_count_enemy = int(characteristic_dict['lvl'])*randint(4,5)-int(characteristic_dict['lvl_skill_diplomacy'])*randint(3,4)+5
                            text_offer_enemy.font_content = 'Вы хотите подкупить за '+str(gold_count_enemy)+'?'
                        elif check_mouse_cor_font(button_threat,mouse_cor) and dict_arguments['count_dialog'] == 50:
                            
                            chance_base = randint(0,100)
                            chance_diplomaty = 33+int(characteristic_dict['lvl_skill_diplomacy'])*5
                            if chance_diplomaty > 80:
                                chance_diplomaty = 80
                            if chance_base <= chance_diplomaty:
                                dict_arguments['flag_dialog_threat_win'] = True
                                dict_arguments['count_dialog'] = 0
                                text_card = 'Не надо Дядя'
                                dict_arguments['flag_show_dialog'] = True
                            else:
                                dict_arguments['flag_dialog_threat_lose'] = True
                                dict_arguments['count_dialog'] = 0
                                text_card = 'У меня шелли с ультой'
                                dict_arguments['flag_show_dialog'] = True


                    #Если заканчиваем ход
                    if check_mouse_cor(button_end_move,mouse_cor) and (player_lvl1.where_move == None or player_lvl1.count_step == 0) and player_lvl1.flag_move:
                        #Обновляем количество ходов игрока
                        player_lvl1.count_step = characteristic_dict['count_step']
                        player_lvl1.where_move = None
                        dict_arguments['flag_button_end'] = True
                        dict_arguments['flag_show_new_day'] = 0
                        if randint(0,100) <= int(settings['DAILY_EVENT']):
                            dict_arguments['daily_event'] = choice(list_daily_events)
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
                            dict_arguments['resources_dict']['gold_bullion'] += 20
                        dict_arguments['artifact_chest'] = None
                        player_lvl1.flag_draw_chest = False
                        mat_objetcs_lvl1[player_lvl1.chest_cor[0]][player_lvl1.chest_cor[1]] = '0'
                        player_lvl1.flag_move = True
                    if check_mouse_cor(amount_money,mouse_cor) and player_lvl1.flag_draw_chest:
                        dict_arguments['artifact_chest'] = None
                        player_lvl1.flag_draw_chest = False
                        if player_lvl1.chest_cor != None:
                            mat_objetcs_lvl1[player_lvl1.chest_cor[0]][player_lvl1.chest_cor[1]] = '0'
                        player_lvl1.flag_move = True
                        dict_arguments['resources_dict']['gold_bullion'] += 20
                    for obj in list_choice_base_skill:
                        if check_mouse_cor(obj,mouse_cor) and dict_arguments['flag_use_royal_academy'] and player_lvl1.flag_academy:
                            name_skill = obj.path.split('/')[-1]
                            name_skill = name_skill.split('.')[0]
                            characteristic_dict['lvl_'+name_skill]+=1
                            if name_skill == 'skill_fight':
                                dict_arguments['past_lvl_skill_fight']+=1
                            player_lvl1.flag_move = True
                            dict_arguments['flag_use_royal_academy'] = False
                            player_lvl1.flag_academy = False
                            player_lvl1.near_academy = False
                            
                    for obj in list_choice_base_skill:
                        if check_mouse_cor(obj,mouse_cor) and characteristic_dict['exp']>=dict_arguments['max_exp_lvl']:
                            name_skill = obj.path.split('/')[-1]
                            name_skill = name_skill.split('.')[0]
                            characteristic_dict['lvl_'+name_skill]+=1
                            if name_skill == 'skill_fight':
                                dict_arguments['past_lvl_skill_fight']+=1
                            player_lvl1.flag_move = True
                            characteristic_dict['exp'] -=dict_arguments['max_exp_lvl']
                            characteristic_dict['lvl']+=1
                            dict_arguments['max_exp_lvl']+=100
                            text_new_lvl.font_content = ('Поздровляем! У вас новый уровень;Выберите улучшение способности;'+'Новый уровень - '+str(characteristic_dict['lvl']+1)).split(';')
                            text_lvl_hero.font_content = ('Текущий уровень - '+str(characteristic_dict['lvl'])+';До следующего уровня:').split(';')
                            dict_arguments['flag_new_lvl'] = False
                    
                        
                    #Когда нажали на кнопку "К ГЕРОЮ" 
                    
                    if check_mouse_cor(button_to_hero,mouse_cor):
                        #Перемещаемся к герою 
                        move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
                    if check_mouse_cor(button_to_castle,mouse_cor):
                        move_to_hero(CENTER_CELL_COR,list_cor_castle_xy,list_objects_cells_lvl1,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'])
                    if check_mouse_cor(frame,mouse_cor):
                        dict_arguments['scene'] = 'menu_hero'
                        create_icon_card(settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],list_cards_pl,list_cards_menu_hero,list_card_pl_reserv)
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
                if dict_arguments['flag_show_dialog']:
                    for obj in list_buttons_dialog:
                        if check_mouse_cor_font(obj,mouse_cor):
                            obj.font_color = 'orange'
                            obj.font_size = settings['SCREEN_WIDTH']//16
                        else:
                            obj.font_color = 'black'
                            obj.font_size = settings['SCREEN_WIDTH']//19
                    
        # if dict_arguments['scene'] == 'sandwich':
        if dict_arguments['scene'] == 'settings_scene':
            book.show_image(win)
            button_menu_hero_back.show_image(win)
            button_volume_sound.show_text(win)
            button_display_size.show_text(win)
            pygame.draw.rect(win,color='DimGrey',rect=rect_volume_sound)
            pygame.draw.rect(win,color='black',rect=mouse_volume_sound)
            count_volume_sound.show_text(win)
            if list_button_display_fullsize[0].font_color != 'red':
                button_display_size.font_color = 'black'
                for obj in list_buttons_display_size:
                    obj.show_text(win)
            else:
                button_display_size.font_color = 'DimGrey'
            
            button_display_fullsize.show_text(win)
            for obj in list_button_display_fullsize:
                obj.show_text(win)
            button_auto_save.show_text(win)
            for obj in list_button_auto_save:
                obj.show_text(win)
            button_save.show_text(win)
            if dict_arguments['flag_mouse_volume_sound']:
                if mouse_volume_sound.x >= rect_volume_sound.x and mouse_volume_sound.x <= rect_volume_sound.x+rect_volume_sound.width:
                    mouse_volume_sound.x = mouse_cor[0]
                if mouse_volume_sound.x <= rect_volume_sound.x:
                    mouse_volume_sound.x = rect_volume_sound.x
                if mouse_volume_sound.x >= rect_volume_sound.x+rect_volume_sound.width:
                    mouse_volume_sound.x = rect_volume_sound.x+rect_volume_sound.width
            count_volume = round((mouse_volume_sound.x-rect_volume_sound.x)/rect_volume_sound.width*100)
            count_volume_sound.font_content = str(count_volume)
        if dict_arguments['flag_fight_start']:
            dict_arguments['flag_offer'] = True
            card_number = 0 
            for card in list_cards_pl:
                if card[0] != None:
                    card_number +=1
            if card_number != 0:
                for i in range(dict_arguments['number_opened_card']):
                    dict_arguments['list_cards_en'][i][0] = player_lvl1.flag_card
                cards_arrangement(dict_arguments,list_cards_pl,list_objects_cards_en,list_objects_cards_pl,dict_card_characteristics_enemy,dict_card_characteristics)
                dict_arguments['scene'] = 'card_game'
                player_lvl1.flag_card = False
            if card_number == 0:
                dict_arguments['flag_not_enough_cards'] = 0
                player_lvl1.flag_card = False
                player_lvl1.near_card = False
            dict_arguments['flag_fight_start'] = False
            text_card = None
        if dict_arguments['flag_fight_start_post']  and dict_arguments['scene'] != 'card_game' and dict_arguments['scene'] != 'result_screen':
            card_number = 0 
            for card in list_cards_pl_post_army:
                if card[0] != None:
                    card_number +=1
            if card_number != 0:
                for i in range(dict_arguments['number_opened_card']):
                    dict_arguments['list_cards_en'][i][0] = choice(list(dict_card_characteristics_enemy.keys()))
                cards_arrangement(dict_arguments,list_cards_pl_post_army,list_objects_cards_en,list_objects_cards_pl,dict_card_characteristics_enemy,dict_card_characteristics)
                dict_arguments['scene'] = 'card_game'
            if card_number == 0:
                dict_arguments['game'] = False
                for i in dict_arguments['resources_dict'].keys():
                    if dict_arguments['resources_dict'][i] != 0:
                        dict_arguments['resources_dict'][i] = dict_arguments['resources_dict'][i]/2
        if dict_arguments['scene'] == 'card_game':
            #Алгоритм поочередности ходов игрока и врага
            move_players_algorithm(dict_arguments['cardgame_variables'],list_objects_cards_pl,text_move,list_objects_cards_en,dict_card_characteristics)
            #Отрисовуем все граф. эелементы
            draw_all(bg,dict_arguments['cardgame_variables'],win,text_move,list_objects_cards_pl,list_objects_cards_en,
            stun_img,heal_cloud,dmg_img)
            
            
            #Проверка на то, кто победил 
            count_cards_player = 0
            for c in list_objects_cards_pl:
                if c.path != None:
                    count_cards_player += 1
            if count_cards_player == 0 and dict_arguments['cardgame_variables']['flag_animation_attack'] <= 1:
                dict_arguments['cardgame_variables']['who_won'] = 'enemy'
                dict_arguments['scene'] = 'result_screen'
                
            count_cards_enemy = 0
            for c in list_objects_cards_en:
                if c.path != None:
                    count_cards_enemy += 1

            if count_cards_enemy == 0 and dict_arguments['cardgame_variables']['flag_animation_attack'] <= 1:
                dict_arguments['cardgame_variables']['who_won'] = 'player'
                dict_arguments['scene'] = 'result_screen'
                for c in dict_arguments['list_losed_card_enemy']:
                    dict_arguments['trophy_exp'] += int(dict_card_price[c].split('/')[1].split(';')[0])*15
                    dict_arguments['trophy_gold'] += int(dict_card_price[c].split('/')[1].split(';')[0])//2
            dict_arguments['cardgame_variables']['count_play_sound'] += 1

            #Функция атаки игрока
            player_attack(dict_arguments['cardgame_variables'],list_objects_cards_pl,list_objects_cards_en,flashing_card,
            Font,win,dict_arguments['list_losed_card_enemy'],dict_card_characteristics,dict_arguments)
            # Функция атаки врагаs
            enemy_attack(dict_arguments['cardgame_variables'],flashing_card,dict_arguments['list_losed_card_pl'],show_all_windows,win=win,dict_card_characteristics=dict_card_characteristics)
        elif dict_arguments['scene'] == 'result_screen':
            # pygame.mixer.music.stop()
            #Функция для показа экрана результата
            show_result_screen(win,bg_win,music_win,bg_lose,music_lose,card_for_result_screen,settings['SCREEN_WIDTH'],settings['SCREEN_HEIGHT'],
            dict_arguments['list_losed_card_enemy'],dict_arguments['list_losed_card_pl'],dict_arguments['trophy_exp'],dict_arguments['trophy_gold'],gold_icon,exp_icon,trophy_recourse_text,button_end_fight,
            dict_arguments['cardgame_variables'])
        if dict_arguments['scene'] == 'lvl1':
            #Условие события 
            
            # if player_lvl1.flag_card != None and player_lvl1.flag_card != False and player_lvl1.where_move == None and player_lvl1.flag_move:
            
                

            amount_crystal.font_content = str(dict_arguments['resources_dict']['crystal'])
            amount_food.font_content = str(dict_arguments['resources_dict']['food'])
            amount_iron.font_content = str(dict_arguments['resources_dict']['iron_bullion'])
            amount_gold.font_content = str(dict_arguments['resources_dict']['gold_bullion'])
            amount_gold_market.font_content = str(dict_arguments['resources_dict']['gold_bullion'])
            amount_wood.font_content = str(dict_arguments['resources_dict']['wood'])
            amount_stone.font_content = str(dict_arguments['resources_dict']['stone'])
            win.fill('black')
            # Отрисовуем клетки
            list_xy = [0,0]
            for cell in list_objects_cells_lvl1:
                if check_rect_cell(cell=cell,rect=win_rect):
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
            player_lvl1.blind_move(index=int(settings['INDEX_FOG'])+dict_arguments['index_fog'],flag_player=[0,0,True])
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
                        shack=shack,royal_academy=royal_academy,tavern=tavern,market=market,castle=city,list_cor_castle_xy=list_cor_castle_xy,
                        dvorf=dvorf,klaus=klaus,bard=bard,golem=golem,giant=giant,yamy=yamy,ork=ork,bomb_man=bomb_man,crossbowman=crossbowman,druid=druid,centaur=centaur,ludorn=ludorn,roggy=roggy,surtur=surtur,
                        fountain_mana_empty=fountain_mana_empty,fountain_exp_empty=fountain_exp_empty,mountain=mountain,water=water,list_forest=list_forest,win_rect=win_rect)
            fog_war_func(mat_objetcs_lvl1,X_FRAME_MM,Y_FRAME_MM,player_lvl1.list_studied_map,fog_war,list_objects_cells_lvl1,win,dict_arguments['list_cells_MM'],LENGTH_MAP_LVL1,W_CELL_MINI_MAP,H_CELL_MINI_MAP)
            if dict_arguments['flag_show_dialog']:
                if text_card == None:
                    text_card = dict_card_dialog[player_lvl1.flag_card]
                dialog_book.show_image(win)
                for obj in list_buttons_dialog:
                    obj.show_text(win)
                player_lvl1.flag_move = False
                text_dialog_card.font_content = text_card
                text_dialog_card.show_text(win)
            if dict_arguments['flag_show_offer']:
                frame_error.show_image(win)
                text_offer_enemy.show_text(win)
                text_offer_yes.show_text(win)
                text_offer_no.show_text(win)
                

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
            if dict_arguments['number_opened_card'] <=5:
                dict_arguments['number_opened_card'] = characteristic_dict['lvl'] // 3
            if player_lvl1.flag_city:
                dict_arguments['scene'] = 'city'

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
                    dict_arguments['flag_buy_card'] = True
                    dict_arguments['flag_use_tavern'] = True
                    dict_arguments['flag_use_royal_academy'] = True
                    for el in range(len(mat_objetcs_lvl1)):
                        for element in range(len(mat_objetcs_lvl1[el])):
                            if mat_objetcs_lvl1[el][element] == 'e' or  mat_objetcs_lvl1[el][element] == 'm' or mat_objetcs_lvl1[el][element] == 's':
                                mat_objetcs_lvl1[el][element] = mat_objetcs_lvl1[el][element].upper()

                    for i in range(dict_arguments['number_opened_card']) :
                        if 'locked' in list_card_camp[i].path:
                            list_card_camp[i].path = list_card_camp[i].path.split('_locked')[0]+'.png'
                            list_card_camp[i].image_load()
                            list_card_camp[i].NAME = None
                    #Обновляем цены артефактов
                    dict_arguments['dict_price_artifact'] = {
                                            'boots_fire':randint(20,30),
                                            'boots_hero':randint(30,35),
                                            'boots_ice':randint(20,30),
                                            'chest_fire':randint(30,35),
                                            'chest_ice':randint(30,35),
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
                    #Обновляем цены ресурсов
                    dict_arguments['dict_count_resource'] = {
                                            'wood':20,
                                            'iron_bullion':20,
                                            'stone':20,
                                            'crystal':20,
                                            'food':20,
                                        }
                    #Ресурсы с портала 
                    if dict_arguments['dict_bought_city']['portal_resource']:
                        dict_arguments['resources_dict']['wood'] += randint(8,10)
                        dict_arguments['resources_dict']['crystal'] += randint(1,2)
                        dict_arguments['resources_dict']['iron_bullion'] += randint(4,6)
                        dict_arguments['resources_dict']['stone'] += randint(6,8)
                        dict_arguments['resources_dict']['food'] += randint(10,12)
                        dict_arguments['resources_dict']['gold_bullion'] += randint(2,4)
                    
                    for obj in list_slots_market:
                        if obj.NAME == 'artifact':
                            obj.path = 'images/artifacts/'+choice(list_matrix_artifact)+'.png'
                            obj.image_load()
                if dict_arguments['index_fog'] != 0:
                    dict_arguments['index_fog'] = 0
                if dict_arguments['dict_price_artifact']['boots_fire'] != dict_price_artifact['boots_fire']:
                    dict_arguments['dict_price_artifact'] = dict_price_artifact
                characteristic_dict['day']+=1
                #Ежедновное золото
                if 'skill_idol_people_learn' in list_learn_skills:
                    if randint(0,4) == 4:
                        resources_dict['gold_bullion']+=characteristic_dict['contribution']*characteristic_dict['lvl_skill_domesticpolitics']
                resources_dict['gold_bullion']+=characteristic_dict['contribution']*characteristic_dict['lvl_skill_domesticpolitics']
                text_date.font_content = ('День: '+str(characteristic_dict['day'])+';Неделя: '+str(characteristic_dict['week'])).split(';')
                dict_arguments['flag_button_end'] = False
                for obj in list_all_artifact:
                    if obj.NAME != None and obj.path != None:
                        effect_resource(resources_dict, obj,effect_art_skills_name_dict,characteristic_dict)
                for obj in list_slots_skills_hero:
                    effect_resource(resources_dict, obj,effect_art_skills_name_dict,characteristic_dict)
            #Новый день
            if dict_arguments['flag_show_new_day'] < 100:
                player_lvl1.flag_move = False
                if dict_arguments['flag_show_new_day'] == 0:
                    text_new_day.font_content = ('           Новый день;        Получено за день; ;Яблок - '+str(dict_arguments['resources_dict']['food']-dict_arguments['past_resources_dict']['food'])+'      Золота - '+str(dict_arguments['resources_dict']['gold_bullion']-dict_arguments['past_resources_dict']['gold_bullion'])+'; ;Железа - '+str(dict_arguments['resources_dict']['iron_bullion']-dict_arguments['past_resources_dict']['iron_bullion'])+'      Кристаллов - '+str(dict_arguments['resources_dict']['crystal']-dict_arguments['past_resources_dict']['crystal'])+'; ;Камня - '+str(dict_arguments['resources_dict']['stone']-dict_arguments['past_resources_dict']['stone'])+'      Дерева - '+str(dict_arguments['resources_dict']['wood']-dict_arguments['past_resources_dict']['wood'])).split(';')
                    dict_arguments['past_resources_dict'] = dict_arguments['resources_dict'].copy()
                frame_new_day.show_image(win)        
                text_new_day.show_text(win)
                dict_arguments['flag_show_new_day'] += 1
            if dict_arguments['flag_show_new_day'] == 100:
                player_lvl1.flag_move = True
                dict_arguments['flag_show_new_day'] = 101
            #Условие нового уровня              
            if characteristic_dict['exp'] >= dict_arguments['max_exp_lvl']:
                dict_arguments['flag_new_lvl'] = True
            if  dict_arguments['flag_new_lvl'] and dict_arguments['flag_show_new_day'] >= 100:
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
                text_new_lvl.show_text(win)
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
            if player_lvl1.flag_draw_chest and dict_arguments['flag_show_new_day'] >= 100:
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
            if player_lvl1.flag_fountain_exp and player_lvl1.fountain_exp_cor != None and mat_objetcs_lvl1[player_lvl1.fountain_exp_cor[0]][player_lvl1.fountain_exp_cor[1]] == 'E':
                characteristic_dict['exp']+=exp_fountain
                player_lvl1.flag_fountain_exp = False
                mat_objetcs_lvl1[player_lvl1.fountain_exp_cor[0]][player_lvl1.fountain_exp_cor[1]] = 'e'
                dict_arguments['flag_show_fountain_exp'] = 0
            elif player_lvl1.flag_fountain_mana and player_lvl1.fountain_mana_cor != None and  mat_objetcs_lvl1[player_lvl1.fountain_mana_cor[0]][player_lvl1.fountain_mana_cor[1]] == 'M':
                characteristic_dict['mana']+=mana_fountain*characteristic_dict['change_mana']
                dict_arguments['flag_use_fountain_mana'] = False
                player_lvl1.flag_fountain_mana = False
                dict_arguments['flag_show_fountain_mana'] = 0
                mat_objetcs_lvl1[player_lvl1.fountain_mana_cor[0]][player_lvl1.fountain_mana_cor[1]] = 'm'
            if player_lvl1.flag_tavern  and player_lvl1.flag_draw_chest == False and player_lvl1.flag_tower==False and dict_arguments['flag_use_tavern']:
                player_lvl1.flag_tavern = False
                dict_arguments['flag_button_end'] = False
                dict_arguments['flag_use_tavern'] = False
                random = randint(0,2)
                if random == 0:
                    text_tavern.font_content =( '    Вы выиграли!; 20  золотых в карты. ;Приходите через неделю;').split(';')
                    resources_dict['gold_bullion']+=20
                if random == 1:
                    text_tavern.font_content = ('; Вы ничего не получили. ; Приходите через неделю').split(';')
                if random == 2:
                    if resources_dict['gold_bullion'] <20:
                        if resources_dict['gold_bullion'] == 1:
                            text_tavern.font_content =( '    Вас ограбили!;    На 1 золотую;Приходите через неделю').split(';')
                        else:
                            text_tavern.font_content =( '    Вас ограбили!;    На '+str(resources_dict['gold_bullion'])+' золотых;Приходите через неделю').split(';')
                        resources_dict['gold_bullion'] = 0
                    else:
                        resources_dict['gold_bullion'] -=20
                        text_tavern.font_content =( '    Вас ограбили!;    На 20 золотых;Приходите через неделю').split(';')
                dict_arguments['flag_show_tavern'] = 0
            if player_lvl1.flag_tower:
                player_lvl1.blind_move(index=6,flag_player=[player_lvl1.tower_cor[1],player_lvl1.tower_cor[0],False])
                player_lvl1.flag_tower = False
            if player_lvl1.flag_shack and player_lvl1.shack_cor != None and mat_objetcs_lvl1[player_lvl1.shack_cor[0]][player_lvl1.shack_cor[1]] == 'S':
                characteristic_dict['mana']+=mana_shack*characteristic_dict['change_mana']
                mat_objetcs_lvl1[player_lvl1.shack_cor[0]][player_lvl1.shack_cor[1]] = 's'
                player_lvl1.flag_shack = False
                dict_arguments['flag_show_shack'] = 0
            
            if player_lvl1.flag_shack  and player_lvl1.flag_pressed  and mat_objetcs_lvl1[player_lvl1.shack_cor[0]][player_lvl1.shack_cor[1]] == 's':
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_shack = False
            if player_lvl1.flag_fountain_exp and  player_lvl1.flag_pressed and mat_objetcs_lvl1[player_lvl1.fountain_exp_cor[0]][player_lvl1.fountain_exp_cor[1]] == 'e':
                dict_arguments['flag_show_error_next_week'] = 0
                player_lvl1.flag_fountain_exp = False
            if player_lvl1.flag_fountain_mana and  player_lvl1.flag_pressed and mat_objetcs_lvl1[player_lvl1.fountain_mana_cor[0]][player_lvl1.fountain_mana_cor[1]] == 'm':
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
                elif cor[2] == 'water':
                    water_mm.X = cor[0]
                    water_mm.Y = cor[1]
                    water_mm.show_image(win)
                elif cor[2] == 'forest':
                    forest_mm.X = cor[0]
                    forest_mm.Y = cor[1]
                    forest_mm.show_image(win)
                elif cor[2] == 'mountain':
                    mountain_mm.X = cor[0]
                    mountain_mm.Y = cor[1]
                    mountain_mm.show_image(win)
            #Отображаем кол-во ресурсов на экране
            if dict_arguments['resources_dict']['food'] != 0:
                apple.show_image(win)
                amount_food.show_text(win)
            if dict_arguments['resources_dict']['iron_bullion'] != 0:
                iron_bullion.show_image(win)
                amount_iron.show_text(win)
            if dict_arguments['resources_dict']['gold_bullion'] != 0:
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
            if dict_arguments['daily_event'] != None:
                dict_arguments['count_daily_event'] = 0
                if dict_arguments['daily_event'] == 'goblin':
                    list_resource = list()
                    text_daily_event.font_content = '           Внимание!;На своём пути вы обнаружили ;тело гоблина. ;Обыскав его вы находите:;'
                    text_daily_event.index = 5
                    list_unavailable_resource = []
                    for i in range(randint(1,4)):
                        resource = choice(list(dict_arguments['resources_dict'].keys()))
                        if not resource in list_unavailable_resource:
                            resoruce_count = randint(1,3)
                            list_unavailable_resource.append(resource)

                            dict_arguments['resources_dict'][resource] += resoruce_count
                            list_resource.append(str(str(resource)+'/'+str(resoruce_count)))
                            if i == 2:
                                text_daily_event.font_content+= ';'
                                text_daily_event.index +=1
                    text_daily_event.font_content += text_cost(list_resource,finally_text='',text_obj=text_daily_event,settings=settings)[0]
                    text_daily_event.font_content = text_daily_event.font_content.split(';')
                if dict_arguments['daily_event'] == 'heist':
                    list_resource = list()
                    text_daily_event.font_content = '           Внимание!;Вы прошли по лесу и;вас ограбили разбойники!;Потеряно:'
                    text_daily_event.index = 4
                    list_unavailable_resource = []
                    for i in range(randint(1,4)):
                        resource = choice(list(dict_arguments['resources_dict'].keys()))
                        if not resource in list_unavailable_resource:
                            resoruce_count = randint(1,3)
                            list_unavailable_resource.append(resource)
                            if dict_arguments['resources_dict'][resource] <= resoruce_count:
                                dict_arguments['resources_dict'][resource] = 0
                            else:
                                dict_arguments['resources_dict'][resource] -= resoruce_count
                            list_resource.append(str(str(resource)+'/'+str(resoruce_count)))
                            if i == 2:
                                text_daily_event.font_content+= ';'
                                text_daily_event.index +=1
                    text_daily_event.font_content += text_cost(list_resource,finally_text='',text_obj=text_daily_event,settings=settings)[0]
                    text_daily_event.font_content = text_daily_event.font_content.split(';')
                if dict_arguments['daily_event'] == 'gold':
                    text_daily_event.font_content = '           Внимание!;Прошлой ночью метеорологами был ;зафиксирован золотопад. ;;Шанс найти золото увеличен.'.split(';')
                    text_daily_event.index = 5
                    for i in range(5):
                        while True:
                            random_y = randint(0,LENGTH_MAP_LVL1-1)
                            random_x = randint(0,LENGTH_MAP_LVL1-1)
                            if mat_objetcs_lvl1[random_y][random_x] == '0' and not [random_y,random_x] in list_untochable_cells:
                                mat_objetcs_lvl1[random_y][random_x] = 'g'
                                break
                if dict_arguments['daily_event'] == 'artifact':
                    text_daily_event.font_content = '           Внимание!;;Ходя по лесу, Вы встретили мудреца;; с артефактом.Он передал его вам'.split(';')
                    text_daily_event.index = 5
                    random_artifact = choice(list_matrix_artifact)
                    for obj in list_all_artifact:
                        if obj.path == None:
                            if obj.NAME != None and obj.NAME == random_artifact.split('_')[0]:
                                obj.path = 'images/artifacts/'+str(random_artifact)+'.png'
                                obj.image_load()
                                random_artifact = None
                                break
                            else:
                                obj.path = 'images/artifacts/'+str(random_artifact)+'.png'
                                obj.image_load()
                                random_artifact = None
                                break
                    if random_artifact != None:
                        text_daily_event.font_content = '           Внимание!;;Ходя по лесу, Вы встретили мудреца;;с артефактом.Он передал его вам;;Но Ваш рюкзак был полным.'.split(';')
                        text_daily_event.index = 7
                if dict_arguments['daily_event'] == 'add_army':
                    text_daily_event.font_content = '           Внимание;;К вашему замку пришли путники;;Они просят вступления в вашу армию.;;Вы любезно согласились!'.split(';')
                    text_daily_event.index = 7
                    counter_card = randint(2,3)
                    for i in range(counter_card):
                        flag_append_card = False
                        for card in list_cards_pl:
                            if card[0] == None:
                                list_cards_pl[list_cards_pl.index(card)][0] = choice(list(dict_card_characteristics.keys()))
                                flag_append_card = True
                                counter_card -=1
                                break
                                
                        if not flag_append_card:
                            for card in list_card_pl_reserv:
                                if card[0] == None:
                                    list_card_pl_reserv[list_card_pl_reserv.index(card)][0] = choice(list(dict_card_characteristics.keys()))
                                    flag_append_card = True
                                    counter_card -=1
                                    break
                    if counter_card != 0:
                        text_daily_event.font_content = ('           Внимание;;К вашему замку пришли путники;;Они просят вступления в вашу армию.;;Но для '+str(counter_card)+' не было найдено место').split(';')
                        text_daily_event.index = 7
                        
                if dict_arguments['daily_event'] == 'fog_less':
                    text_daily_event.font_content = '           Внимание!;;На ваши земли надвигается туман!;;Ваш обзор уменьшен!'.split(';')
                    text_daily_event.index = 5
                    dict_arguments['index_fog'] -= 1
                if dict_arguments['daily_event'] == 'fog_more':
                    text_daily_event.font_content = '           Внимание!;;Сегодня будет ясная погода!;;Ваш обзор увеличен'.split(';')
                    text_daily_event.index = 5
                    dict_arguments['index_fog'] += 1
                if dict_arguments['daily_event'] == 'post_fight':
                    text_daily_event.font_content = '           Внимание!;;   На ваш замок напали! ;;Немедленно перейдите к обороне!'.split(';')
                    text_daily_event.index = 5
                    dict_arguments['daily_event'] = None
                    dict_arguments['count_daily_event_post_fight'] = 0
                if dict_arguments['daily_event'] == 'discount':
                    text_daily_event.font_content = '           Внимание!;;Цены артефактов на рынке упали!;;         Скидки от 50%!!!;;Самое время закупится'.split(';')
                    text_daily_event.index = 7
                    for i in dict_price_artifact.keys():
                        dict_price_artifact[i] = dict_price_artifact[i]//2
                
                dict_arguments['daily_event'] = None
            if player_lvl1.flag_card != None and player_lvl1.flag_card != False:
                dict_arguments['flag_show_dialog'] = True
            player_lvl1.move_sprite(mat_objetcs_lvl1, LENGTH_MAP_LVL1,dict_arguments['resources_dict'],recourse_sounds,list_cor_portals=list_cor_portals,
                                    list_card_matrix=list_card_matrix,)
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
        if dict_arguments['flag_market_aritfact_no_slots'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_market_aritfact_no_slots.show_text(win)
            dict_arguments['flag_market_aritfact_no_slots'] +=1
        if dict_arguments['flag_not_enough_gold'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_not_enough_gold.show_text(win)
            dict_arguments['flag_not_enough_gold'] +=1
        if dict_arguments['flag_not_enough_cards'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_not_enough_cards.show_text(win)
            dict_arguments['flag_not_enough_cards'] +=1
        if dict_arguments['flag_show_error_not_inventory'] <50:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_not_inventory.show_text(win)
            dict_arguments['flag_show_error_not_inventory'] +=1
        if dict_arguments['flag_show_shack'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_shack.show_text(win)
            dict_arguments['flag_show_shack'] +=1
        if dict_arguments['flag_show_fountain_mana'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_fountain_mana.show_text(win)
            dict_arguments['flag_show_fountain_mana'] +=1
        if dict_arguments['flag_show_fountain_exp'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_fountain_exp.show_text(win)
            dict_arguments['flag_show_fountain_exp'] +=1
        if dict_arguments['flag_show_error_locked'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_locked_card.show_text(win)
            dict_arguments['flag_show_error_locked'] +=1
        if dict_arguments['flag_show_error_blocked_camp'] <50:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_blocked_camp.show_text(win)
            dict_arguments['flag_show_error_blocked_camp'] +=1
        if dict_arguments['flag_show_error_bought_card'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_bought_card.show_text(win)
            dict_arguments['flag_show_error_bought_card'] +=1
        if dict_arguments['flag_not_enough_resource'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_not_enough_resource.show_text(win)
            dict_arguments['flag_not_enough_resource'] +=1
        if dict_arguments['flag_build_alredy_bought'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_build_alredy_bought.show_text(win)
            dict_arguments['flag_build_alredy_bought'] += 1  
        if dict_arguments['flag_buy_previous_build'] <30:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_buy_previous_build.show_text(win)
            dict_arguments['flag_buy_previous_build'] += 1  
        if dict_arguments['count_daily_event'] <80 and player_lvl1.flag_move and dict_arguments['count_daily_event_post_fight'] == 80:
            generate_error(frame_error=frame_notification,error_text_obj=error_text_obj,error_content=None,win=win)
            text_daily_event.show_text(win)
            dict_arguments['count_daily_event'] += 1  
        if dict_arguments['flag_save'] <50:
            generate_error(frame_error=frame_error,error_text_obj=error_text_obj,error_content=None,win=win)
            text_save.show_text(win)
            dict_arguments['flag_save'] += 1  
        if dict_arguments['count_daily_event_post_fight'] <80 and player_lvl1.flag_move:
            generate_error(frame_error=frame_notification,error_text_obj=error_text_obj,error_content=None,win=win)
            text_daily_event.show_text(win)
            dict_arguments['count_daily_event_post_fight'] += 1  
            if dict_arguments['count_daily_event_post_fight'] == 80:
                dict_arguments['flag_fight_start_post'] = True
        if dict_arguments['count_dialog'] <50:
            for obj in list_buttons_dialog:
                obj.font_content = ''
            dict_arguments['count_dialog']+=1
            if dict_arguments['count_dialog'] == 50:
                if dict_arguments['flag_dialog_offer_yes']:
                    mat_objetcs_lvl1[player_lvl1.card_cor[0]][player_lvl1.card_cor[1]] = '0'
                    player_lvl1.flag_move = True
                    dict_arguments['flag_show_dialog'] = False
                    dict_arguments['flag_dialog_offer_yes'] = False
                if dict_arguments['flag_dialog_offer_no']:
                    dict_arguments['flag_dialog_offer_no'] = False
                if dict_arguments['flag_dialog_threat_win']:
                    player_lvl1.flag_move = True
                    player_lvl1.flag_card = False
                    player_lvl1.near_card = False
                    dict_arguments['flag_show_dialog'] = False
                    mat_objetcs_lvl1[player_lvl1.card_cor[0]][player_lvl1.card_cor[1]] = '0'
                    dict_arguments['flag_dialog_threat_win'] = False
                if dict_arguments['flag_dialog_threat_lose']:
                    dict_arguments['flag_fight_start'] = True
                    dict_arguments['flag_show_dialog'] = False
                    dict_arguments['flag_dialog_threat_lose']=False
                if dict_arguments['flag_dialog_fight']:
                    dict_arguments['flag_fight_start'] = True
                    dict_arguments['flag_show_dialog'] = False
                    dict_arguments['flag_dialog_fight'] = False
                dict_arguments['flag_offer'] = True
                for obj in list_buttons_dialog:
                    obj.font_content = obj.start_content

        dict_arguments['index_water'] +=1
        if dict_arguments['index_water'] % 10 == 0:
            water = choice(list_water)
        time.tick(int(settings['FPS']))
        if index//1.8 >= int(time.get_fps()):
            dict_arguments['minute_in_game'] +=1
            index = 0
        if dict_arguments['minute_in_game'] == 30:
            pass
        index+=1
        #Обновляем экран
        pygame.display.flip()

run_main(dict_arguments)
