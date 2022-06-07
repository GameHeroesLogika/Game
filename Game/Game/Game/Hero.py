from const import*
import pygame
from random import choice,randint,shuffle
from Addition_Module import move_to_hero
from sounds import Sounds
from graphic_elements import Graphic_elements
from Text import Font
import os

pygame.init()
class Main_Hero(Graphic_elements):
    def __init__(self,x,y,width,height,path,SCREEN_W,SCREEN_H,where_move,count_move, win,count_step):
        super().__init__(x,y,width,height,path)
        self.flag_pressed = True
        self.flag_move = True
        self.list_studied_map = []# Список изученых клеток
        self.index_cor = []
        self.player_cor = [3,1]# Индексы(координаты) пресонажа по матрице
        self.SCREEN_W = SCREEN_W# Ширина эекрана
        self.SCREEN_H = SCREEN_H# Высота эекрана
        self.where_move = where_move# Сторона в которую движется персонаж
        self.count_move = count_move
        self.changed_x = 0# Изменения х персонажа
        self.changed_y = 0# Изменения у персонажа
        self.index = 0
        self.list_images_right = []# Список изображений вправо
        self.list_images_left = []# Список изображений влево
        self.list_images_up = []# Список изображений вверх
        self.list_images_down = []# Список изображений вниз
        self.count_step = count_step# Количество шагов
        self.win = win#Объект экрана 
        self.near_building = False# Флаг нахождения возле здания 
        self.list_capture_buildings = []# Список захваченных зданий
        self.list_capture_buildings_symbol = []# Список символов захваченных зданий
        self.need_to_move_to_hero = False#Нужно ли перемещаться к игроку после телепорта
        

        self.near_chest = False
        self.near_city = False
        self.near_tower = False
        self.near_academy = False
        self.near_shack = False
        self.near_tavern = False
        self.near_market = False
        self.near_fountain_exp = False
        self.near_fountain_mana = False
        self.near_card = False

        self.card_name = False

        self.card_cor = False
        self.city_cor = None
        self.chest_cor = None
        self.tower_cor = None
        self.building_cor = None
        self.fountain_exp_cor = None
        self.fountain_mana_cor = None
        self.shack_cor = None

        self.flag_up = False
        self.flag_down = False
        self.flag_right = False
        self.flag_left = False

        self.flag_card = False
        self.flag_city = False
        self.flag_fountain_mana = False
        self.flag_fountain_exp = False
        self.flag_market = False
        self.flag_draw_chest = False
        self.flag_tower = False
        self.flag_academy = False
        self.flag_shack = False
        self.flag_tavern = False
        for i in range(4):# Заполнение списков изобржаний с движением 
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/right/'+str(i)+'.png')
            self.list_images_right.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/left/'+str(i)+'.png')
            self.list_images_left.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/up/'+str(i)+'.png')
            self.list_images_up.append(path)
            path = os.path.join(os.path.abspath(__file__+'/..'),'images/player/down/'+str(i)+'.png')
            self.list_images_down.append(path)
        #Создание графического экземпляра класса
        self = Graphic_elements(0, 0, SCREEN_W//19, SCREEN_W//19, 'images/player/player_front.png')
         

        
        
    def move_sprite(self, mat_objetcs, LENGTH_MAP,resources_dict,recourse_sounds,list_cor_portals,list_card_matrix):
        
        #Если нажата клавиша ВПРАВО
        if self.count_step != 0:
            if self.where_move == 'right' and self.count_move <= 9:
                # Условия для телепорта
                if self.count_move == 8:
                    # Если клетка справа - телеопрт
                    if mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == 'P':
                        # Перебираме список координат порталов
                        for i in list_cor_portals:
                            # Узнаем на каком именно портале мы находимся
                            for cors in i:
                                if self.player_cor[1] + 1 == cors[1] and self.player_cor[0]   == cors[0]:
                                    # Узнаем, куда нужно телепортировать игрока
                                    for tp_cors in i:
                                        if tp_cors != cors:
                                            mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                                            self.player_cor[1] = tp_cors[1] - 1
                                            self.player_cor[0] = tp_cors[0] + 1
                                            self.count_move = 0
                                            self.index = 0
                                            self.need_to_move_to_hero = True

                                            # move_to_hero(CENTER_CELL_COR,list_cor_player_xy,list_objects_cells_lvl1,SCREEN_W,SCREEN_H)
                                            

                                
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_right[self.index]
                    self.image_load()
                    self.index+=1
                self.X += (self.SCREEN_W//19)/10
                self.changed_x = self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1
                

            elif self.count_move > 9 and self.where_move == 'right':
                self.index = 0
                self.count_move = 0
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.where_move = None
                self.changed_x = 0
                mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] = 'p'
                if mat_objetcs[self.player_cor[0]][self.player_cor[1]] == 'p':
                    mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[1] += 1
                
              
                
                
            if self.where_move == 'left' and self.count_move <= 9:
                # Условия для телепорта
                if self.count_move == 8:
                    if mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == 'P':
                        for i in list_cor_portals:
                            for cors in i:
                                if self.player_cor[1] - 1 == cors[1] and self.player_cor[0]   == cors[0]:
                                    for tp_cors in i:
                                        if tp_cors != cors:
                                            mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                                            self.player_cor[1] = tp_cors[1] + 1
                                            self.player_cor[0] = tp_cors[0] + 1
                                            self.count_move = 0
                                            self.index = 0
                                            self.need_to_move_to_hero = True


                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_left[self.index]
                    self.image_load()
                    self.index+=1
                self.X -= (self.SCREEN_W//19)/10
                self.changed_x = -1*self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1
            elif self.count_move > 9 and self.where_move == 'left':
                self.index = 0
                self.count_move = 0
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.where_move = None
                self.changed_x = 0
                mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] = 'p'
                #Указываем, что на метсе, где стоя игрок - пустая клетка
                mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                #Изменяем координату игрока
                self.player_cor[1] -= 1
            if self.where_move == 'up' and self.count_move <= 9:
                # Условия для портала
                if self.count_move == 8: 
                    if mat_objetcs[self.player_cor[0]-1][self.player_cor[1]] == 'P': 
                        for i in list_cor_portals:
                            for cors in i:
                                if self.player_cor[1] == cors[1] and self.player_cor[0] - 1   == cors[0]: 
                                    for tp_cors in i:
                                        if tp_cors != cors:
                                            mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                                            self.player_cor[1] = tp_cors[1]
                                            self.player_cor[0] = tp_cors[0] + 2
                                            self.count_move = 0
                                            self.index = 0
                                            self.need_to_move_to_hero = True
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_up[self.index]
                    self.image_load()
                    self.index+=1
                self.Y -= (self.SCREEN_W//19)/10
                self.changed_y = -1*self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1

            elif self.count_move > 9 and self.where_move == 'up':
                self.count_move = 0
                self.index = 0
                self.where_move = None
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.changed_y = 0
                mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] = 'p'
                if mat_objetcs[self.player_cor[0]][self.player_cor[1]] == 'p':
                    mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[0] -= 1

            if self.where_move == 'down' and self.count_move <= 9:
                
                if self.count_move == 0 or self.count_move == 3 or self.count_move == 6 or self.count_move == 9:
                    self.path = self.list_images_down[self.index]
                    self.image_load()
                    self.index+=1
                self.X += (self.SCREEN_W//19)/10
                self.changed_y = self.count_move*(self.SCREEN_W//19)/10
                self.count_move+=1

            elif self.count_move > 9 and self.where_move == 'down':
                self.index = 0
                self.count_move = 0
                self.where_move = None
                # self.path = 'images/player/player_front.png'
                # self.image_load()
                self.changed_y = 0
                mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] = 'p'
                if mat_objetcs[self.player_cor[0]][self.player_cor[1]] == 'p':
                    mat_objetcs[self.player_cor[0]][self.player_cor[1]] = '0'
                self.player_cor[0] += 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.flag_move and self.where_move == None:
                #Если мы стоим не с правого краю карты
                if self.player_cor[1] != LENGTH_MAP - 1:
                    #Вызываем функции подбора ресрусов
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'gold_bullion','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'iron_bullion','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'stone','b',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] + 1,'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                
                    if (mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == '0' or mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == 'P') and self.where_move == None:
                        self.where_move = 'right'
                        self.count_step -= 1
                # if mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == 'P' and :
                    # self.player_cor[1]+=10
                        #Указываем, что игрок переместился на клетку вправо
                    
            #Если нажата клавиша ВЛЕВО
            elif keys[pygame.K_LEFT] and self.flag_move and self.where_move == None:
                if self.player_cor[1] != 0:
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'gold_bullion','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'iron_bullion','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'stone','b',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0],self.player_cor[1] - 1,'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                
                    if (mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == '0' or mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == 'P') and self.where_move == None:
                        self.where_move = 'left'
                        self.count_step -= 1

                        
            #Если нажата клавиша ВВЕРХ
            elif keys[pygame.K_UP] and self.flag_move and self.where_move == None:
                if self.player_cor[0] != 0:
                    
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'gold_bullion','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'iron_bullion','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'stone','b',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]-1,self.player_cor[1],'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)
                
                    if (mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] == '0' or mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] == 'P') and self.where_move == None:
                        self.where_move = 'up'
                        self.count_step -= 1
                        
            #Если нажата клавиша ВНИЗ
            elif keys[pygame.K_DOWN] and self.flag_move and self.where_move == None:
                if self.player_cor[0] != LENGTH_MAP - 1:
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'gold_bullion','g',mat_objetcs,2,4,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'iron_bullion','i',mat_objetcs,4,6,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'wood','w',mat_objetcs,8,10,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'stone','b',mat_objetcs,6,8,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'crystal','c',mat_objetcs,1,2,resources_dict,recourse_sounds)
                    self.take_resource(self.player_cor[0]+1,self.player_cor[1],'food','T',mat_objetcs,10,12,resources_dict,recourse_sounds)

                    if mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] == '0'  and self.where_move == None:
                        self.where_move = 'down'
                        self.count_step -= 1

          
            list_symbols_biuldings = ['F','f','D','d','N','n','R','r','H','h','X','x']
            list_symbol_cards = ['А','Б','В','Г','Д','К','С','Л','О','Е','Р','М','Я','П']
            if self.player_cor[1] == LENGTH_MAP - 1:
                self.flag_right = True
            else:
                self.flag_right = False
            if self.player_cor[0] == LENGTH_MAP - 1:
                self.flag_down = True
            else:
                self.flag_down = False
            if self.player_cor[0] == 0:
                self.flag_up = True
            else:
                self.flag_up = False
            if self.player_cor[1] == 0:
                self.flag_left = True
            else:
                self.flag_left = False
        #Здания
            # if self.player_cor[1] != LENGTH_MAP - 1 and self.player_cor[0] != LENGTH_MAP - 1 and self.player_cor[0] != 0 and self.player_cor[1] != 0: 
            if not self.flag_right and mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] in list_symbols_biuldings:
                self.near_building = True
                self.building_cor = mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1]
            elif not self.flag_left and mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] in list_symbols_biuldings:
                self.near_building = True
                self.building_cor = mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1]
            elif not self.flag_down and mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] in list_symbols_biuldings:
                self.near_building = True
                self.building_cor = mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]]
            elif not self.flag_up and mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] in list_symbols_biuldings:
                self.near_building = True
                self.building_cor = mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]]
            else:
                self.near_building = False
                self.building_cor = None

            if not self.flag_right and mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] in list_symbol_cards:
                self.near_card = True
                self.card_name = mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1]
                self.card_cor = [self.player_cor[0],self.player_cor[1] + 1]
            elif not self.flag_left and mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] in list_symbol_cards:
                self.near_card = True
                self.card_name = mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1]
                self.card_cor = [self.player_cor[0],self.player_cor[1] - 1]
            elif not self.flag_down and mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] in list_symbol_cards:
                self.near_card = True
                self.card_name = mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]]
                self.card_cor = [self.player_cor[0] + 1,self.player_cor[1]]
            elif not self.flag_up and mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] in list_symbol_cards:
                self.near_card = True
                self.card_name = mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]]
                self.card_cor = [self.player_cor[0] - 1,self.player_cor[1]]
            else:
                self.near_card = False
                self.card_name = None
            #Сундук
            self.near_chest,self.chest_cor = self.check_near_build(element='C',mat_objetcs=mat_objetcs,flag_building_cor=True)
            #Башня
            self.near_tower,self.tower_cor = self.check_near_build(element='W',mat_objetcs=mat_objetcs,flag_building_cor=True)
            #Таверна
            self.near_tavern = self.check_near_build(element='J',sub_element='j',mat_objetcs=mat_objetcs,flag_building_cor=False)
            #Рынок
            self.near_market = self.check_near_build(element='O',sub_element='o',mat_objetcs=mat_objetcs,flag_building_cor=False)
            #Академия
            self.near_academy = self.check_near_build(element='A',sub_element='a',mat_objetcs=mat_objetcs,flag_building_cor=False)
            #Город
            self.near_city = self.check_near_build(element='K',sub_element='k',mat_objetcs=mat_objetcs,flag_building_cor=False)
            #Башня колдуна
            self.near_shack,self.shack_cor = self.check_near_build(element='S',sub_element='s',mat_objetcs=mat_objetcs,flag_building_cor=True)
            #Фонтаны
            self.near_fountain_mana,self.fountain_mana_cor = self.check_near_build(element='M',sub_element='m',mat_objetcs=mat_objetcs,flag_building_cor=True)
            self.near_fountain_exp,self.fountain_exp_cor = self.check_near_build(element='E',sub_element='e',mat_objetcs=mat_objetcs,flag_building_cor=True)

            if self.near_card:
                for obj in list_card_matrix:
                    if obj.NAME == self.card_name:
                        self.show_tip( '[F] Поговорить с '+obj.path.split('/')[-1].split('.')[0], self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//65,font_size=settings['SCREEN_WIDTH']//80)
                        if keys[pygame.K_f]:
                            self.flag_card = obj.path.split('/')[-1].split('.')[0]
                            self.near_card = False
            if self.near_chest:
                self.show_tip( '[F] Открыть сундук', self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//65)
                if keys[pygame.K_f]:
                    self.near_chest = False
                    self.flag_draw_chest = True
                    self.flag_move = False
            if self.near_fountain_exp:
                self.show_tip(' [E] Дерево знаний',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_fountain_exp = True
                    self.flag_pressed = True
            if self.near_fountain_mana :
                self.show_tip(' [E] Колодец маны',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_fountain_mana = True
                    self.flag_pressed = True
            if self.near_tower:
                self.show_tip(' [E] Поставить дозорного',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5,font_size=settings['SCREEN_WIDTH']//80)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_tower = True
                    self.flag_pressed = True
            if self.near_academy:
                self.show_tip(' [E] Академия',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_academy = True
                    self.flag_pressed = True
            if self.near_shack :
                self.show_tip(' [E] Хижина Колдуна',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_shack = True
                    self.flag_pressed = True
            if self.near_tavern:
                self.show_tip(' [E] Сыграть в карты',self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//32.5)
                if keys[pygame.K_e] and self.flag_pressed == False:
                    self.flag_tavern = True
                    self.flag_pressed = True
            if self.near_market:
                # self.show_tip( '[F] Съесть бутерброд', self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//65)
                self.show_tip( '[F] Зайти на рынок', self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//65)
                if keys[pygame.K_f]:
                    self.near_market = False
                    self.flag_market = True
            if self.near_city:
                self.show_tip( '[F] Зайти в город', self.SCREEN_W-self.SCREEN_W//6.4, self.SCREEN_W//65)
                if keys[pygame.K_f]:
                    self.flag_city = True
                    self.near_city = False
            if not keys[pygame.K_e] and self.flag_pressed:
                self.flag_pressed = False
            #Если рядом со здание и нажимаем кнопку E - захватываем здание
            if self.near_building:
                self.show_tip( '[E] Захватить здание', self.SCREEN_W-self.SCREEN_W//6.4, 0)
                if  keys[pygame.K_e] and self.building_cor!=None:
                    if self.building_cor.upper() == mat_objetcs[self.player_cor[0]+1][self.player_cor[1]]:
                        if (self.player_cor[0]+1,self.player_cor[1]) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]+1,self.player_cor[1]))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]][self.player_cor[1]+1]:
                        if (self.player_cor[0],self.player_cor[1]+1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0],self.player_cor[1]+1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]-2][self.player_cor[1]]:
                        if (self.player_cor[0]-2,self.player_cor[1]) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]-2,self.player_cor[1]))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]+2][self.player_cor[1]]:
                        if (self.player_cor[0]+2,self.player_cor[1]) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]+2,self.player_cor[1]))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]][self.player_cor[1]+2]:
                        if (self.player_cor[0],self.player_cor[1]+2) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0],self.player_cor[1]+2))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]][self.player_cor[1]-2]:
                        if (self.player_cor[0],self.player_cor[1]-2) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0],self.player_cor[1]-2))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]-1][self.player_cor[1]-1]:
                        if (self.player_cor[0]-1,self.player_cor[1]-1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]-1,self.player_cor[1]-1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]+1][self.player_cor[1]+1]:
                        if (self.player_cor[0]+1,self.player_cor[1]+1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]+1,self.player_cor[1]+1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]-1][self.player_cor[1]+1]:
                        if (self.player_cor[0]-1,self.player_cor[1]+1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]-1,self.player_cor[1]+1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]+1][self.player_cor[1]-1]:
                        if (self.player_cor[0]+1,self.player_cor[1]-1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]+1,self.player_cor[1]-1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]-2][self.player_cor[1]-1]:
                        if (self.player_cor[0]-2,self.player_cor[1]-1) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]-2,self.player_cor[1]-1))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
                    elif self.building_cor.upper() == mat_objetcs[self.player_cor[0]-1][self.player_cor[1]-2]:
                        if (self.player_cor[0]-1,self.player_cor[1]-2) not in  self.list_capture_buildings:
                            self.list_capture_buildings.append((self.player_cor[0]-1,self.player_cor[1]-2))
                            self.list_capture_buildings_symbol.append(self.building_cor.upper())
            

    #Функция для сбора ресрусов
    def take_resource(self,index_x,index_y,name_resource,resource_symb,mat_objetcs,min_count,max_count,resources_dict,recourse_sounds):
        if mat_objetcs[index_x][index_y] == resource_symb:
            resources_dict[name_resource] += randint(min_count, max_count)
            choice(recourse_sounds).play_sound()
            if resource_symb == 'T':
                mat_objetcs[index_x][index_y] = 't'
            else:
                mat_objetcs[index_x][index_y] = '0'


    #Функция для показа подсказок
    def show_tip(self, text, x_text, y_text,font_size = settings['SCREEN_WIDTH']//65):
        text = Font('images/Font/pixel_font.ttf',font_size,(255,255,255),text,x_text,y_text)
        text.show_text(self.win)

    # Метод тумана войны 
    def blind_move(self,index,flag_player): 
        # print(len(self.list_studied_map))
        #Константы координат персонажа
        if flag_player[2]:
            index_y = self.player_cor[0]
            index_x = self.player_cor[1]
        else:
            index_y = flag_player[1]
            index_x = flag_player[0]
        
        #Список с координатами персонажа
        self.index_cor = [index_x,index_y]
        #Список с координатами персонажа из списка с координатами персонажа 
        list_cor= list()
        #Цикл работы тумана войны(универсальный)
        for i in range(index):
        #Движение вправо 
            self.index_cor[0]+=i+1
            list_cor= [self.index_cor[0],self.index_cor[1]]
            if list_cor[0] < 0:
                list_cor[0] = list_cor[0]*-1
            if list_cor[1] < 0:
                list_cor[1] = list_cor[1]*-1
            if not list_cor in self.list_studied_map:
                self.list_studied_map.append(list_cor)
            #Движение вправо, дальше по вертикали 
            for number in range(index):
                self.index_cor[1]+=-number-1
                list_cor= [self.index_cor[0],self.index_cor[1]]
                if list_cor[0] < 0:
                    list_cor[0] = list_cor[0]*-1
                if list_cor[1] < 0:
                    list_cor[1] = list_cor[1]*-1
                if not list_cor in self.list_studied_map:
                    self.list_studied_map.append(list_cor)
                self.index_cor[1] = index_y
                self.index_cor[1]+=number+1
                list_cor= [self.index_cor[0],self.index_cor[1]]
                if list_cor[0] < 0:
                    list_cor[0] = list_cor[0]*-1
                if list_cor[1] < 0:
                    list_cor[1] = list_cor[1]*-1
                if not list_cor in self.list_studied_map:
                    self.list_studied_map.append(list_cor)
                self.index_cor[1] = index_y
            self.index_cor = [index_x,index_y] 

            #Движение влево
            self.index_cor[0]+=-i-1
            list_cor= [self.index_cor[0],self.index_cor[1]]
            if list_cor[0] < 0:
                list_cor[0] = list_cor[0]*-1
            if list_cor[1] < 0:
                list_cor[1] = list_cor[1]*-1
            if not list_cor in self.list_studied_map:
                self.list_studied_map.append(list_cor)
            #Движение вправо, дальше по вертикали 
            for number in range(index):
                self.index_cor[1]+=-number-1
                list_cor= [self.index_cor[0],self.index_cor[1]]
                if list_cor[0] < 0:
                    list_cor[0] = list_cor[0]*-1
                if list_cor[1] < 0:
                    list_cor[1] = list_cor[1]*-1
                if not list_cor in self.list_studied_map:
                    self.list_studied_map.append(list_cor)
                self.index_cor[1] = index_y
                self.index_cor[1]+=number+1
                list_cor= [self.index_cor[0],self.index_cor[1]]
                if list_cor[0] < 0:
                    list_cor[0] = list_cor[0]*-1
                if list_cor[1] < 0:
                    list_cor[1] = list_cor[1]*-1
                if not list_cor in self.list_studied_map:
                    self.list_studied_map.append(list_cor)
                self.index_cor[1] = index_y
            self.index_cor = [index_x,index_y] 
            #Движение вниз
            self.index_cor[1]+=i+1
            list_cor= [self.index_cor[0],self.index_cor[1]]
            if list_cor[0] < 0:
                list_cor[0] = list_cor[0]*-1
            if list_cor[1] < 0:
                list_cor[1] = list_cor[1]*-1
            if not list_cor in self.list_studied_map:
                self.list_studied_map.append(list_cor)
            self.index_cor = [index_x,index_y] 
            #Движение вверх
            self.index_cor[1]+=-i-1
            list_cor= [self.index_cor[0],self.index_cor[1]]
            if list_cor[0] < 0:
                list_cor[0] = list_cor[0]*-1
            if list_cor[1] < 0:
                list_cor[1] = list_cor[1]*-1
            if not list_cor in self.list_studied_map:
                self.list_studied_map.append(list_cor)
            self.index_cor = [index_x,index_y] 
            #Координаты персонажа не двигаясь 
            list_cor= [self.index_cor[0],self.index_cor[1]]
            if list_cor[0] < 0:
                list_cor[0] = list_cor[0]*-1
            if list_cor[1] < 0:
                list_cor[1] = list_cor[1]*-1
            if not list_cor in self.list_studied_map: 
                self.list_studied_map.append(list_cor)
            
        self.index_cor = [index_x,index_y] 
    def check_near_build(self,element,mat_objetcs,sub_element=None,flag_building_cor=None):
        building_cor = None
        if not self.flag_right and (mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == element or mat_objetcs[self.player_cor[0]][self.player_cor[1] + 1] == sub_element)  :
            flag_near_building = True
            if flag_building_cor == True:
                building_cor = [self.player_cor[0],self.player_cor[1] + 1]
        elif not self.flag_left and (mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == element or mat_objetcs[self.player_cor[0]][self.player_cor[1] - 1] == sub_element)  :
            flag_near_building = True
            if flag_building_cor == True:
                building_cor = [self.player_cor[0],self.player_cor[1] - 1]
        elif not self.flag_down and (mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] == element or  mat_objetcs[self.player_cor[0] + 1][self.player_cor[1]] == sub_element) :
            flag_near_building = True
            if flag_building_cor == True:
                building_cor = [self.player_cor[0]+1,self.player_cor[1]]
        elif not self.flag_up and (mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] == element or  mat_objetcs[self.player_cor[0] - 1][self.player_cor[1]] == sub_element) :
            flag_near_building = True
            if flag_building_cor == True:
                building_cor = [self.player_cor[0]-1,self.player_cor[1]]
        else:
            flag_near_building = False
        if flag_building_cor == True:
            return flag_near_building,building_cor
        if flag_building_cor == False:
            return flag_near_building