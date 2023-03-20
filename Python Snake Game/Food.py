from turtle import Turtle
import random
from Parameters import Parameters

class Food(Turtle):

    def __init__(self):
        #Initialize food class and parameters
        super().__init__()

        #Get windows size
        cParam = Parameters()

        #get a position inside screen border limits
        self.iScreenLimits = cParam.getScreenLimit()
        
        #Food paramenters and shape
        self.penup()
        self.iSize= 10 
        self.shapesize(stretch_len = 0.5, stretch_wid=0.5)
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.fFoodRefresh()

    def fFoodRefresh(self) :
        self.color("yellow")
        #Get new food coordinates
        self.iRandomX = random.randint(self.iScreenLimits[1], self.iScreenLimits[0])
        self.iRandomY = random.randint(self.iScreenLimits[3], self.iScreenLimits[2])
        self.goto(self.iRandomX, self.iRandomY)

