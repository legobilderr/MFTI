from graph import *


#стена
brushColor(151,121,25)
rectangle(0, 0, 500, 300)
brushColor(186,159,69)
rectangle(0, 300, 500, 600)

#окно
brushColor(183,239,253)
rectangle(260, 10, 490, 290)
# в окне 
brushColor(108,208,233)
rectangle(270, 20, 370, 97)
rectangle(380, 20, 480, 97)
rectangle(380, 107, 480, 280)
rectangle(270, 107, 370, 280)



#я не мтал создавать хвост элипс 
def kat (x,y,size,colors=(213,125,37)):
    def bdy ():
        brushColor(colors)
        oval(x,y,(x-size*2),(y-size))
        oval(x-(size+size/2),y+size,x-size*7,y-size*2)
        circle(x-size*3*0.8, y+size/2, size*0.8)
        oval(x-size*1.9,y+size/2,x-size*1.3,y+size*2)
        oval(x-size*7,y+size/4,x-size*5.5,y+size)
        oval(x-size*7.5,y-size*1.5,x-size*6.8,y+size/4)
        #голова 
        oval(x-size*8,y-size*2,x-size*5.5,y+size/6)
        polygon([(x-size*7.7,y-size*1.4),(x-size*7.8,y-size*2.3),(x-size*7.3,y-size*1.8),(x-size*7.7,y-size*1.4)])
        polygon([(x-size*5.9,y-size*1.4),(x-size*5.8,y-size*2.3),(x-size*6.3,y-size*1.8),(x-size*5.9,y-size*1.4)])
        def ears ():
            brushColor(242,177,177)
            polygon([(x-size*7.65,y-size*1.5),(x-size*7.75,y-size*2.2),(x-size*7.38,y-size*1.8),(x-size*7.65,y-size*1.5)])
            polygon([(x-size*5.95,y-size*1.5),(x-size*5.85,y-size*2.2),(x-size*6.25,y-size*1.8),(x-size*5.95,y-size*1.5)])
        ears()    
        def eye ():
            brushColor(75,210,75)
            circle(x-size*7.27, y-size, size*0.33)
            circle(x-size*6.27, y-size, size*0.33)
            brushColor(0,0,0)
            oval(x-size*7.2, y-size*1.27,x-size*7.1,y-size/1.4)
            oval(x-size*6.2, y-size*1.27,x-size*6.1,y-size/1.4)
            brushColor(255,255,255)
            circle(x-size*7.35,y-size*1.2,size*0.1)
            circle(x-size*6.35,y-size*1.2,size*0.1)
        eye()
        brushColor(242,177,177)
        polygon([(x-size*6.77,y-size*0.5),(x-size*6.97,y-size*0.7),(x-size*6.57,y-size*0.7),(x-size*6.77,y-size*0.5)])
        line(x-size*6.77,y-size*0.5,x-size*6.77,y-size*0.25)
        x1=x-size*6.77
        y1=y-size*0.4
        x2=x-size*7.1
        y2=y-size*0.12
        arc(x1,y1,x2,y2,180,360,[ARC])
        x3=x-size*6.43
        arc(x1,y1,x3,y2,180,360,[ARC])
        def duga(xstart, xmax, xstep, ystart, ystep, yincrease):
        #""" Функция рисует округлые(дуги), в зависимости
		#от переданных значений шагов для координат X и Y. Координаты увеличиваются не
		#в равной степени, за что отвечает параметр yincrease. 
            points_duga = []
            if xstart > xmax:#левые усы 
                while xstart > xmax  :
                    points_duga.append((xstart, ystart))
                    xstart -= xstep
                    ystart += ystep
                    xstep += yincrease
                print(points_duga)
                return points_duga
            else:#правые усы 
                while xstart < xmax  :
                    points_duga.append((xstart, ystart))
                    xstart += xstep
                    ystart += ystep
                    xstep += yincrease
                              
                print(points_duga)
                return points_duga
        polyline(duga(x-size*7,x-size*9,1,y-size*0.4,-1,0.2))
        polyline(duga(x-size*7,x-size*9,0.9,y-size*0.3,-1,0.4))
        polyline(duga(x-size*7,x-size*9,0.8,y-size*0.25,-1,1))
        polyline(duga(x-size*6.5,x-size*4.5,1,y-size*0.4,-1,0.2))
        polyline(duga(x-size*6.5,x-size*4.5,1,y-size*0.3,-1,0.4))
        polyline(duga(x-size*6.5,x-size*4.5,1,y-size*0.25,-1,1))
    bdy()
