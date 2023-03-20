from turtle import Turtle
from Parameters import Parameters

iUP = 90
iDown = 270
iRight = 0
iLeft = 180

class Snake():
    def __init__(self):
        cParam = Parameters()
        #Snake initial parameters
        self.iSnakeLenght = 3  #Initial  snake length 
        self.iDistance = cParam.getSnakeSize() #each step  --screen dots
        self.iSneakHeadPosx  = 0  #Snake Head position
        self.iSneakHeadPosY = 0
        self.sSnakeColor = "White"
        self.iSnakeHeading = "R"  #Snake direction 'R'ight 'L'eft 'U'p  'D'own -- Initial is 'R'
        #Create snake list
        self.theSnakes = []   #Snake array
        self.fCreateSnake()

        #Get Screen Borders 
        self.lScreenLimits = cParam.getScreenLimit()

    #Create snake
    def fCreateSnake(self):
        #create the Snake at center of the screen
        try:
            for i in range(self.iSnakeLenght):
                tempSnake = Turtle("square")
                tempSnake .penup()
                tempSnake.color(self.sSnakeColor)
                tempSnake.speed("fastest")
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
            oSnake
            oSnake.goto(iPosX + iDeltaX, iPosY + iDeltaY)
            oSnake.setx(iPosX + iDeltaX)
            oSnake.sety(iPosY + iDeltaY)
        except Exception as ex:
            print (f"Error Snake Coordinates: {str(ex)}")

    #Snake Grow (after eat food)
    def fSnakeGrow(self):
        #Add new squeare on tail
        try:
            #New Square
            tempSnake = Turtle("square")
            tempSnake.penup()
            tempSnake.speed("fastest")
            tempSnake.color("black")  #Initially create tail on black to hide it

            #Current Tail Location
            xPos = self.theSnakes[self.iSnakeLenght-1].xcor()
            yPos = self.theSnakes[self.iSnakeLenght-1].ycor()

            #new tail location
            if self.iSnakeHeading == "Left":
                #Validate Snake is not in right border
                if xPos+20 < self.lScreenLimits[0]:
                    xPos += 20
                #Validate Snake tail is not in upper border
                elif yPos + 20 < self.lScreenLimits[2]:
                    yPos += 20
                #Otherwise snake tail is on upper border
                else:
                    ypos -= 20
            elif self.iSnakeHeading == "Right":
                #Validate Snake is not in left border
                if xPos-20 < self.lScreenLimits[1]:
                    xPos -= 20
                #Validate Snake tail is not in upper border
                elif yPos + 20 < self.lScreenLimits[2]:
                    yPos += 20
                #Otherwise snake tail is on upper border
                else:
                    ypos -= 20
            elif self.iSnakeHeading == "UP":
                #Validate Snake is not in Upper border
                if yPos+20 < self.lScreenLimits[2]:
                    YPos += 20
                #Validate Snake tail is not in right border
                elif xPos + 20 < self.lScreenLimits[0]:
                    xPos += 20
                #Otherwise snake tail is on left border
                else:
                    xpos -= 20
            else: #Down
                #Validate Snake is not in Upper border
                if yPos-20 < self.lScreenLimits[3]:
                    YPos += 20
                #Validate Snake tail is not in right border
                elif xPos + 20 < self.lScreenLimits[0]:
                    xPos += 20
                #Otherwise snake tail is on left border
                else:
                    xpos -= 20

            #Add new square to snake chain
            self.theSnakes.append(tempSnake)
            self.iSnakeLenght += 1

            #locate new square on screen
            self.fSnakeCoordinates(tempSnake, iPosX=xPos, iPosY= yPos, iDeltaX=0, iDeltaY=0)
            #Show the new tail
            self.theSnakes[self.iSnakeLenght-1].color(self.sSnakeColor)

        except Exception as ex:
            print (f"Error Snake Grow: {str(ex)}")

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

