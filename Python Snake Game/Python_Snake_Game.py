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
theScreen.setup(width=cParam.iScreenWidth, height=cParam.iScreenHeight)

#Clear the screen after each movement
def fCleanScreen(theScreen):
    theScreen.clearscreen()
    theScreen.bgcolor(cParam.sBackColor)
    theScreen.title(f"{cParam.sTitle}")
      
def bDetectCollition():
    #validate if Snake Head  position is same of food point
    if cSnake.theSnakes[0].distance(cFood) < cParam.iSnakeSize-5:
        cFood.fFoodRefresh()
        return True
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
cScore.bPrintScore(cParam.getScore())

#Screen and Key events assigment 
theScreen.onkey(key="Up",fun=cSnake.turnUp)   #This is a sample of a higher order function
theScreen.onkey(key="Down",fun=cSnake.turnDown)   #This is a sample of a higher order function
theScreen.onkey(key="Left",fun=cSnake.moveLeft)   #This is a sample of a higher order function
theScreen.onkey(key="Right",fun=cSnake.moveRight)   #This is a sample of a higher order function
theScreen.listen()

#Snake walk through screen
while bGameIsOn:
    theScreen.update()
    time.sleep(0.1)
    cSnake.fTracer()
    #Detect Collition
    if bDetectCollition():
        #Increment Score
        cParam.bUpdateScore(1)
        cScore.bPrintScore(cParam.getScore())
        cFood.fFoodRefresh()
        
        
#Close the screen -- last instruction of the program
theScreen.exitonclick()
