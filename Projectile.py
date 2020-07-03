import pygame
import math
import tkinter
import numpy


WSCREEN = 1200
HSCREEN = 500
FPS = 60
CLOCK = pygame.time.Clock()
GRAVITY = 9.8
WSCALE = WSCREEN/12
HSCALE = HSCREEN/12

STARTX = int(WSCALE)
STARTY = int(HSCREEN - HSCALE)

TIMEINCREMENT = 0.2

TWEAK = 7.5

win = pygame.display.set_mode((WSCREEN, HSCREEN))

class ball(object):
    def __init__(self, x, y, radius, colour, image = None):
        self.x = x = WSCREEN/12
        self.y = y = 11*HSCREEN/12
        self.xDisplay = 10 - ((WSCREEN - self.x - WSCALE))/(WSCALE) # EXPRESSES x Position in terms of Scale
        self.yDisplay = ((HSCREEN - self.y - HSCALE))/(HSCALE)
        self.V0yDisplay = 0
        self.V0xDisplay = 0
        #self.yDisplay = yDisplay = 0
        self.radius = radius
        self.colour = colour
        self.image = image

    def draw(self, win):
        self.x = int(self.x)
        self.y = int(self.y)
        pygame.draw.circle(win, (0,0,255), (self.x,self.y), self.radius)
        pygame.draw.circle(win, self.colour, (self.x,self.y), self.radius-1)
        if self.image != None:
            win.blit(pygame.image.load(self.image), (self.x,self.y))

    def ballPath(self, startx, starty, pos, angle, time, GRAVITY):
        velx = math.cos(angle) * V0
        vely = math.sin(angle) * V0

        distX = velx * time
        distY = (vely * time) + ((-GRAVITY * (time)**2)/2)

        newX = round(distX + startx)
        newY = round(starty - distY)

        return(newX, newY)
'''
    def maxHeight(y, GRAVITY, ang):
        V0 = math.sqrt((abs(line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2))/8
        maxY = int((((math.sin(angle) * V0)**2)/(2*GRAVITY))*100)
        return(maxY)
'''

class UI(object):
    def __init__(self=None, pos=None):
        self.pos = pos
        self.MouseX = self.pos[0]
        self.MouseY = self.pos[1]
        self.V0x = abs(self.MouseX - proj.x)
        self.V0xDisplay = self.V0x/WSCALE
        #print(self.V0xDisplay)
        self.V0y = abs(self.MouseY - proj.y)
        self.V0yDisplay = self.V0y/HSCALE
        #self.V0Displayalt = math.sqrt((self.V0y/HSCALE)**2+(self.V0x/WSCALE)**2)

        self.V0DisplayOG = math.sqrt(self.V0yDisplay**2+self.V0xDisplay**2)
        #print("SQRT: ",self.V0DisplayOG)
        self.V0Display = self.V0xDisplay/math.cos(findAngle(pos))
        #print("COS: ",self.V0Display)
        self.V0Displaysin = self.V0yDisplay/math.sin(findAngle(pos))
        #print("SIN: ",self.V0Displaysin)
        self.V0Displayfix = math.sqrt(self.V0x**2+self.V0y**2)
        #print("FIX:",self.V0Displayfix)
        self.V0 = math.sqrt(self.V0y**2+self.V0x**2)

        self.xMax = ((self.V0**2)*math.sin(2*findAngle(pos)))/GRAVITY
        self.xMaxDisplay = self.xMax/WSCALE

        self.font = pygame.font.SysFont("comicsansms", 32)
        self.V0xText = self.font.render("V0x: "+str(self.V0xDisplay), True, (0, 128, 0))
        self.V0yText = self.font.render("V0y: "+str(self.V0yDisplay), True, (0, 128, 0))
        self.V0Text = self.font.render("V0: "+str(self.V0Display), True, (0, 128, 0))
        self.RadText = self.font.render("Angle: "+str(int((findAngle(pos)/math.pi)*100)/100)+"π", True, (0, 128, 0))
        self.DegText = self.font.render("Angle: "+str(int(findAngle(pos)*(180/math.pi)))+" °", True, (0, 128, 0))
        #self.maxYText = self.font.render("Max Height: "+str(proj.maxHeight(proj.y,GRAVITY)), True, (0, 128, 0))
        self.yText = self.font.render("y: "+str(proj.yDisplay), True, (0, 128, 0))
        self.xText = self.font.render("x: "+str(proj.x), True, (0, 128, 0))
    def drawBackground(self, WSCREEN,HSCREEN):
        colour = (0, 128, 0)
        yPos = HSCREEN - HSCALE
        xPos = WSCALE
        length = 10
        self.font = pygame.font.SysFont("comicsansms", 10)

        for i in range(length+1):
            win.blit(self.font.render(str(i)+"m", True, colour),((i+1)*WSCALE,yPos))

            win.blit(self.font.render(str(length - i)+"m", True, colour),(xPos,(i+1)*HSCALE))
    def drawRange(self):
        self.font = pygame.font.SysFont("comicsansms", 10)
        colour = (0, 128, 0)
        win.blit(self.font.render("Range: "+str(self.xMax), True, colour),(200,40))
        win.blit(self.font.render("Range: "+str(self.xMaxDisplay), True, colour),(200,100))
        pygame.draw.line(win, colour, (self.xMaxDisplay*WSCALE+WSCREEN/12+proj.x/WSCALE,10), (self.xMaxDisplay*WSCALE+WSCREEN/12+proj.x/WSCALE,HSCREEN), 2)

