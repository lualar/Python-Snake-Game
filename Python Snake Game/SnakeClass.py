from tempfile import tempdir
from turtle import Turtle

iUP = 90
iDown = 270
iRight = 0
iLeft = 180

class Snake:
    def __init__(self):
        #Snake initial parameters
        self.iSnakeLenght = 3  #Initial  snake length 
        self.iDistance = 20  #each step  --screen dots
        self.iSneakHeadPosx  = 0  #Snake Head position
        self.iSneakHeadPosY = 0
        self.sSnakeColor = "White"
        self.iSnakeHeading = "R"  #Snake direction 'R'ight 'L'eft 'U'p  'D'own -- Initial is 'R'
        #Create snake list
        self.theSnakes = []   #Snake array
        self.fCreateSnake()

    #Create snake
    def fCreateSnake(self):
        #create the Snake at center of the screen
        try:
            for i in range(self.iSnakeLenght):
                tempSnake = Turtle("square")
                tempSnake .penup()
                tempSnake.color(self.sSnakeColor)
                self.theSnakes.append(tempSnake)
                self.fSnakeCoordinates(oSnake=tempSnake, iPosX=self.iSneakHeadPosx, iPosY= self.iSneakHeadPosY, iDeltaX= self.iSneakHeadPosx-(20*i), iDeltaY=self.iSneakHeadPosY)
        except Exception as ex:
            print (f"Error Snake Creation: {str(ex)}")

    #move Snake to next position
    def fTracer (self):
        #move snake according with user directions
        for i in range(self.iSnakeLenght-1, 0, -1):
            xTemp = self.theSnakes[i-1].xcor()
            yTemp = self.theSnakes[i-1].ycor()
            self.fSnakeCoordinates (self.theSnakes[i], iPosX=xTemp, iPosY=yTemp)
        #move forward snake head
        self.theSnakes[0].forward(self.iDistance)

    #locate snake @ screen
    def fSnakeCoordinates(self, oSnake, iPosX, iPosY, iDeltaX=0, iDeltaY=0):
        try:
            oSnake.goto(iPosX + iDeltaX, iPosY + iDeltaY)
            oSnake.setx(iPosX + iDeltaX)
            oSnake.sety(iPosY + iDeltaY)
        except Exception as ex:
            print (f"Error Snake Coordinates: {str(ex)}")

    #Functions to move the snake throught the screen
    def moveRight(self):
        if self.iSnakeHeading != iLeft:
            self.iSnakeHeading = "R"    
            self.theSnakes[0].setheading(iRight) 

    def moveLeft(self):
        if self.iSnakeHeading != iRight :
            self.iSnakeHeading = "L"
            self.theSnakes[0].setheading(iLeft) 

    def turnUp(self):
        if self.iSnakeHeading != iDown:
            self.iSnakeHeading = "U"
            self.theSnakes[0].setheading(iUP)
                
    def turnDown(self):
        if self.iSnakeHeading != iUP :
            self.iSnakeHeading = "D"
            self.theSnakes[0].setheading(iDown)                

