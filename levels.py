

class loadLevel(object):
    def __init__(self,level,win,WSCREEN,HSCREEN):
        self.level = level
        if self.level == 1:
            self.ballStartX = ballStartX = int(WSCREEN/12)
            self.ballStartY = ballStartY = int(11*HSCREEN/12)
            self.ballRadius = ballRadius = 5
            self.ballColour = ballColour = (255,255,255)
            self.ballExist = True
            self.floorSurface = floorSurface = win
            self.floorColour = floorColour = (255,255,255)
            self.floorLeft = floorLeft = 0
            self.floorTop = floorTop =  int(HSCREEN- HSCREEN/12)+ballRadius
            self.floorWidth = floorWidth = WSCREEN
            self.floorHeight = floorHeight = 100
            self.floorExist = True

            self.barrierSurface = barrierSurface = win
            self.barrierColour = barrierColour = (255,255,255)
            self.barrierLeft = barrierLeft = 0
            self.barrierTop = barrierTop =  0
            self.barrierWidth = barrierWidth = 0
            self.barrierHeight = barrierHeight = 0
            self.barrierExist = False

            self.targetSurface = targetSurface = win
            self.targetColour = targetColour = (255,0,0)
            self.targetLeft = targetLeft = 10*WSCREEN/12
            self.targetTop = targetTop =  11*HSCREEN/12
            self.targetWidth = targetWidth = WSCREEN/12
            self.targetHeight = targetHeight = HSCREEN/12
            self.targetExist = True

        if level == 2:
            self.ballStartX = ballStartX = int(WSCREEN/12)
            self.ballStartY = ballStartY = int(11*HSCREEN/12)
            self.ballRadius = ballRadius = int(HSCREEN/50)
            self.ballColour = ballColour = (255,255,0)
            self.ballExist = True

            self.floorSurface = floorSurface = win
            self.floorColour = floorColour = (255,0,255)
            self.floorLeft = floorLeft = 0
            self.floorTop = floorTop =  int(HSCREEN- HSCREEN/12)+ballRadius
            self.floorWidth = floorWidth = WSCREEN
            self.floorHeight = floorHeight = HSCREEN/10
            self.floorExist = True

            self.barrierSurface = barrierSurface = win
            self.barrierColour = barrierColour = (255,255,255)
            self.barrierLeft = barrierLeft = 10*WSCREEN/12
            self.barrierTop = barrierTop =  8*HSCREEN/12
            self.barrierWidth = barrierWidth = WSCREEN/12
            self.barrierHeight = barrierHeight = 4*HSCREEN/12
            self.barrierExist = True

            self.targetSurface = targetSurface = win
            self.targetColour = targetColour = (255,0,0)
            self.targetLeft = targetLeft = 10*WSCREEN/12
            self.targetTop = targetTop =  8*HSCREEN/12 - HSCREEN/100
            self.targetWidth = targetWidth = WSCREEN/12
            self.targetHeight = targetHeight = HSCREEN/100
            self.targetExist = True

    def ballAttrib(self):
        ballAttrib = [self.ballStartX, self.ballStartX, self.ballRadius , self.ballColour, None, self.ballExist]
        return ballAttrib

    def floorAttrib(self):
        floorAttrib = [self.floorSurface, self.floorColour, self.floorLeft, self.floorTop, self.floorWidth, self.floorHeight, self.floorExist] #(surface, colour, left, top, width, height)
        return floorAttrib

    def barrierAttrib(self):
        barrierAttrib = [self.barrierSurface, self.barrierColour, self.barrierLeft, self.barrierTop, self.barrierWidth, self.barrierHeight, self.barrierExist] #(surface, colour, left, top, width, height)
        return barrierAttrib

    def targetAttrib(self):
        targetAttrib = [self.targetSurface, self.targetColour, self.targetLeft, self.targetTop, self.targetWidth, self.targetHeight, self.targetExist] #(surface, colour, left, top, width, height)
        return targetAttrib
'''
    if level == 1:
        print(level)

        floorAttrib = [win, (255,255,255), 0, STARTY+proj.radius, WSCREEN, 100] #(surface, colour, left, top, width, height)
        barrierAttrib = [win, (255,255,255), WSCREEN, HSCREEN-100, 500, 50, None] #(surface, colour, left, top, width, height, image)
        targetAttrib = [win, (255,0,0), WSCREEN/4, STARTY, 10, 50, None]
        obstacles=[floor, barrier, target]
        return ballAttrib,floorAttrib,barrierAttrib,targetAttrib,obstacles
'''
