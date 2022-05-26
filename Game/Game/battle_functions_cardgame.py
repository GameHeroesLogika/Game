from random import choice
from random import randint
from objects import*
#
def cards_arrangement(dict_arguments,list_cards_pl,list_objects_cards_en,list_objects_cards_pl,dict_card_characteristics_enemy,dict_card_characteristics):
    #Даем картам игрока начальные параметры
    for i in range(len(dict_arguments['list_cards_en'])):
        if  dict_arguments['list_cards_en'][i][0] != None:
            list_objects_cards_en[i].path = 'images/cards/'+dict_arguments['list_cards_en'][i][0]+'.png'
            list_objects_cards_en[i].DESC_PATH = 'images/cards/desc/desc_' +dict_arguments['list_cards_en'][i][0]+'.png'
            list_objects_cards_en[i].NAME = dict_arguments['list_cards_en'][i][0]
            list_objects_cards_en[i].HP = dict_card_characteristics_enemy[dict_arguments['list_cards_en'][i][0]][0]
            list_objects_cards_en[i].DAMAGE = dict_card_characteristics_enemy[dict_arguments['list_cards_en'][i][0]][1]
            list_objects_cards_en[i].sound_card.path = 'sounds/'+ dict_arguments['list_cards_en'][i][0]+'_sound.wav'
    #Даем картам врага начальные параметры
    for i in range(len(list_cards_pl)):
        if  list_cards_pl[i][0] != None:
            list_objects_cards_pl[i].path = 'images/cards/'+list_cards_pl[i][0]+'.png'
            list_objects_cards_pl[i].DESC_PATH = 'images/cards/desc/desc_' +list_cards_pl[i][0]+'.png'
            list_objects_cards_pl[i].NAME = list_cards_pl[i][0]
            list_objects_cards_pl[i].HP = dict_card_characteristics[list_cards_pl[i][0]][0]
            list_objects_cards_pl[i].DAMAGE = dict_card_characteristics[list_cards_pl[i][0]][1]
            list_objects_cards_pl[i].price = dict_card_characteristics[list_cards_pl[i][0]][2]
            list_objects_cards_pl[i].sound_card.path = 'sounds/'+ list_cards_pl[i][0]+'_sound.wav'
            
