import time
from SnakeClass import Snake
from turtle import Screen
from Parameters import Parameters
from Food import Food
from Score import Score

#Game Status Control
bGameIsOn = False
cParam = Parameters()
cScore = Score()

#Create the screen
theScreen = Screen()
theScreen.tracer(0)
theScreen.setup(width=cParam.iScreenWidth, height=cParam.iScreenHeight)

#Clear the screen after each movement
def fCleanScreen(theScreen):
    theScreen.clearscreen()
    theScreen.bgcolor(cParam.sBackColor)
    theScreen.title(f"{cParam.sTitle}")
      
def bDetectFoodCollition(cSnakeHead):
    #validate if Snake Head  position is same of food point
    if cSnakeHead.distance(cFood) < cParam.iSnakeSize-5:
        cFood.fFoodRefresh()
        cSnake.fSnakeGrow()
        return True
    return False

def bDetectBorder(cSnakeHead, lScreenLimits):
    #Snake Head Position -- Tuple (x,y)
    tCurrentPosition = cSnakeHead.pos()

    #validate if Snake Head  position is same of food point
    if (tCurrentPosition[0] >= lScreenLimits[0]) or (tCurrentPosition[0] <= lScreenLimits[1]) or (tCurrentPosition[1] >= lScreenLimits[2]) or (tCurrentPosition[1] <= lScreenLimits[3]):
        return True

    #If not border return false, game continues
    return False

def bDetectCollitionWithBody(cSnakeHead):

    #validate if head is on same position of any other square of the Snake
    for segment in cSnake.theSnakes[1:]:
        if cSnakeHead.distance(segment) < 10:
            return True
    #If not game continues
    return False

#Game Status Control
fCleanScreen(theScreen)
print ("\nGame Start")
bGameIsOn = True

#create snake object
cSnake = Snake()
cFood = Food()
cParam = Parameters()
cScore = Score()
cScore.bPrintScore()

#Screen and Key events assigment 
theScreen.listen()
theScreen.onkey(key="Up",fun=cSnake.turnUp)   #This is a sample of a higher order function
theScreen.onkey(key="Down",fun=cSnake.turnDown)   #This is a sample of a higher order function
theScreen.onkey(key="Left",fun=cSnake.moveLeft)   #This is a sample of a higher order function
theScreen.onkey(key="Right",fun=cSnake.moveRight)   #This is a sample of a higher order function

#Get Screen Borders 
lScreenLimits = cParam.getScreenLimit()

#Snake walk through screen
while bGameIsOn:
    theScreen.update()
    #time.sleep(0.1)
    cSnake.fTracer()

    #Detect Collition
    if bDetectFoodCollition(cSnake.theSnakes[0]):
        #Increment Score
        cScore.updateScore(1)

    #If snake head collides with square border
    if bDetectBorder(cSnake.theSnakes[0], lScreenLimits):
        cScore.resetScore()
        #ReStart the Snake
        cSnake.bStartSnake()
        #bGameIsOn = False

    #If snake head collides with its own body
    if bDetectCollitionWithBody(cSnake.theSnakes[0]):
        cScore.resetScore()
        #ReStart the Snake
        cSnake.bStartSnake()
        #bGameIsOn = False
        
#Close the screen -- last instruction of the program
theScreen.exitonclick()
