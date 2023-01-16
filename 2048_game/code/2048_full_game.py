import pygame as py
import random
import time
random.seed(time.time())
from sys import exit
py.init()
size=4
Target=2048
screen=py.display.set_mode((400,400))
def zero_placer():
    x_pos=75
    y_pos=60
    for i in range(size):
        for j in range(size):
            if game_board.data[i][j]==0:
                screen.blit(font_style.render(str(game_board.data[i][j]),True,'black'),(x_pos,y_pos))
            x_pos+=75
        x_pos=75
        y_pos+=75
def which_image_to_add(val):
    if val==2:
        return val2
    elif val==4:
        return val4
    elif val==8:
        return val8
    elif val==16:
        return val16
    elif val==32:
        return val32
    elif val==64:
        return val64
    elif val==128:
        return val128
    elif val==256:
        return val256
    elif val==512:
        return val512
    elif val==1024:
        return val1024
    elif val==2048:
        return val2048
def image_placer():
    x_pos=54
    y_pos=54
    for i in range(size):
        for j in range(size):
            if game_board.data[i][j]!=0:
                image_to_add=which_image_to_add(game_board.data[i][j])
                screen.blit(image_to_add,(x_pos,y_pos))
            x_pos+=75
        x_pos=54
        y_pos+=75
    pass
def valid_move_check():
    if check==game_board :
        return 0
    else:
        game_board.spawn()
        return 1
class Board:
    def __init__(self):
        self.data=[[0 for _ in range(size)] for _  in range(size)]
        self.index=0
    #def tostr(self,n):
    #    return f"{self.data[n]}"
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            self.index=0
            raise StopIteration
        result=self.data[self.index]
        self.index+=1
        return result
    def __eq__(self,other):
        for i in range(size):
            for j in range(size):
                if self.data[i][j]!=other.data[i][j]:
                    return False
        return True
    def copy(self,other):
        for i in range(size):
            for j in range(size):
                other.data[i][j]=self.data[i][j]
    def display(self):
        for i in self:
            print(i)
    def which_spawn_val(self):
        p1=random.randint(1,5)
        if p1==4:
            return 4
        return 2
    def where_spawn_val(self):
        while True:
            row=random.randint(0,3)
            col=random.randint(0,3)
            if self.data[row][col]==0:
                break
        return row,col
    def spawn(self):
        row,col=self.where_spawn_val()
        self.data[row][col]=self.which_spawn_val()
    def slide_up(self):
        for _ in range(size):
            for i in range(size-1):
                for j in range(size):
                    if self.data[i][j]==0 and self.data[i+1][j]!=0:
                        self.data[i][j]=self.data[i+1][j]
                        self.data[i+1][j]=0
        for i in range(size-1):
            for j in range(size):
                if self.data[i][j]==self.data[i+1][j]:
                    self.data[i][j]+=self.data[i+1][j]
                    self.data[i+1][j]=0
        for _ in range(size):
            for i in range(size-1):
                for j in range(size):
                    if self.data[i][j]==0 and self.data[i+1][j]!=0:
                        self.data[i][j]=self.data[i+1][j]
                        self.data[i+1][j]=0
    def revers(self):
        other=Board()
        z=size-1
        for i in self:
            other.data[z]=i
            z-=1
        return other

    def slide_left(self):
        for _ in range(size):
            for i in range(size):
                for j in range(size-1):
                    if self.data[i][j]==0 and self.data[i][j+1]!=0:
                        self.data[i][j]=self.data[i][j+1]
                        self.data[i][j+1]=0
        for i in range(size):
            for j in range(size-1):
                if self.data[i][j]==self.data[i][j+1]:
                    self.data[i][j]+=self.data[i][j+1]
                    self.data[i][j+1]=0
        for _ in range(size):
            for i in range(size):
                for j in range(size-1):
                    if self.data[i][j]==0 and self.data[i][j+1]!=0:
                        self.data[i][j]=self.data[i][j+1]
                        self.data[i][j+1]=0
    def turn(self):
        in1=[0,1,2,3]
        in2=[3,2,1,0]
        other=Board()
        for i in range(4):
            for j,j1 in zip(in1,in2):
                other.data[i][j]=self.data[i][j1]
                
        return other
    def lost_check(self):
        for i in range(size-1):
                for j in range(size-1):
                    if self.data[i][j]==self.data[i+1][j] or self.data[i][j]==self.data[i][j+1] :
                        return False
        for i in range(size):
                for j in range(size):
                    if self.data[i][j]==0:
                        return False
        return True
    def win_check(self):
        for i in range(size):
                for j in range(size):
                    if self.data[i][j]==Target:
                        return True
        return False
