import pygame 
from sounds import*
from Text_card import*
from random import choice, randint
from constants import*
from additional_functions import*
from game_objects import*
pygame.init()

    
def card_game(scene,flag_show_error,fps):
    #Даем картам игрока начальные параметры
    for i in range(len(list_cards_en)):
        if  list_cards_en[i] != None:
            list_objects_cards_en[i].path = 'images/cards/'+list_cards_en[i][0]+'.png'
            list_objects_cards_en[i].DESC_PATH = 'images/cards/desc/desc_' +list_cards_en[i][0]+'.png'
            list_objects_cards_en[i].NAME = list_cards_en[i][0]
            list_objects_cards_en[i].HP = list_cards_en[i][1]
            list_objects_cards_en[i].DAMAGE = list_cards_en[i][2]

            list_objects_cards_en[i].sound_card.path = 'sounds/'+ list_cards_en[i][0]+'_sound.wav'


    #Даем картам врага начальные параметры
    for i in range(len(list_cards_pl)):
        if  list_cards_pl[i] != None:
            list_objects_cards_pl[i].path = 'images/cards/'+list_cards_pl[i][0]+'.png'
            list_objects_cards_pl[i].DESC_PATH = 'images/cards/desc/desc_' +list_cards_pl[i][0]+'.png'
            list_objects_cards_pl[i].NAME = list_cards_pl[i][0]
            list_objects_cards_pl[i].HP = list_cards_pl[i][1]
            list_objects_cards_pl[i].DAMAGE = list_cards_pl[i][2]
            list_cards_on_table_pl.append(list_objects_cards_pl[i])
            list_objects_cards_pl[i].price = default_par_cards[list_cards_pl[i][0]][2]
            list_objects_cards_pl[i].sound_card.path = 'sounds/'+ list_cards_pl[i][0]+'_sound.wav'

  
    healed_card = None
    # list_objects_cards_pl[0].can_move = False
    # Индекс карты, которая должна ходить у врага
    index_card_that_move_en = 0
    #Карта, которая должна ходить у врага
    card_that_move_en = None
    #Означает, кто побдил 
    who_won = None
    # Списки с именами карт, которые потеряли игрок и враг
    list_losed_card_enemy = []
    list_losed_card_pl = []
    # Опыт и золото, которое получил игрок при победе
    trophy_exp = 0
    trophy_gold = 0

    #Карта, которая должна ходить у игрока
    card_that_move_pl = None     
    #Индекс карты игрока, которая должна ходить   
    index_card_that_move_pl = 0
    # Нужно ли отображать целебое облако или мечь, при использовании скилла
    need_to_show_skill = True
    # Счетчик для отображения описания скилла
    flag_show_desc_skill = 0
    #Скилл текущего героя
    hero_skill = flash_light_icon
    #Применяется ли скилл в данный момент
    active_skill = None
    # Флаг для отображения ошибки
    #Контент ошибки 
    #Счетчик для отображения тескта для хода
    count_text_move = 0
    # Объект текста хода
    text_move = Font('images/Font/pixel_font.ttf',60,'white','Твой ход!',SCREEN_W//2.5, SCREEN_H//2.3)
    # Временный счетчик,для хода врага
    count_enemy_move = 0
    #Пременная означает, кто ходит
    who_move ='player'
    #Карта, которую взял игрок
    picked_card = None
    #Атакующия карта и карта-жертва
    card_attacker = None
    card_victim = None
    #Происходи ли сейчас лечение 
    is_healing = False
    #Карта, описание которой нужно показать
    card_that_showing_desc = None
    #Счетчик для отображения описания
    flag_show_desc = 0
    #Счетчик для анимации атаки
    flag_animation_attack = 0
    #Переменная, отвечащаяя за сцену
    #Должна ли атакующая карта делать двойной урон
    double_damage = None
    #Задаем значение ФПС 

    count_play_sound = 50
    #Переменная, отвечающая за игру

    #Главный цикл игры
    while scene == 'game':
        
        for event in pygame.event.get():
            mouse_cor = pygame.mouse.get_pos() 
            #Условие выхода из игры
            if event.type == pygame.QUIT:
                scene = 'lvl1'
                return scene
                break
            if scene == 'result_screen':
                if event.type == pygame.MOUSEMOTION:
                    # Если навелись на кнопку окончания боя
                    if check_mouse_cor(button_end_fight,mouse_cor):
                        button_end_fight.path = 'images/buttons/end_fight_w.png'
                    else:
                        button_end_fight.path = 'images/buttons/end_fight_y.png'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Если нажали на кнопку окончания боя
                    if check_mouse_cor(button_end_fight,mouse_cor):
                        print('Бой закончен!')
            elif scene =='game':
                #Если нажата ЛКМ
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Индекс в списке карт выбраной карты
                    index_picked_card = 0
                    
                    if who_move == 'player':
                        #Перебираем список объектов карт игрока
                        for card in list_objects_cards_pl:
                            if card.path != None:
                                # Условия взятия карты игроком
                                if check_mouse_cor(card, mouse_cor) and card_attacker == None and card.can_move and card_victim == None and card == card_that_move_pl:
                                    picked_card = card
                                    card.X = mouse_cor[0] - card.WIDTH // 2
                                    card.Y = mouse_cor[1] - card.HEIGHT // 2
                                    if count_play_sound >= 50:
                                        card.sound_card.play_sound()
                                        count_play_sound = 0
                                    flag_show_error = 30
                                    break
                                elif card != card_that_move_pl and check_mouse_cor(card, mouse_cor):
                                    text_error_content = 'Сейчас ходит другая карта'
                                    flag_show_error = 0
                            index_picked_card +=1
                        #Условия приминения скилла  героя
                        if  hero_skill.path.endswith('bw.png') != True and card_attacker == None and card_that_move_pl != 'оглушена':
                            if check_mouse_cor(hero_skill, mouse_cor):
                                active_skill = hero_skill.NAME
                                if active_skill == 'heal':
                                    heal_cloud.X = mouse_cor[0] - heal_cloud.WIDTH // 2
                                    heal_cloud.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2
                                    need_to_show_skill = True
                                elif active_skill == 'damage':
                                    dmg_img.X = mouse_cor[0] - dmg_img.WIDTH // 2
                                    dmg_img.Y = mouse_cor[1] - dmg_img.HEIGHT // 2
                                    need_to_show_skill = True

                    card_that_showing_desc = None

                #Если отпущена ЛКМ                
                if  event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if card_attacker == None:
                        #Перебираем список объектов вражеских карт
                        for en_card in list_objects_cards_en:
                            #Если игрок положил свою карту на вражескую 
                            if check_mouse_cor(en_card, mouse_cor) and en_card.path != None:
                                card_attacker = picked_card
                                card_victim = en_card
                                break
                        # Индекс карты игрока в следующим цикле
                        index_card_pl = 0
                        for pl_card in list_objects_cards_pl:
                            # Если выбранная карта на карте игрока
                            if check_mouse_cor(pl_card, mouse_cor) and pl_card.path != None :
                                #Если выбранная карта - лечебный маг
                                if picked_card != None:
                                    if (picked_card.NAME == 'клаус' or picked_card.NAME =='дворф') and index_card_pl != index_picked_card: 
                                        
                                        if pl_card.HP < default_par_cards[pl_card.NAME][0] or picked_card.NAME == 'дворф':
                                            card_attacker = picked_card
                                            card_victim = pl_card
                                            is_healing = True
                                            if index_card_pl < index_picked_card:
                                                break
                                        else:
                                            flag_show_error = 0
                                            text_error_content = 'У карты количество ХП макс.'
                            
                            index_card_pl += 1
                                    
                    #Возвращаем на стол взятую в рукт игроком карту, если он отпустил ЛКМ
                    if card_attacker == None and picked_card != None:    
                        picked_card.X = picked_card.START_X
                        picked_card.Y = picked_card.START_Y
                    picked_card = None

                    if active_skill == 'heal' or active_skill =='damage':
                        for pl_card in list_objects_cards_pl:
                            #Узнаем карту, которую нужно вылечить или увеличить урон способностью героя
                            if check_mouse_cor(pl_card, mouse_cor) and pl_card.path != None:
                                card_victim = pl_card
                                need_to_show_skill = False
                                break
                    if card_victim == None:
                        need_to_show_skill = False
                        active_skill = None

                        
                    
                    

                #Условие движения мыши
                if event.type == pygame.MOUSEMOTION:
                    #Двигаем взятую в руки карту вместе с игроком
                    if picked_card != None:
                        picked_card.X = mouse_cor[0] - card.WIDTH // 2
                        picked_card.Y = mouse_cor[1] - card.HEIGHT // 2
                        card_that_showing_desc = None
                        flag_show_desc = 0

                    else:
                        #Перебираем список из карт врага
                        for c in list_objects_cards_en:
                            #Если курсор на карте
                            if check_mouse_cor(c, mouse_cor) and c.path != None:
                                # Нужно отображать карточку-описание для карты
                                card_that_showing_desc = c
                                break
                            else:
                                card_that_showing_desc = None
                                flag_show_desc = 0
                        if card_that_showing_desc == None:
                            # Перебираем список карт игрока для отображения карточки-описания
                            for c in list_objects_cards_pl:
                                if check_mouse_cor(c, mouse_cor) and c.path != None:
                                    card_that_showing_desc = c
                                    break
                                else:
                                    card_that_showing_desc = None

                        #Условие отображения описания скилла 
                        if check_mouse_cor(hero_skill, mouse_cor):
                            desc_skill.path = 'images/skills_icons/desc/' + hero_skill.path.split('/')[-1]
                        else:
                            desc_skill.path = None
                            flag_show_desc_skill = 0
                        

                        # Двигаем цеобное облако или мечь при использовании скиллов
                        if active_skill == 'heal':
                            heal_cloud.X = mouse_cor[0] - heal_cloud.WIDTH // 2
                            heal_cloud.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2
                        elif active_skill == 'damage':
                            dmg_img.X = mouse_cor[0] - heal_cloud.WIDTH // 2
                            dmg_img.Y = mouse_cor[1] - heal_cloud.HEIGHT // 2
        if scene == 'game':
            
            # Задаем карту игрока, которая должна ходить
            if index_card_that_move_pl == 6:
                index_card_that_move_pl = 0
            if card_that_move_pl == None and who_move =='player':
                if list_objects_cards_pl[index_card_that_move_pl].path != None:
                    if list_objects_cards_pl[index_card_that_move_pl].can_move != False:
                        card_that_move_pl = list_objects_cards_pl[index_card_that_move_pl]
                        list_objects_cards_pl[index_card_that_move_pl].Y = list_objects_cards_pl[index_card_that_move_pl].START_Y - list_objects_cards_pl[index_card_that_move_pl].HEIGHT//4
                        list_objects_cards_pl[index_card_that_move_pl].START_Y = list_objects_cards_pl[index_card_that_move_pl].START_Y - list_objects_cards_pl[index_card_that_move_pl].HEIGHT//4
                    else:
                        card_that_move_pl ='оглушена'
                        count_text_move = 0
                        text_move.font_content ='Твоя карта оглушена'
                        text_move.font_color = 'yellow'
                        
                else:
                    index_card_that_move_pl += 1
         
        
            # Задаем карту врага, которая должна ходить
            if who_move == 'enemy':
                if index_card_that_move_en == 6:
                    index_card_that_move_en = 0
                if card_that_move_en == None and who_move =='enemy':
                    if list_objects_cards_en[index_card_that_move_en].path != None:
                        if list_objects_cards_en[index_card_that_move_en].can_move != False:
                            card_that_move_en = list_objects_cards_en[index_card_that_move_en]
                            list_objects_cards_en[index_card_that_move_en].Y = list_objects_cards_en[index_card_that_move_en].START_Y + list_objects_cards_en[index_card_that_move_en].HEIGHT//4
                            list_objects_cards_en[index_card_that_move_en].START_Y = list_objects_cards_en[index_card_that_move_en].START_Y + list_objects_cards_en[index_card_that_move_en].HEIGHT//4
                            list_objects_cards_en[index_card_that_move_en].sound_card.play_sound()
                            # сколько карт на столе у врага
                            cards_on_table_en = 0
                            for i in list_objects_cards_en:
                                if i.path != None:
                                    cards_on_table_en += 1
                            # Если ходит карта Клаус - выбираем, какую карту хилить 
                            if card_that_move_en.NAME == 'клаус' and cards_on_table_en > 1:
                                difference_hp = 0
                                
                                for i in list_objects_cards_en:
                                    if i.path != None and i != card_that_move_en:
                                        if i.HP < default_par_cards[i.NAME][0]:
                                            if default_par_cards[i.NAME][0] - i.HP > difference_hp:
                                                difference_hp =  default_par_cards[i.NAME][0] - i.HP
                                                card_victim = i
                                                card_attacker = card_that_move_en
                                                is_healing = True

                           
                            #Если нужно атаковать карту игрока - выбираем ту, которую можно убить за один удра 
                            if card_attacker == None:
                                for i in list_cards_on_table_pl:
                                    if card_that_move_en.DAMAGE >= i.HP and i.path != None:
                                        card_attacker =  card_that_move_en
                                        card_victim = i
                                        break
                            #Если ходит Дворф - выбираем карту, которой нужно прибавить урон 
                            if card_that_move_en.NAME == 'дворф' and card_attacker == None and cards_on_table_en > 1:
                                card_attacker = card_that_move_en
                                card_victim = choice(list_objects_cards_en)
                                is_healing = True
                                while card_victim.path == None or card_victim == card_attacker:
                                    card_victim = choice(list_objects_cards_en)

                            #Если нужно атаковать рандомную карту игрока
                            if card_attacker == None:
                                card_attacker = card_that_move_en
                                card_victim = choice(list_objects_cards_pl)
                                while card_victim.path == None:
                                    card_victim = choice(list_objects_cards_pl)

                        else:
                            card_that_move_en ='оглушена'
                            count_text_move = 0
                            text_move.font_content ='Карта врага оглушена'
                            text_move.font_color = 'white'
                            
                    else:
                        index_card_that_move_en += 1

                # count_enemy_move +=1
           
            #Отображаем задний фон
            bg.show_image(win)
            #Отображаем иконку скилла
            hero_skill.show_image(win)

            for c in list_cards_on_table_pl:
                if c.path == None:
                    list_cards_on_table_pl.remove(c)
            
            # Отображение текста хода
            if  count_text_move <= 30:
                if count_text_move > 1:
                    text_move.show_text(win)
                count_text_move += 1
            else:
                if text_move.font_content == 'Твоя карта оглушена':
                    who_move = 'enemy'
                    count_text_move = 0
                    text_move.font_content ='Ход врага'
                    text_move.font_color = 'yellow'
                    list_objects_cards_pl[index_card_that_move_pl].can_move = True
                    index_card_that_move_pl += 1
                    card_that_move_pl = None
                elif text_move.font_content == 'Карта врага оглушена':
                    who_move = 'player'
                    count_text_move = 0
                    text_move.font_content ='Твой ход'
                    text_move.font_color = 'white'
                    list_objects_cards_en[index_card_that_move_en].can_move = True
                    index_card_that_move_en += 1
                    card_that_move_en = None
                    
                   

            #Отрисовуем карты игрока
            for c in list_objects_cards_pl:
                if c.path != None and c != picked_card:
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
            if picked_card!=None:
                picked_card.show_image(win)
                picked_card.show_parametres(win)
            #Отрисовуем целебное облако и мечь при использовании скиллов
            if active_skill == 'heal' and need_to_show_skill:
                heal_cloud.show_image(win)
            elif active_skill == 'damage' and need_to_show_skill:
                dmg_img.show_image(win)
            
            #Проверка на то, кто победил 
            count_cards_player = 0
            for c in list_objects_cards_pl:
                if c.path != None:
                    count_cards_player += 1
            if count_cards_player == 0:
                who_won = 'enemy'
                scene = 'result_screen'
                
            count_cards_enemy = 0
            for c in list_objects_cards_en:
                if c.path != None:
                    count_cards_enemy += 1

            if count_cards_enemy == 0:
                who_won = 'player'
                scene = 'result_screen'
                for c in list_losed_card_enemy:
                    trophy_exp += default_par_cards[c][2]*15
                    trophy_gold += default_par_cards[c][2]//2

            count_play_sound += 1
            

            


           
            #Прописываем анимацию атаки карты игрока на вражескую карту
            if card_attacker != None and is_healing != True and who_move =='player':
                #Размещаем карту игрока под картой врага
                if flag_animation_attack == 1:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y + card_victim.HEIGHT + card_attacker.HEIGHT // 6
                #Карта игрока делает "замах"
                elif 5 > flag_animation_attack:
                    card_attacker.Y += card_attacker.HEIGHT // 20

                #Карта врага делает "отскок"
                elif flag_animation_attack == 8:
                    sound_hit.play_sound()
                    
                    # Если атакует подрывник, отскок делают все карты врага
                    if card_attacker.NAME == 'подрывник':
                        sound_explosion.play_sound()
                        for c in list_objects_cards_en:
                            c.Y -= card_attacker.HEIGHT // 7        
                    else:
                        card_victim.Y -= card_attacker.HEIGHT // 7
                    
                #Карты возвращаются на исходное положение
                elif flag_animation_attack == 9:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y + card_victim.HEIGHT  + card_attacker.HEIGHT // 6
                    if card_attacker.NAME == 'ями':
                        count_cards_player = 0
                        for c in list_objects_cards_pl:
                            if c.path != None:
                                count_cards_player += 1
                        if count_cards_player > 1:
                            healed_card = choice(list_objects_cards_pl)
                            while healed_card == card_attacker or healed_card.path == None:
                                healed_card = choice(list_objects_cards_pl) 
                    

                    #Количество ХП, которое нужно прибавить союзнику 
                    hp_for_heal = card_victim.HP
                    # Если атакует подрывник
                    if card_attacker.NAME == 'подрывник':

                        #все карты возвращаются назад
                        for c in list_objects_cards_en:
                            c.Y += card_attacker.HEIGHT // 7
                            #  Отнимается хп у цели
                            if c == card_victim:
                                card_victim.HP -= card_attacker.DAMAGE
                            # Отнимается хп у остальных карт
                            else:
                                if c.path != None:
                                    c.HP -= 1
                    else:
                        card_victim.Y += card_attacker.HEIGHT // 7
                        card_victim.HP -= card_attacker.DAMAGE
                        #Если атакует Ями, вычислаем количество ХП, которое нужно прибавить союзнику 
                        if card_attacker.NAME == 'ями' and healed_card != None:
                            if card_victim.HP > 0:
                                hp_for_heal -= card_victim.HP
                            healed_card.HP += hp_for_heal

                          
                #Карта игрока делает "удар" 
                elif 8 > flag_animation_attack:
                    card_attacker.Y -= card_attacker.HEIGHT // 7

                   
                #Отображаем текст, сколько ХП отнялось у вражеской карты
                elif 25 > flag_animation_attack > 9:
                    
                    hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'red','-'+str(card_attacker.DAMAGE),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)   
                    
                    # Если атакует подрывник, рисуем картинки взрыва на картах 
                    if card_attacker.NAME == 'подрывник':
                        for c in list_objects_cards_en:
                            if c != card_victim and c.path != None:
                                hp_text.font_content = '-1'
                                hp_text.font_x = c.X - c.WIDTH // 2.9
                                hp_text.show_text(win)
                        for c in list_objects_cards_en:
                            if c.path != None:
                                img_boom.X = c.X
                                img_boom.Y = c.Y  + c.HEIGHT //3  
                                img_boom.show_image(win)
                    # Если атакует ями, отображаем анимацию прибавления ХП союзнику
                    elif card_attacker.NAME == 'ями' and healed_card != None:
                        hp_text.font_content = '+'+str(hp_for_heal)
                        hp_text.font_color = 'green'
                        hp_text.font_x = healed_card.X -healed_card.WIDTH // 2.9 
                        hp_text.font_y = healed_card.Y+healed_card.HEIGHT-healed_card.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, healed_card)
                        if flag_animation_attack == 10:
                            sound_heal.play_sound()
                        
                    #Если арбалетчик наносит двойнной урон - отображаем текст 
                    elif card_attacker.NAME == 'арбалетчик' and double_damage == 'Dont reapet':
                        hp_text.font_size = card_victim.HEIGHT//7
                        hp_text.font_content = 'ДВОЙНОЙ  УРОН'
                        hp_text.font_color = 'yellow'
                        hp_text.font_y = card_attacker.Y + card_attacker.HEIGHT//1.8
                        hp_text.font_x = card_attacker.X - card_attacker.WIDTH*1.5
                        hp_text.show_text(win) 
                    #Если карта - орк, отображаем текст прибавленого ХП 
                    elif card_attacker.NAME == 'орк':
                        hp_text.font_content = '+1'
                        hp_text.font_color = 'yellow'
                        hp_text.font_x = card_attacker.X + card_attacker.WIDTH 
                        hp_text.font_y = card_attacker.Y+card_attacker.HEIGHT-card_attacker.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, card_attacker)
                        if flag_animation_attack == 10:
                            card_attacker.DAMAGE += 1
                        if flag_animation_attack == 10:
                            sound_heal.play_sound()
                        hp_text.font_content = '-'+str(card_attacker.DAMAGE - 1)
                        hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'red','-'+str(card_attacker.DAMAGE - 1),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)   
                    hp_text.show_text(win)
                    
                    

                    

                #Если атакует арбалетчик - проверяем, нужно ли ему наносить двойной урон
                elif flag_animation_attack == 25:
                    if card_attacker.NAME == 'арбалетчик':
                        if double_damage !=  'Dont reapet':
                            double_damage = randint(0,1)
                            if card_victim.HP > 0:
                                if double_damage:
                                    flag_animation_attack = 0
                                    double_damage = 'Dont reapet'
                    #Если карта - кентавр, задаем, нужно ли оглушать врага 
                    elif card_attacker.NAME == 'кентавр':
                        chance_to_stun = randint(1,100)
                        if chance_to_stun <= 35:
                            card_victim.can_move = False

                #Конец анимации
                elif flag_animation_attack == 26:
                    #Если карту врага убили - она исчезает
                    for c in list_objects_cards_en:
                        if c.path != None:
                            if c.HP <= 0:
                                c.path = None
                                list_losed_card_enemy.append(c.NAME)
                    #Обновляем все переменные
                    card_victim = None
                    card_attacker.X = card_attacker.START_X
                    card_attacker.Y = card_attacker.START_Y
                    flag_animation_attack = 0
                    card_attacker = None
                    double_damage = None
                    who_move = 'enemy'
                    count_text_move = 0
                    text_move.font_content ='Ход врага'
                    text_move.font_color = 'yellow'
                    card_that_move_pl.Y =  card_that_move_pl.START_Y +  card_that_move_pl.HEIGHT//4
                    card_that_move_pl.START_Y = card_that_move_pl.START_Y + card_that_move_pl.HEIGHT//4
                    index_card_that_move_pl += 1
                    card_that_move_pl = None
                    healed_card = None
                    
                    
                flag_animation_attack += 1