#Функция для показа экрана результата
def show_result_screen(win,bg_win,music_win,bg_lose,music_lose,card_for_result_screen,SCREEN_W,SCREEN_H,
list_losed_card_enemy,list_losed_card_pl,trophy_exp,trophy_gold,gold_icon,exp_icon,trophy_recourse_text,button_end_fight,
cardgame_variables):
    #В зависимости от того, кто победил - отображаем соответствующий фон 
    if cardgame_variables['who_won'] == 'player':
        bg_win.show_image(win)
        if cardgame_variables['need_to_play_final_music']:
            music_win.play_sound()
            cardgame_variables['need_to_play_final_music'] = False
    else:
        bg_lose.show_image(win)
        if cardgame_variables['need_to_play_final_music']:
            music_lose.play_sound()
            cardgame_variables['need_to_play_final_music'] = False

    # Отображаем потери игрока и врага
    card_for_result_screen.X = SCREEN_W//12*3.2
    card_for_result_screen.Y = SCREEN_H//4.1
    for name in list_losed_card_enemy:
        card_for_result_screen.path = 'images/cards/'+ name +'.png'
        card_for_result_screen.show_image(win)
        card_for_result_screen.X += (SCREEN_W//12*4.6 - SCREEN_W//12*3.2)
    card_for_result_screen.Y = SCREEN_H//1.8
    card_for_result_screen.X = SCREEN_W//12*3.2
    for name in list_losed_card_pl:
        card_for_result_screen.path = 'images/cards/'+ name +'.png'
        card_for_result_screen.show_image(win)
        card_for_result_screen.X += (SCREEN_W//12*4.6 - SCREEN_W//12*3.2)

    #отображаем награду игрока в случае победы
    if trophy_exp != 0 and trophy_gold != 0:
        trophy_recourse_text.font_content = str(trophy_gold)
        trophy_recourse_text.font_x = gold_icon.X + gold_icon.WIDTH*1.1
        trophy_recourse_text.font_y = gold_icon.Y
        gold_icon.show_image(win)
        trophy_recourse_text.show_text(win)
        trophy_recourse_text.font_content = str(trophy_exp)
        trophy_recourse_text.font_x = exp_icon.X + gold_icon.WIDTH
        trophy_recourse_text.show_text(win)
        exp_icon.show_image(win)
    #Отображаем кнопку завершения боя
    button_end_fight.show_image(win)
  

#Алгоритм поочередности ходов игрока и врага
def move_players_algorithm(cardgame_variables,list_objects_cards_pl,text_move,list_objects_cards_en,dict_card_characteristics):
    # Задаем карту игрока, которая должна ходить
    if cardgame_variables['card_that_move_index'] == 6:
        cardgame_variables['card_that_move_index'] = 0
    if cardgame_variables['card_that_move_pl'] == None and cardgame_variables['who_move'] =='player':
        if list_objects_cards_pl[cardgame_variables['card_that_move_index']].path != None:
            if list_objects_cards_pl[cardgame_variables['card_that_move_index']].can_move != False:
                cardgame_variables['card_that_move_pl'] = list_objects_cards_pl[cardgame_variables['card_that_move_index']]
                list_objects_cards_pl[cardgame_variables['card_that_move_index']].Y = list_objects_cards_pl[cardgame_variables['card_that_move_index']].START_Y - list_objects_cards_pl[cardgame_variables['card_that_move_index']].HEIGHT//4
                list_objects_cards_pl[cardgame_variables['card_that_move_index']].START_Y = list_objects_cards_pl[cardgame_variables['card_that_move_index']].START_Y - list_objects_cards_pl[cardgame_variables['card_that_move_index']].HEIGHT//4
            else:
                cardgame_variables['card_that_move_pl'] ='оглушена'
                cardgame_variables['count_text_move'] = 0
                text_move.font_content ='Твоя карта оглушена'
                text_move.font_color = 'yellow'
                
        else:
            cardgame_variables['card_that_move_index'] += 1
    

    # Задаем карту врага, которая должна ходить
    if cardgame_variables['who_move'] == 'enemy':
        if cardgame_variables['index_card_that_move_en'] == 6:
            cardgame_variables['index_card_that_move_en'] = 0
        if cardgame_variables['card_that_move_en'] == None and cardgame_variables['who_move'] =='enemy':
            if list_objects_cards_en[cardgame_variables['index_card_that_move_en']].path != None:
                if list_objects_cards_en[cardgame_variables['index_card_that_move_en']].can_move != False:
                    cardgame_variables['card_that_move_en'] = list_objects_cards_en[cardgame_variables['index_card_that_move_en']]
                    list_objects_cards_en[cardgame_variables['index_card_that_move_en']].Y = list_objects_cards_en[cardgame_variables['index_card_that_move_en']].START_Y + list_objects_cards_en[cardgame_variables['index_card_that_move_en']].HEIGHT//4
                    list_objects_cards_en[cardgame_variables['index_card_that_move_en']].START_Y = list_objects_cards_en[cardgame_variables['index_card_that_move_en']].START_Y + list_objects_cards_en[cardgame_variables['index_card_that_move_en']].HEIGHT//4
                    list_objects_cards_en[cardgame_variables['index_card_that_move_en']].sound_card.play_sound()
                    # сколько карт на столе у врага
                    cards_on_table_en = 0
                    for i in list_objects_cards_en:
                        if i.path != None:
                            cards_on_table_en += 1
                    # Если ходит карта Клаус - выбираем, какую карту хилить 
                    if cardgame_variables['card_that_move_en'].NAME == 'клаус' and cards_on_table_en > 1:
                        difference_hp = 0
                        
                        for i in list_objects_cards_en:
                            
                            if i.path != None and i != cardgame_variables['card_that_move_en']:
                                if i.HP < dict_card_characteristics[i.NAME][0]:
                                    if dict_card_characteristics[i.NAME][0] - i.HP > difference_hp:
                                        difference_hp =  dict_card_characteristics[i.NAME][0] - i.HP
                                        cardgame_variables['card_victim'] = i
                                        cardgame_variables['card_attacker'] = cardgame_variables['card_that_move_en']
                                        cardgame_variables['is_healing'] = True

                    
                    #Если нужно атаковать карту игрока - выбираем ту, которую можно убить за один удра 
                    if cardgame_variables['card_attacker'] == None:
                        for i in list_objects_cards_pl:
                            if i.path != None:
                                if cardgame_variables['card_that_move_en'].DAMAGE >= i.HP:
                                    cardgame_variables['card_attacker'] =  cardgame_variables['card_that_move_en']
                                    cardgame_variables['card_victim'] = i
                                    break
                    #Если ходит Дворф - выбираем карту, которой нужно прибавить урон 
                    if cardgame_variables['card_that_move_en'].NAME == 'дворф' and cardgame_variables['card_attacker'] == None and cards_on_table_en > 1:
                        cardgame_variables['card_attacker'] = cardgame_variables['card_that_move_en']
                        cardgame_variables['card_victim'] = choice(list_objects_cards_en)
                        cardgame_variables['is_healing'] = True
                        while cardgame_variables['card_victim'].path == None or cardgame_variables['card_victim'] == cardgame_variables['card_attacker']:
                            cardgame_variables['card_victim'] = choice(list_objects_cards_en)

                    #Если нужно атаковать рандомную карту игрока
                    if cardgame_variables['card_attacker'] == None:
                        cardgame_variables['card_attacker'] = cardgame_variables['card_that_move_en']
                        cardgame_variables['card_victim'] = choice(list_objects_cards_pl)
                        while cardgame_variables['card_victim'].path == None:
                            cardgame_variables['card_victim'] = choice(list_objects_cards_pl)

                else:
                    cardgame_variables['card_that_move_en'] ='оглушена'
                    cardgame_variables['count_text_move'] = 0
                    text_move.font_content ='Карта врага оглушена'
                    text_move.font_color = 'white'
                    
            else:
                cardgame_variables['index_card_that_move_en'] += 1


def player_attack(cardgame_variables,list_objects_cards_pl,list_objects_cards_en,flashing_card,
                Font,win,list_losed_card_enemy,dict_card_characteristics,dict_arguments):
    #Прописываем анимацию атаки карты игрока на вражескую карту
    if cardgame_variables['card_attacker'] != None and cardgame_variables['is_healing'] != True and cardgame_variables['who_move'] =='player':
        #Размещаем карту игрока под картой врага
        if cardgame_variables['flag_animation_attack'] == 1:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y + cardgame_variables['card_victim'].HEIGHT + cardgame_variables['card_attacker'].HEIGHT // 6
        #Карта игрока делает "замах"
        elif 5 > cardgame_variables['flag_animation_attack']:
            cardgame_variables['card_attacker'].Y += cardgame_variables['card_attacker'].HEIGHT // 20

        #Карта игрока делает "удар" 
        elif 8 > cardgame_variables['flag_animation_attack']:
            cardgame_variables['card_attacker'].Y -= cardgame_variables['card_attacker'].HEIGHT // 7

        #Карта врага делает "отскок"
        elif cardgame_variables['flag_animation_attack'] == 8:
            sound_hit.play_sound()
            
            # Если атакует подрывник, отскок делают все карты врага
            if cardgame_variables['card_attacker'].NAME == 'подрывник':
                sound_explosion.play_sound()
                for c in list_objects_cards_en:
                    c.Y -= cardgame_variables['card_attacker'].HEIGHT // 7        
            else:
                cardgame_variables['card_victim'].Y -= cardgame_variables['card_attacker'].HEIGHT // 7
            
        #Карты возвращаются на исходное положение
        elif cardgame_variables['flag_animation_attack'] == 9:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y + cardgame_variables['card_victim'].HEIGHT  + cardgame_variables['card_attacker'].HEIGHT // 6
            if cardgame_variables['card_attacker'].NAME == 'ями':
                count_cards_player = 0
                for c in list_objects_cards_pl:
                    if c.path != None:
                        count_cards_player += 1
                if count_cards_player > 1:
                    cardgame_variables['healed_card'] = choice(list_objects_cards_pl)
                    while cardgame_variables['healed_card'] == cardgame_variables['card_attacker'] or cardgame_variables['healed_card'].path == None:
                        cardgame_variables['healed_card'] = choice(list_objects_cards_pl) 
            

            #Количество ХП, которое нужно прибавить союзнику 
            cardgame_variables['hp_for_heal'] = cardgame_variables['card_victim'].HP
            # Если атакует подрывник
            if cardgame_variables['card_attacker'].NAME == 'подрывник':

                #все карты возвращаются назад
                for c in list_objects_cards_en:
                    c.Y += cardgame_variables['card_attacker'].HEIGHT // 7
                    #  Отнимается хп у цели
                    if c == cardgame_variables['card_victim']:
                        cardgame_variables['card_victim'].HP -= cardgame_variables['card_attacker'].DAMAGE
                    # Отнимается хп у остальных карт
                    else:
                        if c.path != None:
                            c.HP -= 1
            else:
                cardgame_variables['card_victim'].Y += cardgame_variables['card_attacker'].HEIGHT // 7
                cardgame_variables['card_victim'].HP -= cardgame_variables['card_attacker'].DAMAGE
                #Если атакует Ями, вычислаем количество ХП, которое нужно прибавить союзнику 
                if cardgame_variables['card_attacker'].NAME == 'ями' and cardgame_variables['healed_card'] != None:
                    if cardgame_variables['card_victim'].HP > 0:
                        cardgame_variables['hp_for_heal'] -= cardgame_variables['card_victim'].HP
                    cardgame_variables['healed_card'].HP += cardgame_variables['hp_for_heal']

                    
        

            
        #Отображаем текст, сколько ХП отнялось у вражеской карты
        elif 25 > cardgame_variables['flag_animation_attack'] > 9:
            
            cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'red','-'+str(cardgame_variables['card_attacker'].DAMAGE),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)   
            
            # Если атакует подрывник, рисуем картинки взрыва на картах 
            if cardgame_variables['card_attacker'].NAME == 'подрывник':
                for c in list_objects_cards_en:
                    if c != cardgame_variables['card_victim'] and c.path != None:
                        cardgame_variables['hp_text'].font_content = '-1'
                        cardgame_variables['hp_text'].font_x = c.X - c.WIDTH // 2.9
                        cardgame_variables['hp_text'].show_text(win)
                for c in list_objects_cards_en:
                    if c.path != None:
                        img_boom.X = c.X
                        img_boom.Y = c.Y  + c.HEIGHT //3  
                        img_boom.show_image(win)
            # Если атакует ями, отображаем анимацию прибавления ХП союзнику
            elif cardgame_variables['card_attacker'].NAME == 'ями' and cardgame_variables['healed_card'] != None:
                cardgame_variables['hp_text'].font_content = '+'+str(cardgame_variables['hp_for_heal'])
                cardgame_variables['hp_text'].font_color = 'green'
                cardgame_variables['hp_text'].font_x = cardgame_variables['healed_card'].X -cardgame_variables['healed_card'].WIDTH // 2.9 
                cardgame_variables['hp_text'].font_y = cardgame_variables['healed_card'].Y+cardgame_variables['healed_card'].HEIGHT-cardgame_variables['healed_card'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['healed_card'])
                if cardgame_variables['flag_animation_attack'] == 10:
                    sound_heal.play_sound()
                
            #Если арбалетчик наносит двойнной урон - отображаем текст 
            elif cardgame_variables['card_attacker'].NAME == 'арбалетчик' and cardgame_variables['double_damage'] == 'Dont reapet':
                cardgame_variables['hp_text'].font_size = cardgame_variables['card_victim'].HEIGHT//7
                cardgame_variables['hp_text'].font_content = 'ДВОЙНОЙ  УРОН'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_attacker'].Y + cardgame_variables['card_attacker'].HEIGHT//1.8
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_attacker'].X - cardgame_variables['card_attacker'].WIDTH*1.5
                cardgame_variables['hp_text'].show_text(win) 
            #Если карта - орк, отображаем текст прибавленого ХП 
            elif cardgame_variables['card_attacker'].NAME == 'орк':
                cardgame_variables['hp_text'].font_content = '+1'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_attacker'].X + cardgame_variables['card_attacker'].WIDTH 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_attacker'].Y+cardgame_variables['card_attacker'].HEIGHT-cardgame_variables['card_attacker'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_attacker'])
                if cardgame_variables['flag_animation_attack'] == 10:
                    cardgame_variables['card_attacker'].DAMAGE += 1
                if cardgame_variables['flag_animation_attack'] == 10:
                    sound_heal.play_sound()
                cardgame_variables['hp_text'].font_content = '-'+str(cardgame_variables['card_attacker'].DAMAGE - 1)
                cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'red','-'+str(cardgame_variables['card_attacker'].DAMAGE - 1),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)   
            cardgame_variables['hp_text'].show_text(win)
            
            

            

        #Если атакует арбалетчик - проверяем, нужно ли ему наносить двойной урон
        elif cardgame_variables['flag_animation_attack'] == 25:
            if cardgame_variables['card_attacker'].NAME == 'арбалетчик':
                if cardgame_variables['double_damage'] !=  'Dont reapet':
                    cardgame_variables['double_damage'] = randint(0,1)
                    if cardgame_variables['card_victim'].HP > 0:
                        if cardgame_variables['double_damage']:
                            cardgame_variables['flag_animation_attack'] = 0
                            cardgame_variables['double_damage'] = 'Dont reapet'
            #Если карта - кентавр, задаем, нужно ли оглушать врага 
            elif cardgame_variables['card_attacker'].NAME == 'кентавр':
                chance_to_stun = randint(1,100)
                if chance_to_stun <= 35:
                    cardgame_variables['card_victim'].can_move = False

        #Конец анимации
        elif cardgame_variables['flag_animation_attack'] == 26:
            #Если карту врага убили - она исчезает
            for c in list_objects_cards_en:
                if c.path != None:
                    if c.HP <= 0:
                        c.path = None
                        list_losed_card_enemy.append(c.NAME)
            #Обновляем все переменные
            cardgame_variables['card_victim'] = None
            cardgame_variables['card_attacker'].X = cardgame_variables['card_attacker'].START_X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_attacker'].START_Y
            cardgame_variables['flag_animation_attack'] = 0
            cardgame_variables['card_attacker'] = None
            cardgame_variables['double_damage'] = None
            cardgame_variables['who_move'] = 'enemy'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Ход врага'
            text_move.font_color = 'yellow'
            cardgame_variables['card_that_move_pl'].Y =  cardgame_variables['card_that_move_pl'].START_Y +  cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'].START_Y = cardgame_variables['card_that_move_pl'].START_Y + cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_index'] += 1
            cardgame_variables['card_that_move_pl'] = None
            cardgame_variables['healed_card'] = None
            cardgame_variables['is_healing'] = False
            
            
        cardgame_variables['flag_animation_attack'] += 1
