import pygame


#Функция взятия карты в руки
def take_card(cardgame_variables,list_objects_cards_pl,check_mouse_cor,mouse_cor):
    #Перебираем список объектов карт игрока
    for card in list_objects_cards_pl:
        if card.path != None:
            # Условия взятия карты игроком
            if check_mouse_cor(card, mouse_cor) and cardgame_variables['card_attacker'] == None and card.can_move and cardgame_variables['card_victim'] == None and card == cardgame_variables['card_that_move_pl']:
                cardgame_variables['picked_card'] = card
                card.X = mouse_cor[0] - card.WIDTH // 2
                card.Y = mouse_cor[1] - card.HEIGHT // 2
                if cardgame_variables['count_play_sound'] >= 50:
                    card.sound_card.play_sound()
                    cardgame_variables['count_play_sound'] = 0
                cardgame_variables['flag_show_error'] = 30
                break
            elif card != cardgame_variables['card_that_move_pl'] and check_mouse_cor(card, mouse_cor):
                cardgame_variables['text_error_content']  = 'Сейчас ходит другая карта'
                cardgame_variables['flag_show_error'] = 0
        cardgame_variables['index_picked_card'] +=1

#Функция приминения скилла  героя
def activate_hero_skill(cardgame_variables,heal_cloud,dmg_img,check_mouse_cor,hero_skill,mouse_cor):
    if  hero_skill.path.endswith('bw.png') != True and cardgame_variables['card_attacker'] == None and cardgame_variables['card_that_move_pl'] != 'оглушена':
        if check_mouse_cor(cardgame_variables['hero_skill'], mouse_cor):
            cardgame_variables['active_skill'] = hero_skill.NAME
            if cardgame_variables['active_skill'] == 'heal':
                heal_cloud.X = mouse_cor[0] - heal_cloud.WIDTH // 2
                heal_cloud.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2
                cardgame_variables['need_to_show_skill'] = True
            elif cardgame_variables['active_skill'] == 'damage':
                dmg_img.X = mouse_cor[0] - dmg_img.WIDTH // 2
                dmg_img.Y = mouse_cor[1] - dmg_img.HEIGHT // 2
                cardgame_variables['need_to_show_skill'] = True
#Отвечает за обнаружение цели, которую выбрал игрок, когда отпустил карту или скилл
def target_searching(cardgame_variables,list_objects_cards_en,list_objects_cards_pl,check_mouse_cor,mouse_cor,dict_card_characteristics):
    if cardgame_variables['card_attacker'] == None:
        #Перебираем список объектов вражеских карт
        for en_card in list_objects_cards_en:
            #Если игрок положил свою карту на вражескую 
            if check_mouse_cor(en_card, mouse_cor) and en_card.path != None and cardgame_variables['active_skill']== None:
                cardgame_variables['card_attacker'] = cardgame_variables['picked_card']
                cardgame_variables['card_victim'] = en_card
                break
        # Индекс карты игрока в следующeм цикле
        index_card_pl = 0
        for pl_card in list_objects_cards_pl:
            # Если выбранная карта на карте игрока
            if check_mouse_cor(pl_card, mouse_cor) and pl_card.path != None :
                #Если выбранная карта - лечебный маг
                if cardgame_variables['picked_card'] != None:
                    
                    if (cardgame_variables['picked_card'].NAME == 'клаус' or cardgame_variables['picked_card'].NAME =='дворф') and index_card_pl != cardgame_variables['index_picked_card']: 
                        
                        if pl_card.HP < dict_card_characteristics[pl_card.NAME][0] or cardgame_variables['picked_card'].NAME == 'дворф':
                            cardgame_variables['card_attacker'] = cardgame_variables['picked_card']
                            cardgame_variables['card_victim'] = pl_card
                            cardgame_variables['is_healing'] = True
                            if index_card_pl < cardgame_variables['index_picked_card']:
                                break
                        else:
                            cardgame_variables['flag_show_error'] = 0
                            cardgame_variables['text_error_content'] = 'У карты количество ХП макс.'
            
            index_card_pl += 1
                    
    #Возвращаем на стол взятую в рукт игроком карту, если он отпустил ЛКМ
    if cardgame_variables['card_attacker'] == None and cardgame_variables['picked_card'] != None:    
        cardgame_variables['picked_card'].X = cardgame_variables['picked_card'].START_X
        cardgame_variables['picked_card'].Y = cardgame_variables['picked_card'].START_Y
    cardgame_variables['picked_card'] = None

    if cardgame_variables['active_skill'] == 'heal' or cardgame_variables['active_skill'] =='damage':
        for pl_card in list_objects_cards_pl:
            #Узнаем карту, которую нужно вылечить или увеличить урон способностью героя
            if check_mouse_cor(pl_card, mouse_cor) and pl_card.path != None:
                cardgame_variables['card_victim'] = pl_card
                cardgame_variables['need_to_show_skill'] = False
                break
    if cardgame_variables['card_victim'] == None:
        cardgame_variables['need_to_show_skill'] = False
        cardgame_variables['active_skill'] = None


def mousemoution_react(cardgame_variables,mouse_cor,list_objects_cards_en,check_mouse_cor,list_objects_cards_pl,desc_skill,
    heal_cloud,dmg_img):
    #Двигаем взятую в руки карту вместе с игроком
    if cardgame_variables['picked_card'] != None:
        cardgame_variables['picked_card'].X = mouse_cor[0] - cardgame_variables['picked_card'].WIDTH // 2
        cardgame_variables['picked_card'].Y = mouse_cor[1] - cardgame_variables['picked_card'].HEIGHT // 2
        cardgame_variables['card_that_showing_desc'] = None
        cardgame_variables['flag_show_desc'] = 0

    else:
        #Перебираем список из карт врага
        for c in list_objects_cards_en:
            #Если курсор на карте
            if check_mouse_cor(c, mouse_cor) and c.path != None:
                # Нужно отображать карточку-описание для карты
                cardgame_variables['card_that_showing_desc'] = c
                break
            else:
                cardgame_variables['card_that_showing_desc'] = None
                cardgame_variables['flag_show_desc'] = 0
        if cardgame_variables['card_that_showing_desc'] == None:
            # Перебираем список карт игрока для отображения карточки-описания
            for c in list_objects_cards_pl:
                if check_mouse_cor(c, mouse_cor) and c.path != None:
                    cardgame_variables['card_that_showing_desc'] = c
                    break
                else:
                    cardgame_variables['card_that_showing_desc'] = None

        #Условие отображения описания скилла 
        if check_mouse_cor(cardgame_variables['hero_skill'], mouse_cor):
            desc_skill.path = 'images/skills_icons/desc/' + cardgame_variables['hero_skill'].path.split('/')[-1]
        else:
            desc_skill.path = None
            cardgame_variables['flag_show_desc_skill'] = 0
        

        # Двигаем цеобное облако или мечь при использовании скиллов
        if cardgame_variables['active_skill'] == 'heal':
            heal_cloud.X = mouse_cor[0] - heal_cloud.WIDTH // 2
            heal_cloud.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2
        elif cardgame_variables['active_skill'] == 'damage':
            dmg_img.X = mouse_cor[0] - heal_cloud.WIDTH // 2
            dmg_img.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2