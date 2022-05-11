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