####################################################################################################
    # Есди происходит лечение
    elif cardgame_variables['card_attacker']!= None and cardgame_variables['is_healing'] and cardgame_variables['who_move'] =='player':
        # Лечебная карта становиться над картой, которую нужно лечить
        if cardgame_variables['flag_animation_attack'] <= 1:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y - cardgame_variables['card_victim'].HEIGHT
            cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'green','+'+str(dict_card_characteristics[cardgame_variables['card_victim'].NAME][0]- cardgame_variables['card_victim'].HP),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)
            
        #Карта игрока делает "замах" 
        elif  cardgame_variables['flag_animation_attack'] < 10 :
            cardgame_variables['card_attacker'].Y -= cardgame_variables['card_attacker'].HEIGHT // 40
            heal_cloud.X = cardgame_variables['card_attacker'].X
            heal_cloud.Y = cardgame_variables['card_attacker'].Y + cardgame_variables['card_attacker'].HEIGHT
            dmg_img.X = cardgame_variables['card_attacker'].X
            dmg_img.Y = cardgame_variables['card_attacker'].Y + cardgame_variables['card_attacker'].HEIGHT
        #Лечебная карта пускает облако
        elif 11 < cardgame_variables['flag_animation_attack'] <= 20:
            if cardgame_variables['card_attacker'].NAME == 'клаус':
                heal_cloud.Y += cardgame_variables['card_attacker'].HEIGHT//20
                heal_cloud.show_image(win)
            elif cardgame_variables['card_attacker'].NAME == 'дворф':
                dmg_img.Y += cardgame_variables['card_attacker'].HEIGHT//20
                dmg_img.show_image(win)
        #Отображаем текст, сколько лечебная карта похилила    
        elif 21< cardgame_variables['flag_animation_attack'] < 37:
            if cardgame_variables['card_attacker'].NAME == 'дворф':
                cardgame_variables['hp_text'].font_content = '+2'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_victim'].X + cardgame_variables['card_victim'].WIDTH 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_victim'])
                if cardgame_variables['flag_animation_attack'] == 22:
                    cardgame_variables['card_victim'].DAMAGE += 2

            else:
                cardgame_variables['hp_text'].show_text(win) 
                cardgame_variables['card_victim'].HP = dict_card_characteristics[cardgame_variables['card_victim'].NAME][0]
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_victim'])

            if cardgame_variables['flag_animation_attack'] == 22:
                    sound_heal.play_sound()
        
        # Конец анимации
        elif cardgame_variables['flag_animation_attack'] == 37:

            #Обнуляем все переменные
            cardgame_variables['card_victim'] = None
            cardgame_variables['card_attacker'].X = cardgame_variables['card_attacker'].START_X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_attacker'].START_Y
            cardgame_variables['flag_animation_attack'] = 0
            cardgame_variables['card_attacker'] = None
            cardgame_variables['is_healing'] = None
            cardgame_variables['who_move'] = 'enemy'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Ход врага'
            text_move.font_color = 'yellow'
            cardgame_variables['card_that_move_pl'].Y =  cardgame_variables['card_that_move_pl'].START_Y +  cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'].START_Y = cardgame_variables['card_that_move_pl'].START_Y + cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_index'] += 1
            cardgame_variables['card_that_move_pl'] = None
            
        cardgame_variables['flag_animation_attack'] += 1

    # print(cardgame_variables['card_attacker'], cardgame_variables['card_victim'])