class wall(object):
    def __init__(self, surface, colour, left, top, width, height, image = None):
        self.surface = surface
        self.colour = colour
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.image = image

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, pygame.Rect(self.left, self.top, self.width, self.height))
        if self.image != None:
            win.blit(pygame.image.load(self.image), (self.left,self.top))
def drawDash(surf, color, start_pos, end_pos, width=1, dash_length=10):
    start_pos = list(start_pos)
    start_pos[1] = int(start_pos[1])
    x1, y1 = start_pos

    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c
        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

def redrawWindow(shoot,obstacles):
    win.fill((0,64,64))
    proj.draw(win)
    try:
        if floor in obstacles:
            floor.draw()
    except:
        None
    try:
        if barrier in obstacles:
            barrier.draw()
    except:
        None
    try:
        if target in obstacles:
            target.draw()
    except:
        None

    display = UI(pos)
    display.drawBackground(WSCREEN,HSCREEN)
    if shoot == False:
        display.drawRange()

    win.blit(display.yText,(WSCREEN-WSCALE,HSCREEN/24))
    win.blit(display.xText,(WSCREEN-WSCALE*2,HSCREEN/10))
    if shoot == False:
        pygame.draw.line(win, (255,255,255), line[0], line[1])
        #pygame.draw.line(win, (255,255,255), xLine[0], xLine[1])
        drawDash(win, (255,255,255), xLine[0], xLine[1], width=1, dash_length=10)
        drawDash(win, (255,255,255), yLine[0], yLine[1], width=1, dash_length=10)


        win.blit(display.V0xText,((pos[0]/2)-50,xLine[0][1]-50))
        win.blit(display.V0yText,(pos[0],(pos[1])))
        win.blit(display.V0Text,(pos[0]-100,(pos[1]-100)))
        win.blit(display.RadText,(WSCREEN-WSCREEN/2,HSCREEN/6))
        win.blit(display.DegText,(WSCREEN-WSCREEN/2,HSCREEN/4))
        #win.blit(display.maxYText,(0,120))

    if shoot == True:
        display = UI(pos)
        if doObjsOverlap(proj, target):
            winText = self.font.render("BIG WIN", True, (0, 128, 0))
            win.blit(winText,((pos[0]/2)-50,xLine[0][1]-50))

    pygame.display.update()

def findAngle(pos):
    sX = proj.x/WSCALE -1
    sY = ((HSCREEN-proj.y)/HSCALE -1)
    mY = 11 - pos[1]/HSCALE
    mX = pos[0]/WSCALE - 1
    try:
        angle = math.atan((sY - mY) / (sX - mX))
    except:
        angle = math.pi / 2

    if mY < sY and mX > sX:
        angle = abs(angle)
    elif mY < sY and mX < sX:
        angle = math.pi - angle
    elif mY > sY and mX < sX:
        angle = math.pi + abs(angle)
    elif mY > sY and mX > sX:
        angle = (math.pi * 2) - angle
    angle = 2*math.pi - angle
    return angle