py.display.set_caption("Hello World")
clock=py.time.Clock()
font_style=py.font.Font('assets/DS-DIGI.TTF',50)
font_style1=py.font.Font('assets/DS-DIGI.TTF',25)
background=py.image.load("assets/background.png")
menu=py.image.load("assets/main_menue.png")
win_screen=py.image.load("assets/won1.png")
rules_screen=py.image.load("assets/rules.png")
lost_screen=py.image.load("assets/lost.png")
back=py.image.load("assets/back.png")
val2=py.image.load("assets/2box.png")
val4=py.image.load("assets/4box.png")
val8=py.image.load("assets/8box.png")
val16=py.image.load("assets/16box.png")
val32=py.image.load("assets/32box.png")
val64=py.image.load("assets/64box.png")
val128=py.image.load("assets/128box.png")
val256=py.image.load("assets/256box.png")
val512=py.image.load("assets/512box.png")
val1024=py.image.load("assets/1024box.png")
val2048=py.image.load("assets/2048box.png")
hover_con=py.image.load("assets\hover_con.png")
hover_str=py.image.load("assets\hover_str.png")
hover_rul=py.image.load("assets\hover_rul.png")
hover_2048=py.image.load("assets\hover_2048.png")
bon_2048=py.Rect(127,76,140,38)
start=py.Rect(145,218,72,30)
rules=py.Rect(145,259,72,37)
continu=py.Rect(136,177,104,30)
back_pos=py.Rect(3,367,60,30)
screen_val=1
spare=Board()
spare_move=0
first_spwan=1
while True:
    for event in py.event.get():    
        if event.type==py.QUIT:
            py.quit()
            exit()
        if event.type==py.KEYDOWN:
            game_board.copy(check)
            if event.key==py.K_w and screen_val==2:
                game_board.slide_up()
                move_number+=valid_move_check()
            elif event.key==py.K_s and screen_val==2:
                temp=game_board.revers()
                temp.slide_up()
                game_board=temp.revers()
                move_number+=valid_move_check()
            elif event.key==py.K_a and screen_val==2:
               game_board.slide_left()
               move_number+=valid_move_check()
            elif event.key==py.K_d and screen_val==2:
               temp=game_board.turn()
               temp.slide_left()
               game_board=temp.turn()
               move_number+=valid_move_check()
            elif event.key==py.K_x:
                py.quit()
                exit() 
    if screen_val==1:
        move_number=0
        game_board=Board()
        check=Board()
        screen.blit(menu,(0,0))
        menu_mouse_pos=py.mouse.get_pos()
        menu_mouse_pres=py.mouse.get_pressed()
        if start.collidepoint(menu_mouse_pos) :
            screen.blit(hover_str,(128,211))
        elif rules.collidepoint(menu_mouse_pos):
            screen.blit(hover_rul,(125,255))
        elif continu.collidepoint(menu_mouse_pos):
            screen.blit(hover_con,(130,170))
        elif bon_2048.collidepoint(menu_mouse_pos):
            screen.blit(hover_2048,(100,60))
        if start.collidepoint(menu_mouse_pos) and menu_mouse_pres[0]:
            first_spwan=1
            screen_val=2
        elif rules.collidepoint(menu_mouse_pos) and menu_mouse_pres[0]:
            screen_val=3
        elif continu.collidepoint(menu_mouse_pos) and menu_mouse_pres[0]:
            screen_val=2
            game_board=spare
            move_number=spare_move
    if screen_val==2:
        if first_spwan==1:
            game_board.spawn()
            first_spwan=0
        screen.blit(background,(0,0))
        zero_placer()
        image_placer()
        clock.tick(60)
        screen.blit(font_style1.render("Move number: "+str(move_number),True,'yellow'),(0,3))
        if game_board.lost_check():
            screen.blit(lost_screen,(0,0))
            screen.blit(font_style1.render("You lost after moveing: "+str(move_number)+" times",True,'blue'),(20,20))
        if game_board.win_check():
            screen.blit(win_screen,(0,0))
            screen.blit(font_style1.render("You won in: "+str(move_number),True,'blue'),(20,20))
        screen.blit(back,(10,360))
        game_mouse=py.mouse.get_pos()
        game_mouse_press=py.mouse.get_pressed()
        if back_pos.collidepoint(game_mouse) and game_mouse_press[0]:
            spare=game_board
            spare_move=move_number
            screen_val=1
    if screen_val==3:
        screen.blit(rules_screen,(0,0))
        screen.blit(back,(3,370))
        rule_mouse=py.mouse.get_pos()
        rule_mouse_press=py.mouse.get_pressed()
        if back_pos.collidepoint(rule_mouse) and rule_mouse_press[0]:
            screen_val=1
    py.display.update()