########################################################################################################
    #Анимация приминения скилла
    if  cardgame_variables['active_skill'] == 'flash_light':
        if cardgame_variables['flag_animation_attack'] <= 1:
            cardgame_variables['card_victim'] = choice(list_objects_cards_en)
            while cardgame_variables['card_victim'].path == None:
                cardgame_variables['card_victim'] = choice(list_objects_cards_en)
            dict_arguments['count_animation'] = 0
            sound_flashlight.play_sound()
        elif 2<cardgame_variables['flag_animation_attack']<16:
            flash_light_image.path = 'images/flashlight/'+str(dict_arguments['count_animation'])+'.png'
            flash_light_image.X = cardgame_variables['card_victim'].X
            flash_light_image.show_image(win)
            if cardgame_variables['flag_animation_attack'] % 2 != 0:
                cardgame_variables['card_victim'].path = None
            else:
                cardgame_variables['card_victim'].path = 'images/cards/'+ cardgame_variables['card_victim'].NAME +'.png'                
        dict_arguments['count_animation'] += 1
        if dict_arguments['count_animation'] == 4:
            dict_arguments['count_animation'] = 0
        cardgame_variables['flag_animation_attack'] += 1
        if cardgame_variables['flag_animation_attack'] == 16:
            list_losed_card_enemy.append(cardgame_variables['card_victim'].NAME)
            cardgame_variables['card_victim'].path = None  
            cardgame_variables['card_victim'] = None
            cardgame_variables['flag_animation_attack'] = 0
            dict_arguments['count_animation'] = 0
            cardgame_variables['active_skill'] = None 
            cardgame_variables['who_move'] = 'enemy'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Ход врага'
            text_move.font_color = 'yellow'
            file_name = cardgame_variables['hero_skill'].path.split('/')[-1]
            file_name = file_name.split('.')[0] + '_bw.png'
            cardgame_variables['hero_skill'].path = 'images/skills_icons/'+file_name
            cardgame_variables['card_that_move_pl'].Y =  cardgame_variables['card_that_move_pl'].START_Y +  cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'].START_Y = cardgame_variables['card_that_move_pl'].START_Y + cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'] = None