####################################################################################################
            # Есди происходит лечение
            elif card_attacker!= None and is_healing and who_move =='player':
                # Лечебная карта становиться над картой, которую нужно лечить
                if flag_animation_attack <= 1:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y - card_victim.HEIGHT
                    hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'green','+'+str(default_par_cards[card_victim.NAME][0]- card_victim.HP),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)
                    
                #Карта игрока делает "замах" 
                elif  flag_animation_attack < 10 :
                    card_attacker.Y -= card_attacker.HEIGHT // 40
                    heal_cloud.X = card_attacker.X
                    heal_cloud.Y = card_attacker.Y + card_attacker.HEIGHT
                    dmg_img.X = card_attacker.X
                    dmg_img.Y = card_attacker.Y + card_attacker.HEIGHT
                #Лечебная карта пускает облако
                elif 11 < flag_animation_attack <= 20:
                    if card_attacker.NAME == 'клаус':
                        heal_cloud.Y += card_attacker.HEIGHT//20
                        heal_cloud.show_image(win)
                    elif card_attacker.NAME == 'дворф':
                        dmg_img.Y += card_attacker.HEIGHT//20
                        dmg_img.show_image(win)
                #Отображаем текст, сколько лечебная карта похилила    
                elif 21< flag_animation_attack < 37:
                    if card_attacker.NAME == 'дворф':
                        hp_text.font_content = '+2'
                        hp_text.font_color = 'yellow'
                        hp_text.font_x = card_victim.X + card_victim.WIDTH 
                        hp_text.font_y = card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, card_victim)
                        if flag_animation_attack == 22:
                            card_victim.DAMAGE += 2

                    else:
                        hp_text.show_text(win) 
                        card_victim.HP = default_par_cards[card_victim.NAME][0]
                        flashing_card(flag_animation_attack, card_victim)

                    if flag_animation_attack == 22:
                            sound_heal.play_sound()
                
                # Конец анимации
                elif flag_animation_attack == 37:

                    #Обнуляем все переменные
                    card_victim = None
                    card_attacker.X = card_attacker.START_X
                    card_attacker.Y = card_attacker.START_Y
                    flag_animation_attack = 0
                    card_attacker = None
                    is_healing = None
                    who_move = 'enemy'
                    count_text_move = 0
                    text_move.font_content ='Ход врага'
                    text_move.font_color = 'yellow'
                    card_that_move_pl.Y =  card_that_move_pl.START_Y +  card_that_move_pl.HEIGHT//4
                    card_that_move_pl.START_Y = card_that_move_pl.START_Y + card_that_move_pl.HEIGHT//4
                    index_card_that_move_pl += 1
                    card_that_move_pl = None
                    
                flag_animation_attack += 1

            # print(card_attacker, card_victim)