def findVelocity(line):
    V0 = math.sqrt(((line[1][1] - line[0][1]))**2 + ((line[1][0] - line[0][0]))**2)
    return V0


def doObjsOverlap(proj, obstacle):
    if proj.x > obstacle.left - proj.radius and proj.x < obstacle.left + obstacle.width + proj.radius and proj.y > obstacle.top - proj.radius and proj.y < obstacle.height + obstacle.top + proj.radius :
        return True

    else:
        return False


def callLevel(level):
    loadedLevel = levels.loadLevel(level,win,WSCREEN,HSCREEN)
    ballAttrib = loadedLevel.ballAttrib()
    floorAttrib = loadedLevel.floorAttrib()
    barrierAttrib = loadedLevel.barrierAttrib()
    targetAttrib = loadedLevel.targetAttrib()
    return loadedLevel, ballAttrib, floorAttrib, barrierAttrib,targetAttrib

def exitTk():
    window.destroy()

def setLevel(lvl):
    global level
    level = lvl
#Class creation and appending to list of obstacles


import levels
window = tkinter.Tk()
window.title("MENU")
menuLoop = True

if menuLoop:
    tkinter.Button(window, text = "Level 1", command=lambda:[callLevel(1),exitTk(),setLevel(1)]).pack()
    tkinter.Button(window, text = "Level 2", command=lambda:[callLevel(2),exitTk(),setLevel(2)]).pack()
    menuLoop = False
    window.mainloop()

Attribs = callLevel(level)
ballAttrib = Attribs[1]
floorAttrib = Attribs[2]
barrierAttrib = Attribs[3]
targetAttrib = Attribs[4]


if not menuLoop:
    obstacles = []
    #print(ballAttrib)
    if ballAttrib[5] == True:
        proj = ball(ballAttrib[0], ballAttrib[1], ballAttrib[2] , ballAttrib[3], ballAttrib[4])
    if floorAttrib[6] == True:
        floor = wall(floorAttrib[0], floorAttrib[1], floorAttrib[2] , floorAttrib[3], floorAttrib[4], floorAttrib[5]) #(surface, colour, left, top, width, height)
        obstacles.append(floor)
    if barrierAttrib[6] == True:
        barrier = wall(barrierAttrib[0], barrierAttrib[1], barrierAttrib[2] , barrierAttrib[3], barrierAttrib[4], barrierAttrib[5]) #(surface, colour, left, top, width, height, image)
        obstacles.append(barrier)
    if targetAttrib[6] == True:
        target = wall(targetAttrib[0], targetAttrib[1], targetAttrib[2] , targetAttrib[3], targetAttrib[4], targetAttrib[5]) #(surface, colour, left, top, width, height, image)
        obstacles.append(target)

pygame.init()

run = True
while run:
    for obstacle in obstacles:
        if doObjsOverlap(proj, obstacle):
                proj.y -= proj.radius
                proj.x -= proj.radius
                shoot = False

    if shoot:
        if -HSCREEN < proj.y < HSCREEN:
            time += TIMEINCREMENT
            po = proj.ballPath(x,y,V0,angle,time,GRAVITY)
            proj.x = po[0]
            proj.y = po[1]

            proj.xDisplay = 10 - ((WSCREEN - proj.x - WSCALE))/(WSCALE)
            proj.yDisplay = ((HSCREEN - proj.y - HSCALE))/(HSCALE)

        else:
            shoot = False
            proj.y = HSCREEN - proj.radius
    if not shoot:
        proj.x = int(WSCALE)
        proj.y = int(HSCREEN - HSCALE)

    pos = pygame.mouse.get_pos()
    line = [(proj.x, proj.y), pos]

    xLine = [(proj.x, proj.y), (pos[0],proj.y)]
    yLine = [(pos[0], proj.y), pos]

    redrawWindow(shoot,obstacles)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = proj.x
                y = proj.y
                time = 0
                V0 = findVelocity(line)
                #print("V0: ",V0)
                angle = findAngle(pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                proj.x = int(WSCALE)
                proj.y = int(HSCREEN - HSCALE)


    CLOCK.tick(FPS)

pygame.quit()