# Использование скиллов
################################################################################
    elif (cardgame_variables['active_skill'] == 'heal' or cardgame_variables['active_skill'] == 'damage') and cardgame_variables['card_victim'] != None:
        cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'red','-'+str(cardgame_variables['card_victim'].DAMAGE),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)
        if cardgame_variables['flag_animation_attack'] <= 1:
            sound_heal.play_sound()

        if cardgame_variables['flag_animation_attack'] <= 16:

            flashing_card(cardgame_variables['flag_animation_attack'],cardgame_variables['card_victim'])
            if cardgame_variables['active_skill'] == 'heal':
                cardgame_variables['hp_text'].font_content = '+5'
                cardgame_variables['hp_text'].font_color = 'green'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
            else:
                cardgame_variables['hp_text'].font_content = '+5'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_victim'].X + cardgame_variables['card_victim'].WIDTH 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)


        elif cardgame_variables['flag_animation_attack'] == 17:
            if cardgame_variables['active_skill'] == 'heal':
                cardgame_variables['card_victim'].HP += 5
            else:
                cardgame_variables['card_victim'].DAMAGE += 5
            

        elif cardgame_variables['flag_animation_attack'] == 18: 
            cardgame_variables['card_victim'] = None
            cardgame_variables['flag_animation_attack'] = 0
            cardgame_variables['active_skill'] = None 
            cardgame_variables['who_move'] = 'enemy'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Ход врага'
            text_move.font_color = 'yellow'
            file_name = cardgame_variables['hero_skill'].path.split('/')[-1]
            file_name = file_name.split('.')[0] + '_bw.png'
            cardgame_variables['hero_skill'].path = 'images/skills_icons/'+file_name
            cardgame_variables['card_that_move_pl'].Y =  cardgame_variables['card_that_move_pl'].START_Y +  cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'].START_Y = cardgame_variables['card_that_move_pl'].START_Y + cardgame_variables['card_that_move_pl'].HEIGHT//4
            cardgame_variables['card_that_move_pl'] = None

        cardgame_variables['flag_animation_attack'] += 1













