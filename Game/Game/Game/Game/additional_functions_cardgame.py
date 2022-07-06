#Функция, заставляющая карту "мигать" 
def flashing_card(flag_animation_attack, card):
    if flag_animation_attack % 4 != 0:
        card.path = None
    else:
        card.path = 'images/cards/'+ card.NAME +'.png'



#Функция сравнения кординаты мыши и спрайта
def check_mouse_cor(sprite,mouse_cor):
    if mouse_cor[0] > sprite.X and mouse_cor[0] < sprite.X + sprite.WIDTH and mouse_cor[1] > sprite.Y and mouse_cor[1] < sprite.Y + sprite.HEIGHT:
        return True

#Функция для отображения окна с ошибкой
def generate_error(frame_error,error_text_obj,error_content,win):
    frame_error.show_image(win)
    error_text_obj.font_content = error_content
    error_text_obj.show_text(win)
#Функция для показа всех всплывающих окон 
def show_all_windows(sound_paper,win,desc_skill, frame_error,error_text_obj,
                    text_error_content, cardgame_variables ):
    #Если нужно, отображаем карточку-описание
    if cardgame_variables['card_that_showing_desc'] != None:
        if cardgame_variables['flag_show_desc'] >= 30:
            cardgame_variables['card_that_showing_desc'].show_desc(win)
            if cardgame_variables['flag_show_desc'] == 30:
                sound_paper.play_sound()
        cardgame_variables['flag_show_desc'] += 1
    #Отображаем описание скилла
    if desc_skill.path != None:
        if cardgame_variables['flag_show_desc_skill'] >= 30:
            desc_skill.show_image(win)
            if cardgame_variables['flag_show_desc_skill'] == 30:
                sound_paper.play_sound()
        cardgame_variables['flag_show_desc_skill'] += 1
    #Отображаем ошибку, если нужно
    if cardgame_variables['flag_show_error'] < 30:
        generate_error(frame_error,error_text_obj,text_error_content,win)
        cardgame_variables['flag_show_error'] += 1   