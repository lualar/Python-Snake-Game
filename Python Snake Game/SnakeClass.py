from turtle import Turtle
from Parameters import Parameters

iUP = 90
iDown = 270
iRight = 0
iLeft = 180

class Snake():
    def __init__(self):
        #Paremeter object
        cParam = Parameters()
        
        #Create snake list
        self.theSnakes = []   #Snake array
        #Snake initial parameters
        self.iDistance = cParam.getSnakeSize() #each step  --screen dots
        self.bStartSnake()
        #Get Screen Borders 
        self.lScreenLimits = cParam.getScreenLimit()

    #Create snake
    def fCreateSnake(self):
        #create the Snake at center of the screen
        try:
            for i in range(self.iSnakeLenght):
                #Create a segment (block) for the snake
                self.fAddSegment((self.iSneakHeadPosx-(20*i),0))
        except Exception as ex:
            print (f"Error Snake Creation: {str(ex)}")

    #Create a new segment and addit on tail of the Snake
    def fAddSegment(self, lPosition):
        tempSnake = Turtle("square")
        tempSnake.speed(0)
        tempSnake .penup()
        tempSnake.color(self.sSnakeColor)
        tempSnake.goto(lPosition)
        self.theSnakes.append(tempSnake)

    #move Snake to next position
    def fTracer (self):
        #move snake according with user directions
        for i in range(self.iSnakeLenght-1, 0, -1):
            xTemp = self.theSnakes[i-1].xcor()
            yTemp = self.theSnakes[i-1].ycor()
            self.theSnakes[i].goto(xTemp, yTemp)
        #move forward snake head
        self.theSnakes[0].forward(self.iDistance)

    #Snake Grow (after eat food)
    def fSnakeGrow(self):
        #Add new squeare on tail
        self.fAddSegment(self.theSnakes[-1].position())
        self.iSnakeLenght += 1

    #Functions to move the snake throught the screen
    def moveRight(self):
        if self.iSnakeHeading != "Left":
            self.iSnakeHeading = "Right"    
            self.theSnakes[0].setheading(iRight) 

    def moveLeft(self):
        if self.iSnakeHeading != "Right":
            self.iSnakeHeading = "Left"
            self.theSnakes[0].setheading(iLeft) 

    def turnUp(self):
        if self.iSnakeHeading != "Down":
            self.iSnakeHeading = "Up"
            self.theSnakes[0].setheading(iUP)
                
    def turnDown(self):
        if self.iSnakeHeading != "Up" :
            self.iSnakeHeading = "Down"
            self.theSnakes[0].setheading(iDown)                

    def bStartSnake(self):
        #delete old snake
        for i in self.theSnakes:
            i.goto(1000,1000)

        #restart the Snake
        self.iSnakeLenght = 3  #Initial  snake length 
        self.iSneakHeadPosx  = 0  #Snake Head position
        self.iSneakHeadPosY = 0
        self.sSnakeColor = "White"
        self.iSnakeHeading = "Right"  #Snake direction 'R'ight 'L'eft 'U'p  'D'own -- Initial is 'R'
        self.theSnakes.clear()
        self.fCreateSnake()
