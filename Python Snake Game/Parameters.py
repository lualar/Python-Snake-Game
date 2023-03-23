
class Parameters():
    
    def __init__(self):
        #Program Variables or Constants
        self.sTitle = "my Snake Game - Python"
        self.iScreenWidth = 600   #Future improvement, ask user for screen size??
        self.iScreenHeight = 500
        self.sBackColor = "Black"
        self.iSnakeSize = 20  #Snake Size of pixels

        #Define screen limits
        self.limitX =  (self.iScreenWidth - self.iSnakeSize*2) / 2 #X right
        self.limitX1 = (self.iScreenWidth - self.iSnakeSize*2) / -2     #X left
        self.limitY = (self.iScreenHeight- self.iSnakeSize*2) / 2     #X left
        self.limitY1 = (self.iScreenHeight- self.iSnakeSize*2) / -2     #X left

    def getSnakeSize(self):
        return self.iSnakeSize

    def getScreenLimit(self):
        lLimits = []
        lLimits.append(self.limitX)
        lLimits.append(self.limitX1)
        lLimits.append(self.limitY)
        lLimits.append(self.limitY1)
        return lLimits




