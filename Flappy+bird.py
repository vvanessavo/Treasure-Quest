  #**********************************************************
# Program : Flappy bird
# Author : Vanessa Vo
# Due Date : 11/05/18
# Description : Flappy bird game
#**********************************************************

import turtle 
import sys
import random
tom = turtle.Turtle()

tom.color("Mistyrose")
tom.shape("turtle")

turtle.setup(600,600)
screen = turtle.Screen()

screen.bgcolor("black")
screen.bgpic("star.gif")

image = ("kirbystar.gif")
screen.addshape(image)
tom.shape(image)

tom.left(90)
tom.penup()

image2 =("metaknight.gif")
blob= turtle.Turtle()
screen.addshape(image2)
blob.shape(image2)
blob.penup()
blob.right(180)
blob.color("Mistyrose")
def newBlob():
    y = random.randint(-255,255)
    blob.setposition(300,y)

def move_the_blob():
    if (blob.xcor() == -5):
        newBlob()
    blob.forward(5)
    if (abs(tom.ycor() - blob.ycor()) <10 and blob.xcor()>-5):
        tom.write("U PROTECC")
    screen.ontimer(move_the_blob,5)
    if (abs(tom.ycor() - blob.ycor()) >100 and blob.xcor() ==-5) :
        blob.write("HE ATTACK:((")

def fall():
    if tom.ycor() - 1 > -280:
        tom.backward(1)
    screen.ontimer(fall,1)

def space_bar():
    if tom.ycor() + 20<290:
        tom.forward(40)
        
fall()
newBlob()

screen.onkey(space_bar, "space")

move_the_blob()
screen.listen()

screen.mainloop()