def enemy_attack(cardgame_variables,flashing_card,list_losed_card_pl,show_all_windows,dict_card_characteristics,win):
    if cardgame_variables['who_move'] =='enemy' and cardgame_variables['card_attacker'] != None and cardgame_variables['is_healing'] != True and cardgame_variables['count_text_move'] > 30:
        # Размещаем карту врага над картой игрока
        if cardgame_variables['flag_animation_attack'] == 1:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y - cardgame_variables['card_victim'].HEIGHT - cardgame_variables['card_attacker'].HEIGHT // 6
        #Карта врага делает "замах"
        elif 5 > cardgame_variables['flag_animation_attack']:
            cardgame_variables['card_attacker'].Y -= cardgame_variables['card_attacker'].HEIGHT // 20

        #Карта врага делает "удар" 
        elif 8 > cardgame_variables['flag_animation_attack']:
            cardgame_variables['card_attacker'].Y += cardgame_variables['card_attacker'].HEIGHT // 7

        #Карта игрока делает "отскок"
        elif cardgame_variables['flag_animation_attack'] == 8:
            sound_hit.play_sound()
            
            # Если атакует подрывник, отскок делают все карты игрока
            if cardgame_variables['card_attacker'].NAME == 'подрывник':
                sound_explosion.play_sound()
                for c in list_objects_cards_pl:
                    c.Y += cardgame_variables['card_attacker'].HEIGHT // 7        
            else:
                cardgame_variables['card_victim'].Y += cardgame_variables['card_attacker'].HEIGHT // 7
            
        #Карты возвращаются на исходное положение
        elif cardgame_variables['flag_animation_attack'] == 9:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y - cardgame_variables['card_victim'].HEIGHT  - cardgame_variables['card_attacker'].HEIGHT // 6
            if cardgame_variables['card_attacker'].NAME == 'ями':
                count_cards_enemy = 0
                for c in list_objects_cards_en:
                    if c.path != None:
                        count_cards_enemy += 1
                if count_cards_enemy > 1:
                    cardgame_variables['healed_card'] = choice(list_objects_cards_en)
                    while cardgame_variables['healed_card'] == cardgame_variables['card_attacker'] or cardgame_variables['healed_card'].path == None:
                        cardgame_variables['healed_card'] = choice(list_objects_cards_en) 
            

            #Количество ХП, которое нужно прибавить союзнику 
            cardgame_variables['hp_for_heal'] = cardgame_variables['card_victim'].HP
            # Если атакует подрывник
            if cardgame_variables['card_attacker'].NAME == 'подрывник':

                #все карты возвращаются назад
                for c in list_objects_cards_pl:
                    c.Y -= cardgame_variables['card_attacker'].HEIGHT // 7
                    #  Отнимается хп у цели
                    if c == cardgame_variables['card_victim']:
                        cardgame_variables['card_victim'].HP -= cardgame_variables['card_attacker'].DAMAGE
                    # Отнимается хп у остальных карт
                    else:
                        if c.path != None:
                            c.HP -= 1
            else:
                cardgame_variables['card_victim'].Y -= cardgame_variables['card_attacker'].HEIGHT // 7
                cardgame_variables['card_victim'].HP -= cardgame_variables['card_attacker'].DAMAGE
                #Если атакует Ями, вычислаем количество ХП, которое нужно прибавить союзнику 
                if cardgame_variables['card_attacker'].NAME == 'ями' and cardgame_variables['healed_card'] != None:
                    if cardgame_variables['card_victim'].HP > 0:
                        cardgame_variables['hp_for_heal'] -= cardgame_variables['card_victim'].HP
                    cardgame_variables['healed_card'].HP += cardgame_variables['hp_for_heal']

                
        

        #Отображаем текст, сколько ХП отнялось у вражеской карты
        elif 25 > cardgame_variables['flag_animation_attack'] > 9:
            cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'red','-'+str(cardgame_variables['card_attacker'].DAMAGE),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)
            # Если атакует подрывник, рисуем картинки взрыва на картах 
            if cardgame_variables['card_attacker'].NAME == 'подрывник':
                for c in list_objects_cards_pl:
                    if c != cardgame_variables['card_victim'] and c.path != None:
                        cardgame_variables['hp_text'].font_content = '-1'
                        cardgame_variables['hp_text'].font_x = c.X - c.WIDTH // 2.9
                        cardgame_variables['hp_text'].show_text(win)
                for c in list_objects_cards_pl:
                    if c.path != None:
                        img_boom.X = c.X
                        img_boom.Y = c.Y  + c.HEIGHT //3  
                        img_boom.show_image(win)
            # Если атакует ями, отображаем анимацию прибавления ХП союзнику
            elif cardgame_variables['card_attacker'].NAME == 'ями' and cardgame_variables['healed_card'] != None:
                cardgame_variables['hp_text'].font_content = '+'+str(cardgame_variables['hp_for_heal'])
                cardgame_variables['hp_text'].font_color = 'green'
                cardgame_variables['hp_text'].font_x = cardgame_variables['healed_card'].X -cardgame_variables['healed_card'].WIDTH // 2.9 
                cardgame_variables['hp_text'].font_y = cardgame_variables['healed_card'].Y+cardgame_variables['healed_card'].HEIGHT-cardgame_variables['healed_card'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['healed_card'])
                if cardgame_variables['flag_animation_attack'] == 10:
                    sound_heal.play_sound()
                
            #Если арбалетчик наносит двойнной урон - отображаем текст 
            elif cardgame_variables['card_attacker'].NAME == 'арбалетчик' and cardgame_variables['double_damage'] == 'Dont reapet':
                cardgame_variables['hp_text'].font_size = cardgame_variables['card_victim'].HEIGHT//7
                cardgame_variables['hp_text'].font_content = 'ДВОЙНОЙ  УРОН'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_attacker'].Y + cardgame_variables['card_attacker'].HEIGHT//1.8
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_attacker'].X - cardgame_variables['card_attacker'].WIDTH*1.5
                cardgame_variables['hp_text'].show_text(win) 
            #Если карта - орк, отображаем текст прибавленого ХП 
            elif cardgame_variables['card_attacker'].NAME == 'орк':
                cardgame_variables['hp_text'].font_content = '+1'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_attacker'].X + cardgame_variables['card_attacker'].WIDTH 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_attacker'].Y+cardgame_variables['card_attacker'].HEIGHT-cardgame_variables['card_attacker'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_attacker'])
                if cardgame_variables['flag_animation_attack'] == 10:
                    cardgame_variables['card_attacker'].DAMAGE += 1
                if cardgame_variables['flag_animation_attack'] == 10:
                    sound_heal.play_sound()
                cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'red','-'+str(cardgame_variables['card_attacker'].DAMAGE - 1),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)   
            cardgame_variables['hp_text'].show_text(win)


        #Если атакует арбалетчик - проверяем, нужно ли ему наносить двойной урон
        elif cardgame_variables['flag_animation_attack'] == 25:
            if cardgame_variables['card_attacker'].NAME == 'арбалетчик':
                if cardgame_variables['double_damage'] !=  'Dont reapet':
                    cardgame_variables['double_damage'] = randint(0,1)
                    if cardgame_variables['card_victim'].HP > 0:
                        if cardgame_variables['double_damage']:
                            cardgame_variables['flag_animation_attack'] = 0
                            cardgame_variables['double_damage'] = 'Dont reapet'
            #Если карта - кентавр, задаем, нужно ли оглушать врага 
            elif cardgame_variables['card_attacker'].NAME == 'кентавр':
                chance_to_stun = randint(1,100)
                if chance_to_stun <= 35:
                    cardgame_variables['card_victim'].can_move = False

        #Конец анимации
        elif cardgame_variables['flag_animation_attack'] == 26:
            #Если карту врага убили - она исчезает
            for c in list_objects_cards_pl:
                
                if c.path != None:
                    if c.HP <= 0:
                        c.path = None
                        list_losed_card_pl.append(c.NAME)
            #Обновляем все переменные
            cardgame_variables['card_victim'] = None
            
            cardgame_variables['card_attacker'].X = cardgame_variables['card_attacker'].START_X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_attacker'].START_Y
            cardgame_variables['flag_animation_attack'] = 0
            cardgame_variables['card_attacker'] = None
            cardgame_variables['double_damage'] = None
            cardgame_variables['who_move'] = 'player'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Твой ход'
            text_move.font_color = 'white'
            cardgame_variables['card_that_move_en'].Y =  cardgame_variables['card_that_move_en'].START_Y -  cardgame_variables['card_that_move_en'].HEIGHT//4
            cardgame_variables['card_that_move_en'].START_Y = cardgame_variables['card_that_move_en'].START_Y -  cardgame_variables['card_that_move_en'].HEIGHT//4
            cardgame_variables['index_card_that_move_en'] += 1
            cardgame_variables['card_that_move_en'] = None
            
            
        cardgame_variables['flag_animation_attack'] += 1

        # Если происходит лечение или прибавление ХП
    elif cardgame_variables['card_attacker']!= None and cardgame_variables['is_healing'] and cardgame_variables['who_move'] =='enemy' and cardgame_variables['count_text_move'] > 30:
        # Лечебная карта становиться под картой, которую нужно лечить
        if cardgame_variables['flag_animation_attack'] <= 1:
            cardgame_variables['card_attacker'].X = cardgame_variables['card_victim'].X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_victim'].Y + cardgame_variables['card_victim'].HEIGHT
            cardgame_variables['hp_text'] = Font('images/Font/pixel_font.ttf', cardgame_variables['card_victim'].HEIGHT//5,'green','+'+str(dict_card_characteristics[cardgame_variables['card_victim'].NAME][0]- cardgame_variables['card_victim'].HP),cardgame_variables['card_victim'].X -cardgame_variables['card_victim'].WIDTH // 2.9 ,cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6)
            
        #Карта  делает "замах" 
        elif  cardgame_variables['flag_animation_attack'] < 10 :
            cardgame_variables['card_attacker'].Y += cardgame_variables['card_attacker'].HEIGHT // 40
            heal_cloud.X = cardgame_variables['card_attacker'].X
            heal_cloud.Y = cardgame_variables['card_attacker'].Y 
            dmg_img.X = cardgame_variables['card_attacker'].X
            dmg_img.Y = cardgame_variables['card_attacker'].Y 
        #Лечебная карта пускает облако
        elif 11 < cardgame_variables['flag_animation_attack'] <= 20:
            if cardgame_variables['card_attacker'].NAME == 'клаус':
                heal_cloud.Y -= cardgame_variables['card_attacker'].HEIGHT//20
                heal_cloud.show_image(win)
            elif cardgame_variables['card_attacker'].NAME == 'дворф':
                dmg_img.Y -= cardgame_variables['card_attacker'].HEIGHT//20
                dmg_img.show_image(win)
        #Отображаем текст, сколько лечебная карта похилила    
        elif 21< cardgame_variables['flag_animation_attack'] < 37:
            if cardgame_variables['card_attacker'].NAME == 'дворф':
                cardgame_variables['hp_text'].font_content = '+2'
                cardgame_variables['hp_text'].font_color = 'yellow'
                cardgame_variables['hp_text'].font_x = cardgame_variables['card_victim'].X + cardgame_variables['card_victim'].WIDTH 
                cardgame_variables['hp_text'].font_y = cardgame_variables['card_victim'].Y+cardgame_variables['card_victim'].HEIGHT-cardgame_variables['card_victim'].HEIGHT//6
                cardgame_variables['hp_text'].show_text(win)
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_victim'])
                if cardgame_variables['flag_animation_attack'] == 22:
                    cardgame_variables['card_victim'].DAMAGE += 2

            else:
                cardgame_variables['hp_text'].show_text(win) 
                cardgame_variables['card_victim'].HP = dict_card_characteristics[cardgame_variables['card_victim'].NAME][0]
                flashing_card(cardgame_variables['flag_animation_attack'], cardgame_variables['card_victim'])

            if cardgame_variables['flag_animation_attack'] == 22:
                    sound_heal.play_sound()
        
        # Конец анимации
        elif cardgame_variables['flag_animation_attack'] == 37:

            #Обнуляем все переменные
            cardgame_variables['card_victim'] = None
            cardgame_variables['card_attacker'].X = cardgame_variables['card_attacker'].START_X
            cardgame_variables['card_attacker'].Y = cardgame_variables['card_attacker'].START_Y
            cardgame_variables['flag_animation_attack'] = 0
            cardgame_variables['card_attacker'] = None
            cardgame_variables['is_healing'] = None
            cardgame_variables['who_move'] = 'player'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Твой ход'
            text_move.font_color = 'white'
            cardgame_variables['card_that_move_en'].Y =  cardgame_variables['card_that_move_en'].START_Y -  cardgame_variables['card_that_move_en'].HEIGHT//4
            cardgame_variables['card_that_move_en'].START_Y = cardgame_variables['card_that_move_en'].START_Y -  cardgame_variables['card_that_move_en'].HEIGHT//4
            cardgame_variables['index_card_that_move_en'] += 1
            cardgame_variables['card_that_move_en'] = None
            
        cardgame_variables['flag_animation_attack'] += 1

    
    #Функция для показа всех всплывающих окон    
    show_all_windows(sound_paper,win,desc_skill, frame_error,error_text_obj,
                cardgame_variables['text_error_content'], cardgame_variables) 