########################################################################################################
            #Анимация приминения скилла
            if  active_skill == 'flash_light':
                if flag_animation_attack <= 1:
                    card_victim = choice(list_objects_cards_en)
                    while card_victim.path == None:
                        card_victim = choice(list_objects_cards_en)
                    count_animation = 0
                    sound_flashlight.play_sound()
                elif 2<flag_animation_attack<16:
                    flash_light_image.path = 'images/flashlight/'+str(count_animation)+'.png'
                    flash_light_image.X = card_victim.X
                    flash_light_image.show_image(win)
                    if flag_animation_attack % 2 != 0:
                        card_victim.path = None
                    else:
                        card_victim.path = 'images/cards/'+ card_victim.NAME +'.png'                
                count_animation += 1
                if count_animation == 4:
                    count_animation = 0
                flag_animation_attack += 1
                if flag_animation_attack == 16:
                    list_losed_card_enemy.append(card_victim.NAME)
                    card_victim.path = None  
                    card_victim = None
                    flag_animation_attack = 0
                    count_animation = 0
                    active_skill = None 
                    who_move = 'enemy'
                    count_text_move = 0
                    text_move.font_content ='Ход врага'
                    text_move.font_color = 'yellow'
                    file_name = hero_skill.path.split('/')[-1]
                    file_name = file_name.split('.')[0] + '_bw.png'
                    hero_skill.path = 'images/skills_icons/'+file_name
                    card_that_move_pl.Y =  card_that_move_pl.START_Y +  card_that_move_pl.HEIGHT//4
                    card_that_move_pl.START_Y = card_that_move_pl.START_Y + card_that_move_pl.HEIGHT//4
                    card_that_move_pl = None
                    
