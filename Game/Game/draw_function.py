#Для отрисовки всех граф. эелементов
def draw_all(bg,cardgame_variables,win,text_move,list_objects_cards_pl,list_objects_cards_en,
                stun_img,heal_cloud,dmg_img,hero_skill):
    #Отображаем задний фон
    bg.show_image(win)
    # win.fill('white')
    #Отображаем иконку скилла
    if hero_skill.path != None:
        hero_skill.show_image(win)
    # Отображение текста хода
    if  cardgame_variables['count_text_move'] <= 30:
        if cardgame_variables['count_text_move'] > 1:
            text_move.show_text(win)
        cardgame_variables['count_text_move'] += 1
    else:
        if text_move.font_content == 'Твоя карта оглушена':
            cardgame_variables['who_move'] = 'enemy'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Ход врага'
            text_move.font_color = 'yellow'
            list_objects_cards_pl[cardgame_variables['card_that_move_index']].can_move = True
            cardgame_variables['card_that_move_index'] += 1
            cardgame_variables['card_that_move_pl'] = None
        elif text_move.font_content == 'Карта врага оглушена':
            cardgame_variables['who_move'] = 'player'
            cardgame_variables['count_text_move'] = 0
            text_move.font_content ='Твой ход'
            text_move.font_color = 'white'
            list_objects_cards_en[cardgame_variables['index_card_that_move_en']].can_move = True
            cardgame_variables['index_card_that_move_en'] += 1
            cardgame_variables['card_that_move_en'] = None     
    #Отрисовуем карты игрока
    for c in list_objects_cards_pl:
        if c.path != None and c != cardgame_variables['picked_card']:
            c.show_image(win)
            c.show_parametres(win) 
            if c.can_move == False:
                stun_img.X = c.X-  c.WIDTH//6
                stun_img.Y = c.Y  + c.HEIGHT //1.5
                stun_img.show_image(win)
    #Отрисовуем карты противника
    for c in list_objects_cards_en:
        if c.path != None:
            c.show_image(win)
            c.show_parametres(win) 
            if c.can_move == False:
                stun_img.X = c.X - c.WIDTH//6
                stun_img.Y = c.Y  + c.HEIGHT // 1.5
                stun_img.show_image(win)                
    #Отрисовуем взятую в руки игроком карту выше остальных спрайтов
    if cardgame_variables['picked_card']!=None:
        cardgame_variables['picked_card'].show_image(win)
        cardgame_variables['picked_card'].show_parametres(win)
    #Отрисовуем целебное облако и мечь при использовании скиллов
    if cardgame_variables['active_skill'] == 'heal' and cardgame_variables['need_to_show_skill']:
        heal_cloud.show_image(win)
    elif cardgame_variables['active_skill'] == 'damage' and cardgame_variables['need_to_show_skill']:
        dmg_img.show_image(win)