import pygame as py
import random
import time
random.seed(time.time())
from sys import exit
py.init()
size=4
Target=2048
screen=py.display.set_mode((400,400))
def move_counter():
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
        
    def display(self):
        for i in self:
            print(i)
    def which_spawn_val(self):
        p1=random.randint(1,2)
        p2=random.randint(1,2)
        if p1==p2 and p1==2:
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
    def up(self):
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

    def left(self):
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
                    if self.data[i][j]==self.data[i+1][j] or self.data[i][j]==self.data[i][j+1]:
                        return False
        return True
    def win_check(self):
        for i in range(size):
                for j in range(size):
                    if self.data[i][j]==Target:
                        return True
        return False
x_pos=83
y_pos=67
py.display.set_caption("Hello World")
clock=py.time.Clock()
font_style=py.font.Font('...assets/DS-DIGI.TTF',50)
font_style1=py.font.Font('2024_final/assets/DS-DIGI.TTF',25)
background=py.image.load("2024_final/assets/background.png")
menu=py.image.load("2024_final/assets/main_menue.png")
win_screen=py.image.load("2024_final/assets/won1.png")
rules_screen=py.image.load("2024_final/assets/rules.png")
lost_screen=py.image.load("2024_final/assets/lost.png")
back=py.image.load("2024_final/assets/back.png")
start=py.Rect(145,218,72,30)
rules=py.Rect(145,259,72,37)
continu=py.Rect(136,177,104,30)
back_pos=py.Rect(3,367,60,30)
screen_val=1
spare=Board()
spare_move=0
while True:
    for event in py.event.get():    
        if event.type==py.QUIT:
            py.quit()
            exit()
        if event.type==py.KEYDOWN:
            if event.key==py.K_w and screen_val==2:
                game_board.up()
                move_number+=move_counter()
            elif event.key==py.K_s and screen_val==2:
                temp=game_board.revers()
                temp.up()
                game_board=temp.revers()
                move_number+=move_counter()
            elif event.key==py.K_a and screen_val==2:
               game_board.left()
               move_number+=move_counter()
            elif event.key==py.K_d and screen_val==2:
               temp=game_board.turn()
               temp.left()
               game_board=temp.turn()
               move_number+=move_counter()
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
        for i in range(4):
            for j in range(4):
                screen.blit(font_style.render(str(game_board.data[i][j]),True,'black'),(x_pos,y_pos))
                x_pos+=70
            y_pos+=70
            x_pos=83
        x_pos=83
        y_pos=67
        clock.tick(60)
        screen.blit(font_style1.render("Move number: "+str(move_number),True,'blue'),(10,10))
        if game_board.lost_check():
            screen.blit(lost_screen,(0,0))
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