################################################################################
            elif (active_skill == 'heal' or active_skill == 'damage') and card_victim != None:
                hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'red','-'+str(card_victim.DAMAGE),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)
                if flag_animation_attack <= 1:
                    sound_heal.play_sound()

                if flag_animation_attack <= 16:

                    flashing_card(flag_animation_attack,card_victim)
                    if active_skill == 'heal':
                        hp_text.font_content = '+5'
                        hp_text.font_color = 'green'
                        hp_text.font_x = card_victim.X -card_victim.WIDTH // 2.9 
                        hp_text.font_y = card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6
                        hp_text.show_text(win)
                    else:
                        hp_text.font_content = '+5'
                        hp_text.font_color = 'yellow'
                        hp_text.font_x = card_victim.X + card_victim.WIDTH 
                        hp_text.font_y = card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6
                        hp_text.show_text(win)


                elif flag_animation_attack == 17:
                    if active_skill == 'heal':
                        card_victim.HP += 5
                    else:
                        card_victim.DAMAGE += 5
                    

                elif flag_animation_attack == 18: 
                    card_victim = None
                    flag_animation_attack = 0
                    active_skill = None 
                    who_move = 'enemy'
                    count_text_move = 0
                    text_move.font_content ='Ход врага'
                    text_move.font_color = 'yellow'
                    file_name = hero_skill.path.split('/')[-1]
                    file_name = file_name.split('.')[0] + '_bw.png'
                    hero_skill.path = 'images/skills_icons/'+file_name
                    card_that_move_pl.Y =  card_that_move_pl.START_Y +  card_that_move_pl.HEIGHT//4
                    card_that_move_pl.START_Y = card_that_move_pl.START_Y + card_that_move_pl.HEIGHT//4
                    card_that_move_pl = None

                flag_animation_attack += 1

            ##################################################
            ##################################################
            ##################################################
            ##################################################
            # Анимация атаки врага
            if who_move =='enemy' and card_attacker != None and is_healing != True and count_text_move > 30:
                # Размещаем карту врага над картой игрока
                if flag_animation_attack == 1:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y - card_victim.HEIGHT - card_attacker.HEIGHT // 6
                #Карта врага делает "замах"
                elif 5 > flag_animation_attack:
                    card_attacker.Y -= card_attacker.HEIGHT // 20

                #Карта врага делает "удар" 
                elif 8 > flag_animation_attack:
                    card_attacker.Y += card_attacker.HEIGHT // 7

                #Карта игрока делает "отскок"
                elif flag_animation_attack == 8:
                    sound_hit.play_sound()
                    
                    # Если атакует подрывник, отскок делают все карты игрока
                    if card_attacker.NAME == 'подрывник':
                        sound_explosion.play_sound()
                        for c in list_objects_cards_pl:
                            c.Y += card_attacker.HEIGHT // 7        
                    else:
                        card_victim.Y += card_attacker.HEIGHT // 7
                    
                #Карты возвращаются на исходное положение
                elif flag_animation_attack == 9:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y - card_victim.HEIGHT  - card_attacker.HEIGHT // 6
                    if card_attacker.NAME == 'ями':
                        count_cards_enemy = 0
                        for c in list_objects_cards_en:
                            if c.path != None:
                                count_cards_enemy += 1
                        if count_cards_enemy > 1:
                            healed_card = choice(list_objects_cards_en)
                            while healed_card == card_attacker or healed_card.path == None:
                                healed_card = choice(list_objects_cards_en) 
                    

                    #Количество ХП, которое нужно прибавить союзнику 
                    hp_for_heal = card_victim.HP
                    # Если атакует подрывник
                    if card_attacker.NAME == 'подрывник':

                        #все карты возвращаются назад
                        for c in list_objects_cards_pl:
                            c.Y -= card_attacker.HEIGHT // 7
                            #  Отнимается хп у цели
                            if c == card_victim:
                                card_victim.HP -= card_attacker.DAMAGE
                            # Отнимается хп у остальных карт
                            else:
                                if c.path != None:
                                    c.HP -= 1
                    else:
                        card_victim.Y -= card_attacker.HEIGHT // 7
                        card_victim.HP -= card_attacker.DAMAGE
                        #Если атакует Ями, вычислаем количество ХП, которое нужно прибавить союзнику 
                        if card_attacker.NAME == 'ями' and healed_card != None:
                            if card_victim.HP > 0:
                                hp_for_heal -= card_victim.HP
                            healed_card.HP += hp_for_heal

                        
                

                #Отображаем текст, сколько ХП отнялось у вражеской карты
                elif 25 > flag_animation_attack > 9:
                    hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'red','-'+str(card_attacker.DAMAGE),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)
                    # Если атакует подрывник, рисуем картинки взрыва на картах 
                    if card_attacker.NAME == 'подрывник':
                        for c in list_objects_cards_pl:
                            if c != card_victim and c.path != None:
                                hp_text.font_content = '-1'
                                hp_text.font_x = c.X - c.WIDTH // 2.9
                                hp_text.show_text(win)
                        for c in list_objects_cards_pl:
                            if c.path != None:
                                img_boom.X = c.X
                                img_boom.Y = c.Y  + c.HEIGHT //3  
                                img_boom.show_image(win)
                    # Если атакует ями, отображаем анимацию прибавления ХП союзнику
                    elif card_attacker.NAME == 'ями' and healed_card != None:
                        hp_text.font_content = '+'+str(hp_for_heal)
                        hp_text.font_color = 'green'
                        hp_text.font_x = healed_card.X -healed_card.WIDTH // 2.9 
                        hp_text.font_y = healed_card.Y+healed_card.HEIGHT-healed_card.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, healed_card)
                        if flag_animation_attack == 10:
                            sound_heal.play_sound()
                        
                    #Если арбалетчик наносит двойнной урон - отображаем текст 
                    elif card_attacker.NAME == 'арбалетчик' and double_damage == 'Dont reapet':
                        hp_text.font_size = card_victim.HEIGHT//7
                        hp_text.font_content = 'ДВОЙНОЙ  УРОН'
                        hp_text.font_color = 'yellow'
                        hp_text.font_y = card_attacker.Y + card_attacker.HEIGHT//1.8
                        hp_text.font_x = card_attacker.X - card_attacker.WIDTH*1.5
                        hp_text.show_text(win) 
                    #Если карта - орк, отображаем текст прибавленого ХП 
                    elif card_attacker.NAME == 'орк':
                        hp_text.font_content = '+1'
                        hp_text.font_color = 'yellow'
                        hp_text.font_x = card_attacker.X + card_attacker.WIDTH 
                        hp_text.font_y = card_attacker.Y+card_attacker.HEIGHT-card_attacker.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, card_attacker)
                        if flag_animation_attack == 10:
                            card_attacker.DAMAGE += 1
                        if flag_animation_attack == 10:
                            sound_heal.play_sound()
                        hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'red','-'+str(card_attacker.DAMAGE - 1),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)   
                    hp_text.show_text(win)


                #Если атакует арбалетчик - проверяем, нужно ли ему наносить двойной урон
                elif flag_animation_attack == 25:
                    if card_attacker.NAME == 'арбалетчик':
                        if double_damage !=  'Dont reapet':
                            double_damage = randint(0,1)
                            if card_victim.HP > 0:
                                if double_damage:
                                    flag_animation_attack = 0
                                    double_damage = 'Dont reapet'
                    #Если карта - кентавр, задаем, нужно ли оглушать врага 
                    elif card_attacker.NAME == 'кентавр':
                        chance_to_stun = randint(1,100)
                        if chance_to_stun <= 35:
                            card_victim.can_move = False

                #Конец анимации
                elif flag_animation_attack == 26:
                    #Если карту врага убили - она исчезает
                    for c in list_objects_cards_pl:
                        
                        if c.path != None:
                            if c.HP <= 0:
                                c.path = None
                                list_losed_card_pl.append(c.NAME)
                    #Обновляем все переменные
                    card_victim = None
                    
                    card_attacker.X = card_attacker.START_X
                    card_attacker.Y = card_attacker.START_Y
                    flag_animation_attack = 0
                    card_attacker = None
                    double_damage = None
                    who_move = 'player'
                    count_text_move = 0
                    text_move.font_content ='Твой ход'
                    text_move.font_color = 'white'
                    card_that_move_en.Y =  card_that_move_en.START_Y -  card_that_move_en.HEIGHT//4
                    card_that_move_en.START_Y = card_that_move_en.START_Y -  card_that_move_en.HEIGHT//4
                    index_card_that_move_en += 1
                    card_that_move_en = None
                    
                    
                flag_animation_attack += 1

             # Если происходит лечение или прибавление ХП
            elif card_attacker!= None and is_healing and who_move =='enemy' and count_text_move > 30:
                # Лечебная карта становиться под картой, которую нужно лечить
                if flag_animation_attack <= 1:
                    card_attacker.X = card_victim.X
                    card_attacker.Y = card_victim.Y + card_victim.HEIGHT
                    hp_text = Font('images/Font/pixel_font.ttf', card_victim.HEIGHT//5,'green','+'+str(default_par_cards[card_victim.NAME][0]- card_victim.HP),card_victim.X -card_victim.WIDTH // 2.9 ,card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6)
                    
                #Карта  делает "замах" 
                elif  flag_animation_attack < 10 :
                    card_attacker.Y += card_attacker.HEIGHT // 40
                    heal_cloud.X = card_attacker.X
                    heal_cloud.Y = card_attacker.Y 
                    dmg_img.X = card_attacker.X
                    dmg_img.Y = card_attacker.Y 
                #Лечебная карта пускает облако
                elif 11 < flag_animation_attack <= 20:
                    if card_attacker.NAME == 'клаус':
                        heal_cloud.Y -= card_attacker.HEIGHT//20
                        heal_cloud.show_image(win)
                    elif card_attacker.NAME == 'дворф':
                        dmg_img.Y -= card_attacker.HEIGHT//20
                        dmg_img.show_image(win)
                #Отображаем текст, сколько лечебная карта похилила    
                elif 21< flag_animation_attack < 37:
                    if card_attacker.NAME == 'дворф':
                        hp_text.font_content = '+2'
                        hp_text.font_color = 'yellow'
                        hp_text.font_x = card_victim.X + card_victim.WIDTH 
                        hp_text.font_y = card_victim.Y+card_victim.HEIGHT-card_victim.HEIGHT//6
                        hp_text.show_text(win)
                        flashing_card(flag_animation_attack, card_victim)
                        if flag_animation_attack == 22:
                            card_victim.DAMAGE += 2

                    else:
                        hp_text.show_text(win) 
                        card_victim.HP = default_par_cards[card_victim.NAME][0]
                        flashing_card(flag_animation_attack, card_victim)

                    if flag_animation_attack == 22:
                            sound_heal.play_sound()
                
                # Конец анимации
                elif flag_animation_attack == 37:

                    #Обнуляем все переменные
                    card_victim = None
                    card_attacker.X = card_attacker.START_X
                    card_attacker.Y = card_attacker.START_Y
                    flag_animation_attack = 0
                    card_attacker = None
                    is_healing = None
                    who_move = 'player'
                    count_text_move = 0
                    text_move.font_content ='Твой ход'
                    text_move.font_color = 'white'
                    card_that_move_en.Y =  card_that_move_en.START_Y -  card_that_move_en.HEIGHT//4
                    card_that_move_en.START_Y = card_that_move_en.START_Y -  card_that_move_en.HEIGHT//4
                    index_card_that_move_en += 1
                    card_that_move_en = None
                    
                flag_animation_attack += 1




            #Если нужно, отображаем карточку-описание
            if card_that_showing_desc != None:
                if flag_show_desc >= 30:
                    card_that_showing_desc.show_desc(win)
                    if flag_show_desc == 30:
                        sound_paper.play_sound()
                flag_show_desc += 1
            #Отображаем описание скилла
            if desc_skill.path != None:
                if flag_show_desc_skill >= 30:
                    desc_skill.show_image(win)
                    if flag_show_desc_skill == 30:
                        sound_paper.play_sound()
                flag_show_desc_skill += 1
            #Отображаем ошибку, если нужно
            if flag_show_error < 30:
                generate_error(frame_error,error_text_obj,text_error_content,win)
                flag_show_error += 1   
                
                
                    
        #Сцена с показом результата боя 
        elif scene == 'result_screen':
            #В зависимости от того, кто победил - отображаем соответствующий фон 
            if who_won == 'player':
                bg_win.show_image(win)
            else:
                bg_lose.show_image(win)
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
            #Отображаем кнопку завершения бояы
            button_end_fight.show_image(win)
                          
        pygame.display.flip()
