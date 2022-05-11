#Функция для отображения окна с ошибкой
def generate_error(frame_error,error_text_obj,error_content,win):
    frame_error.show_image(win)
    error_text_obj.font_content = error_content
    error_text_obj.show_text(win)

# Рамка для ошибки
frame_error = Graphic_elements_cards(SCREEN_W//2 - SCREEN_W//6, SCREEN_H//2 - SCREEN_H//8, SCREEN_W//3, SCREEN_H//4, 'images/error_sheet.png')
# Объект текста ошибки
error_text_obj = Font('images/Font/pixel_font.ttf',SCREEN_W//50,'red',None,frame_error.X+SCREEN_W//40,frame_error.Y + SCREEN_H//10)
# Флаг для отображения ошибки
flag_show_error = 30
#Контент ошибки 
text_error_content = None



#Отображаем ошибку, если нужно
if flag_show_error < 30:
    generate_error(frame_error,error_text_obj,text_error_content,win)
    flag_show_error += 1