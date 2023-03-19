from queue import Empty
from sre_constants import RANGE
import time
from SnakeClass import Snake
from turtle import Screen

#Game Status Control
bGameIsOn = False

#Program Variables or Constants
iScreenWidth = 600   #Future improvement, ask user for screen size??
iScreenHeight = 600
sBackColor = "Black"
sTitle = "my Snake Game - Python"
iScore = 0  #Player Score

#Create the screen
theScreen = Screen()
theScreen.setup(width=iScreenWidth, height=iScreenHeight)

#Clear the screen after each movement
def fCleanScreen(theScreen):
    theScreen.clearscreen()
    theScreen.bgcolor(sBackColor)
    if bGameIsOn == True:
        theScreen.title(f"{sTitle} - Score: {str(iScore)} - Sneak Heading to {cSnake.iSnakeHeading}")
    else:
        theScreen.title(f"{sTitle} - Score: {str(iScore)} ")
        
#Game Status Control
fCleanScreen(theScreen)
print ("\nGame Start")
bGameIsOn = True
#create snake object
cSnake = Snake()

#Screen and Key events assigment 
theScreen.onkey(key="Up",fun=cSnake.turnUp)   #This is a sample of a higher order function
theScreen.onkey(key="Down",fun=cSnake.turnDown)   #This is a sample of a higher order function
theScreen.onkey(key="Left",fun=cSnake.moveLeft)   #This is a sample of a higher order function
theScreen.onkey(key="Right",fun=cSnake.moveRight)   #This is a sample of a higher order function

#Snake walk through screen
while bGameIsOn:
    theScreen.update()
    time.sleep(0.1)
    theScreen.listen()
    cSnake.fTracer()

#Close the screen -- last instruction of the program
theScreen.exitonclick()
