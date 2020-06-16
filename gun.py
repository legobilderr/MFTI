from random import randrange as rnd, choice
import tkinter as tk
import math
import time




def main():
    global root ,canv,gun,target,screen1, balls, bullet , gun, target 
    root = tk.Tk()
    
    root.geometry('800x600')
    canv = tk.Canvas(root, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    
    target = Target()
    screen1 = canv.create_text(400, 300, text='', font='28')
    gun = Gun()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun.fire2_start)
    canv.bind('<ButtonRelease-1>', gun.fire2_end)
    canv.bind('<Motion>', gun.targetting)


def canvas_clener():
    canv.delete("all")


class Ball():
    def __init__(self, x, y, vx=0, vy=0):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
        
        
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )


    def objekt_id_coords(self):
        self.coordss=canv.coords(self.id)
        return self.coordss
    

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        if self.x+self.vx <0:
            self.vx*=-1
        if self.x+self.vx >800:
            self.vx*=-1
        if self.y-self.vy <0:
            self.vy*=-1
        if self.y-self.vy >590:
            self.vy*=-1   

        self.vy-= 1
        
        if 0<self.x+self.vx<800:
            self.x+=self.vx   
        if 0<self.y-self.vy<600:
            self.y-=self.vy   
        self.set_coords()          

        self.vx -= 0.1 * self.vx / abs(self.vx)
        self.vy -= 0.2 * self.vy / abs(self.vy)

        
        if abs(self.vy)-0.15 < 0  and abs(self.vx)-0.05 < 0  : 
            canv.delete(self.id)
        if abs(self.vx)-0.15 < 0 and abs(self.vy)-1 < 0 :
            canv.delete(self.id)

                  
    def hittest(self,target_coords):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в Targey.init.

        Args:
            target_coords: координаты цели.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        
        
        self.coordss_of_ball=self.objekt_id_coords()
        self.coordss_of_target=target_coords
        try :
            if self.coordss_of_ball[0]>self.coordss_of_target[0] and self.coordss_of_ball[1]>self.coordss_of_target[1] \
                and self.coordss_of_ball[0]<self.coordss_of_target[2] and self.coordss_of_ball[1]<self.coordss_of_target[3]:
                return True
            if self.coordss_of_ball[2]>self.coordss_of_target[0] and self.coordss_of_ball[3]>self.coordss_of_target[1] \
                and self.coordss_of_ball[2]<self.coordss_of_target[2] and self.coordss_of_ball[3]<self.coordss_of_target[3]:
                return True
        except IndexError: 
            return False
        # print("координаты мяча",self.coordss_of_ball)
        # print("координаты цели",self.coordss_of_target)
        return False


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.angl = 1
        self.x=20
        self.y=450
        self.id = canv.create_line(self.x,self.y,50,420,width=7) # FIXME: don't know how to set it...


    def fire2_start(self, event):
        self.f2_on = 1


    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        
        try :
            self.angl = math.atan((event.y-self.y) / (event.x-self.x))
        except ZeroDivisionError :
            event.x+=0.1
        x=20 + max(self.f2_power, 20) * math.cos(self.angl)
        y=450 + max(self.f2_power, 20) * math.sin(self.angl)
        vx = self.f2_power * math.cos(self.angl)
        vy = - self.f2_power * math.sin(self.angl)
        new_ball = Ball(x,y,vx,vy)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10


    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        try :    
            if event:
                self.angl = math.atan((event.y-490) / (event.x-20))
            if self.f2_on:
                canv.itemconfig(self.id, fill='orange')
            else:
                canv.itemconfig(self.id, fill='black')
        except ZeroDivisionError :
            event.x+=0.1
            
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.angl),
                    450 + max(self.f2_power, 20) * math.sin(self.angl)
                    )


    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        global cords_target
        self.points = 0
        self.live = 1
        x = self.x = rnd(600, 780)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        self.id = canv.create_oval(0,0,0,0)
        self.id_points = canv.create_text(30,30,text = self.points,font = '28')
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        cords_target=self.coords_target()
        
        
    def coords_target (self):
        coordss = canv.coords(self.id)
        return coordss


    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)

 
def time_handler():
    target.live = 1
    while target.live or balls:
        for ball in balls:
            ball.move()
            if ball.hittest(cords_target) and target.live:
                target.live = 0
                target.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.bind('<Motion>', '')
                # canvas_clener()
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                
                return
        canv.update()
        time.sleep(0.03)
        gun.targetting()
        gun.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(50, time_handler)

main()

time_handler()
root.mainloop()
