from turtle import Turtle
from Parameters import Parameters

class Score(Turtle):
    
    def __init__(self):
        super().__init__()

        #Score Screen
        self.color("white")
        self.penup()
        #Get windows size
        cParam = Parameters()
        self.iScorePos = (cParam.iScreenHeight/2)-25
        self.hideturtle()

    def bPrintScore(self, iScore):
        #Write score 
        self.goto (0, self.iScorePos)
        self.clear()
        self.write(f"Score: {iScore}", align="center", font=("Courier", 12, "normal"))

    def bPrintGameOver(self, iScore):
        #Game Over Message
        self.goto (0, 0)
        self.write(f"GAME OVER!! Score: {iScore}", align="center", font=("Courier", 12, "normal"))
