import pygame 
from sounds_cardgame import*
from Text_cardgame import*
from random import choice, randint
from constants_cardgame import*
from additional_functions_cardgame import*
from cardgame_objects import*
from battle_functions_cardgame import*
from event_functions_cardgame import*
from dict_cardgame_variables import*
from draw_function import draw_all
# from objects import bg
pygame.init()

    
def run_game():
    cards_arrangement(list_cards_en,list_cards_pl,list_objects_cards_en,list_objects_cards_pl,default_par_cards)
    pygame.mixer.music.load(os.path.join(os.path.abspath(__file__ + "/.."), 'sounds/game_music.wav'))
    pygame.mixer.music.play(-1)
    # Списки с именами карт, которые потеряли игрок и враг
    list_losed_card_enemy = []
    list_losed_card_pl = []
    # Опыт и золото, которое получил игрок при победе
    trophy_exp = 0
    trophy_gold = 0
    #Переменная, отвечащаяя за сцену
    scene = 'game'
    #Задаем значение ФПС 
    fps =  pygame.time.Clock()

    #Переменная, отвечающая за игру
    game = True
    #Главный цикл игры
    while game:
        
        for event in pygame.event.get():
            mouse_cor = pygame.mouse.get_pos() 
            #Условие выхода из игры
            if event.type == pygame.QUIT:
                game = False
        
            if scene == 'result_screen':
                # Если навелись на кнопку окончания боя
                if event.type == pygame.MOUSEMOTION:
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
                    
                    if cardgame_variables['who_move'] == 'player':
                        cardgame_variables['index_picked_card'] = 0
                        #Функция взятия карты в руки
                        take_card(cardgame_variables,list_objects_cards_pl,check_mouse_cor,mouse_cor,)
                        #Функция приминения скилла  героя
                        activate_hero_skill(cardgame_variables,heal_cloud,dmg_img,check_mouse_cor,cardgame_variables['hero_skill'],mouse_cor)
                    cardgame_variables['card_that_showing_desc'] = None

                #Если отпущена ЛКМ                
                if  event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    #Отвечает за обнаружение цели, которую выбрал игрок, когда отпустил карту или скилл
                    target_searching(cardgame_variables,list_objects_cards_en,list_objects_cards_pl,check_mouse_cor,mouse_cor,default_par_cards)
                      
                #Условие движения мыши
                if event.type == pygame.MOUSEMOTION:
                    mousemoution_react(cardgame_variables,mouse_cor,list_objects_cards_en,check_mouse_cor,
                    list_objects_cards_pl,desc_skill,heal_cloud,dmg_img)
                        

                    
            
                
            

        if scene == 'game':
            #Алгоритм поочередности ходов игрока и врага
            move_players_algorithm(cardgame_variables,list_objects_cards_pl,text_move,list_objects_cards_en,default_par_cards)
            #Отрисовуем все граф. эелементы
            draw_all(bg,cardgame_variables,win,text_move,list_objects_cards_pl,list_objects_cards_en,
            stun_img,heal_cloud,dmg_img)
            
            
            #Проверка на то, кто победил 
            count_cards_player = 0
            for c in list_objects_cards_pl:
                if c.path != None:
                    count_cards_player += 1
            if count_cards_player == 0 and cardgame_variables['flag_animation_attack'] <= 1:
                cardgame_variables['who_won'] = 'enemy'
                scene = 'result_screen'
                
            count_cards_enemy = 0
            for c in list_objects_cards_en:
                if c.path != None:
                    count_cards_enemy += 1

            if count_cards_enemy == 0 and cardgame_variables['flag_animation_attack'] <= 1:
                cardgame_variables['who_won'] = 'player'
                scene = 'result_screen'
                for c in list_losed_card_enemy:
                    trophy_exp += default_par_cards[c][2]*15
                    trophy_gold += default_par_cards[c][2]//2

            cardgame_variables['count_play_sound'] += 1

            #Функция атаки игрока
            player_attack(cardgame_variables,list_objects_cards_pl,list_objects_cards_en,flashing_card,
            Font,win,list_losed_card_enemy,)
            # Функция атаки врага
            enemy_attack(cardgame_variables,flashing_card,list_losed_card_pl,show_all_windows)                
        #Сцена с показом результата боя 
        elif scene == 'result_screen':
            pygame.mixer.music.stop()
            #Функция для показа экрана результата
            show_result_screen(win,bg_win,music_win,bg_lose,music_lose,card_for_result_screen,SCREEN_W,SCREEN_H,
            list_losed_card_enemy,list_losed_card_pl,trophy_exp,trophy_gold,gold_icon,exp_icon,trophy_recourse_text,button_end_fight,
            cardgame_variables)



           


                    
                      
                          

            
                
        fps.tick(30)
        pygame.display.flip()


run_game()