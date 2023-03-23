from turtle import Turtle
from Parameters import Parameters
from highScoreFile import highScoreFile

class Score(Turtle):
    
    def __init__(self):
        super().__init__()

        #Score Screen
        self.color("white")
        self.penup()
        #Get windows size
        cParam = Parameters()
        #Locate Scoreboard on top of the screen
        self.iScorePos = (cParam.iScreenHeight/2)-25    #Ycoordinate
        self.goto (0, self.iScorePos)
        self.hideturtle()

        #Game Score ()
        self.iScore = 0  #Player Score

        #Get HighScore from File
        cHigh =highScoreFile()
        self.iHighScore = cHigh.getHighScore()
        self.bNewHighScore = False

    def bPrintScore(self):
        #Write score 
        #self.clear()
        self.goto (0, self.iScorePos)
        self.write(f"Score: {self.iScore} - High Score {self.iHighScore}", align="center", font=("Courier", 12, "normal"))

    def bPrintGameOver(self):
        #Game Over Message
        self.goto (0, 0)
        self.write(f"Score: {self.iScore} - High Score {self.iHighScore}", align="center", font=("Courier", 12, "normal"))

    def getScore(self):
        return self.iScore

    def updateScore(self, iPoint):
        self.iScore += iPoint
        self.bPrintScore()

    def getHighScore(self):
        return self.iHighScore

    def resetScore(self):
        if self.iScore > self.iHighScore:
            self.iHighScore = self.iScore
            self.bNewHighScore  = True

        self.iScore=0
        self.bPrintScore()
        #Save high score on file
        cHighScore = highScoreFile()
        cHighScore.bSaveFile(self.bNewHighScore, self.iHighScore)
        self.bNewHighScore  = False