def booll(x,y,size,colors=(192, 192, 192)):
    brushColor(colors)
    circle(x, y, size)
    def nitki(xstart,xstep,xmax,ystart,ystep,ymax):
        point=[]
        while xstart<xmax and ystart<ymax:
            point.append((xstart,ystart))
            xstart+=xstep
            ystart+=ystep
            ystep+=ystep*2
        print(point)
        return point
    polyline(nitki(x-size/2,3,x+size/2,y-size/2,0.01,y+size/2))
    polyline(nitki(x-size/1.6,3,x+size/2,y-size/2.3,0.01,y+size/2))
    polyline(nitki(x-size/1.4,3,x+size/2,y-size/3.1,0.01,y+size/2))
    def nitki2(xstart,xstep,xmax,ystart,ystep,ymax,dopstep):
        point=[]
        while xstart<xmax and ystart>ymax:
            point.append((xstart,ystart))
            xstart+=xstep
            ystart-=ystep
            ystep+=dopstep
        print(point)
        return point
    polyline(nitki2(x-size/2.4,6,x+size*1.7,y+size*0.7,1,y-size/2.5,2))
    polyline(nitki2(x-size/2.6,6,x+size*1.7,y+size*0.9,1,y-size/2.5,2))
    polyline(nitki2(x-size/7,6,x+size*1.7,y+size*1,1,y-size/2.5,2))

def kat1 (x,y,size,colors=(213,125,37)):
    def bdy ():
        brushColor(colors)
        oval(x-size*0.9,y,(x+size*2),(y-size))
        oval(x+(size-size/2),y+size,x+size*7,y-size*2)
        circle(x+size*3*0.8, y+size/2, size*0.8)
        oval(x+size*1.9,y+size/2,x+size*1.3,y+size*2)
        oval(x+size*7,y+size/4,x+size*5.5,y+size)
        oval(x+size*7.5,y-size*1.5,x+size*6.8,y+size/4)
        #голова 
        oval(x+size*8,y-size*2,x+size*5.5,y+size/6)
        polygon([(x+size*7.7,y-size*1.4),(x+size*7.8,y-size*2.3),(x+size*7.3,y-size*1.8),(x+size*7.7,y-size*1.4)])
        polygon([(x+size*5.9,y-size*1.4),(x+size*5.8,y-size*2.3),(x+size*6.3,y-size*1.8),(x+size*5.9,y-size*1.4)])
        def ears ():
            brushColor(242,177,177)
            polygon([(x+size*7.65,y-size*1.5),(x+size*7.75,y-size*2.2),(x+size*7.38,y-size*1.8),(x+size*7.65,y-size*1.5)])
            polygon([(x+size*5.95,y-size*1.5),(x+size*5.85,y-size*2.2),(x+size*6.25,y-size*1.8),(x+size*5.95,y-size*1.5)])
        ears()
        def eye ():
            brushColor(75,210,75)
            circle(x+size*7.27, y-size, size*0.33)
            circle(x+size*6.27, y-size, size*0.33)
            brushColor(0,0,0)
            oval(x+size*7.2, y-size*1.27,x+size*7.1,y-size/1.4)
            oval(x+size*6.2, y-size*1.27,x+size*6.1,y-size/1.4)
            brushColor(255,255,255)
            circle(x+size*7.35,y-size*1.2,size*0.1)
            circle(x+size*6.35,y-size*1.2,size*0.1)
        eye()
        brushColor(242,177,177)
        polygon([(x+size*6.77,y-size*0.5),(x+size*6.97,y-size*0.7),(x+size*6.57,y-size*0.7),(x+size*6.77,y-size*0.5)])
        line(x+size*6.77,y-size*0.5,x+size*6.77,y-size*0.25)
        x1=x+size*6.77
        y1=y-size*0.4
        x2=x+size*7.1
        y2=y-size*0.12
        arc(x1,y1,x2,y2,180,360,[ARC])
        x3=x+size*6.43
        arc(x1,y1,x3,y2,180,360,[ARC])
        def duga(xstart, xmax, xstep, ystart, ystep, yincrease):
        #""" Функция рисует округлые(дуги), в зависимости
		#от переданных значений шагов для координат X и Y. Координаты увеличиваются не
		#в равной степени, за что отвечает параметр yincrease. 
            points_duga = []
            if xstart > xmax:#левые усы 
                while xstart > xmax  :
                    points_duga.append((xstart, ystart))
                    xstart -= xstep
                    ystart += ystep
                    xstep += yincrease
                print(points_duga)
                return points_duga
            else:#правые усы 
                while xstart < xmax  :
                    points_duga.append((xstart, ystart))
                    xstart += xstep
                    ystart += ystep
                    xstep += yincrease
                              
                print(points_duga)
                return points_duga
        polyline(duga(x+size*7,x+size*9,1,y-size*0.4,-1,0.2))
        polyline(duga(x+size*7,x+size*9,0.9,y-size*0.3,-1,0.4))
        polyline(duga(x+size*7,x+size*9,0.8,y-size*0.25,-1,1))
        polyline(duga(x+size*6.5,x+size*4.5,1,y-size*0.4,-1,0.2))
        polyline(duga(x+size*6.5,x+size*4.5,1,y-size*0.3,-1,0.4))
        polyline(duga(x+size*6.5,x+size*4.5,1,y-size*0.25,-1,1)) 
        
    bdy()



kat(500,410,50)
kat1(20,490,20,'grey')

kat(200,300,10,'black')

booll(300,520,40)
booll(50,250,70,'green')

a=windowSize()
print(a)
run()








