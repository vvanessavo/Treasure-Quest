#**********************************************************
# Program : Assignment #3
# Author : Vanessa Vo
# Due Date : 11/08/18
# Description :Rainbow Peacock!!
#**********************************************************\

import turtle
import sys
tom = turtle.Turtle()

tom.shape("turtle")
turtle.setup(600,600)
screen = turtle.Screen()
turtle.colormode(255)
turtle.bgcolor(12,0,80)
##screen.bgpic("animals-3.gif")
tom.speed(0)


##grid
tom.speed(0)
tom.pencolor("white")
tom.penup()
tom.goto(0,-300)
tom.pendown()
tom.goto(0,300)
tom.penup()
tom.goto(-300,0)
tom.pendown()
tom.goto(300,0)
tom.speed(5)

tom.penup()

tom.goto(-32,-83.5)

#fan left side
tom.pendown()
tom.pencolor(117,244,168)
tom.begin_fill()
tom.fillcolor(117,244,168)

tom.left(195)
tom.forward(105)
tom.right(50)
tom.forward(60)
tom.left(35)
tom.forward(40)
tom.right(50)

for i in range(3):
    tom.forward(90)
    tom.right(103)
    tom.forward(90)
    tom.left(80)
tom.forward(90)

###fan right side
tom.right(120)

for i in range (3):
    tom.forward(90)
    tom.left(80)
    tom.forward(90)
    tom.right(106)


tom.left(8)
tom.forward(90)
tom.right(50)
tom.forward(40)
tom.left(35)
tom.forward(60)
tom.right(52)
tom.forward(105)

tom.left(15)
tom.forward(60)

tom.forward(84)
tom.end_fill()

tom.speed(10)
#big designs

tom.goto(-217,-65)
tom.pendown()
tom.pencolor(250,250,131)
tom.begin_fill()
tom.fillcolor(250,250,131)

##Left big design1

tom.goto(-175,-65)
tom.goto(-165,5)
tom.goto(-197,23)
tom.goto(-265,-10)
tom.goto(-217,-65)
tom.end_fill()

##Left design 2
tom.penup()
tom.goto(-155,25)
tom.pendown()
tom.begin_fill()
tom.goto(-190,43)
tom.goto(-213,113)
tom.goto(-135,117)
tom.goto(-115,90)
tom.goto(-155,25)
tom.end_fill()

##Left design3
tom.penup()
tom.goto(-100,100)
tom.pendown()
tom.begin_fill()
tom.goto(-123,128)
tom.goto(-115,200)
tom.goto(-50,175)
tom.goto(-37,145)
tom.goto(-100,100)
tom.end_fill()

##Middle design
tom.penup()
tom.goto(-25,150)
tom.pendown()
tom.begin_fill()
tom.goto(-35,180)
tom.goto(0,245)
tom.goto(40,180)
tom.goto(25,150)
tom.goto(-25,150)
tom.end_fill()

##Right big design1
tom.penup()
tom.goto(217,-65)
tom.pendown()
tom.begin_fill()
tom.goto(175,-65)
tom.goto(165,5)
tom.goto(197,23)
tom.goto(265,-10)
tom.goto(217,-65)
tom.end_fill()

##Right big design2
tom.penup()
tom.goto(155,25)
tom.pendown()
tom.begin_fill()
tom.goto(190,43)
tom.goto(213,113)
tom.goto(135,117)
tom.goto(115,90)
tom.goto(155,25)
tom.end_fill()

##Right big design3

tom.penup()
tom.goto(100,100)
tom.pendown()
tom.begin_fill()
tom.goto(123,128)
tom.goto(115,200)
tom.goto(50,175)
tom.goto(40,145)
tom.goto(100,100)
tom.end_fill()


#Left inside orange 1

tom.penup()
tom.goto(-197,-65)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)

tom.goto(-155,-65)
tom.goto(-145,5)
tom.goto(-177,23)
tom.goto(-245,-10)
tom.goto(-197,-65)
tom.end_fill()

#Left inside red 1

tom.penup()
tom.goto(-197,-65)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)

tom.goto(-135,-65)
tom.goto(-125,5)
tom.goto(-157,23)
tom.goto(-225,-10)
tom.goto(-177,-65)
tom.end_fill()

#Left inside pink 1 
tom.penup()
tom.goto(-177,-65)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)

tom.goto(-115,-65)
tom.goto(-105,5)
tom.goto(-137,23)
tom.goto(-205,-10)
tom.goto(-157,-65)
tom.end_fill()

#Left inside pink-purple1
tom.penup()
tom.goto(-157,-65)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(248,131,236)

tom.goto(-95,-65)
tom.goto(-85,5)
tom.goto(-117,23)
tom.goto(-185,-10)
tom.goto(-137,-65)
tom.end_fill()

#Left inside purple1
tom.penup()
tom.goto(-137,-65)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)

tom.goto(-75,-65)
tom.goto(-65,5)
tom.goto(-97,23)
tom.goto(-165,-10)
tom.goto(-117,-65)
tom.end_fill()

#Left inside darker purple1
tom.penup()
tom.goto(-127,-65)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)

tom.goto(-55,-65)
tom.goto(-45,5)
tom.goto(-77,23)
tom.goto(-145,-10)
tom.goto(-97,-65)
tom.end_fill()

#Left inside darkerdarker purple1
tom.penup()
tom.goto(-107,-65)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)

tom.goto(-35,-65)
tom.goto(-25,5)
tom.goto(-57,23)
tom.goto(-125,-10)
tom.goto(-77,-65)
tom.end_fill()

#Left inside blue 1
tom.penup()
tom.goto(-87,-65)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)

tom.goto(-15,-65)
tom.goto(-5,5)
tom.goto(-37,23)
tom.goto(-105,-10)
tom.goto(-57,-65)
tom.end_fill()

#Left inside orange 2
tom.penup()
tom.goto(-140,15)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)
tom.goto(-175,33)
tom.goto(-198,103)
tom.goto(-120,107)
tom.goto(-90,80)
tom.goto(-140,15)
tom.end_fill()

#Left inside red 2 
tom.penup()
tom.goto(-140,5)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)
tom.goto(-160,23)
tom.goto(-183,93)
tom.goto(-105,97)
tom.goto(-75,70)
tom.goto(-125,5)
tom.end_fill()

#Left inside pink 2 
tom.penup()
tom.goto(-125,-5)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)
tom.goto(-145,13)
tom.goto(-168,83)
tom.goto(-90,87)
tom.goto(-60,60)
tom.goto(-110,-5)
tom.end_fill()

#Left inside pink-purple 2 
tom.penup()
tom.goto(-110,-15)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(249,131,236)
tom.goto(-130,3)
tom.goto(-153,73)
tom.goto(-75,77)
tom.goto(-45,50)
tom.goto(-95,-15)
tom.end_fill()

#Left inside purple 2 
tom.penup()
tom.goto(-95,-25)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)
tom.goto(-115,-3)
tom.goto(-138,63)
tom.goto(-60,67)
tom.goto(-30,40)
tom.goto(-80,-25)
tom.end_fill()

#Left inside darker purple 2 
tom.penup()
tom.goto(-80,-35)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)
tom.goto(-100,-13)
tom.goto(-123,53)
tom.goto(-45,57)
tom.goto(-15,30)
tom.goto(-65,-35)
tom.end_fill()

#Left inside darker darker purple 2 
tom.penup()
tom.goto(-65,-45)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)
tom.goto(-85,-23)
tom.goto(-108,43)
tom.goto(-30,47)
tom.goto(0,20)
tom.goto(-50,-45)
tom.end_fill()

#Left inside blue 2
tom.penup()
tom.goto(-50,-55)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)
tom.goto(-70,-33)
tom.goto(-93,33)
tom.goto(-15,37)
tom.goto(15,10)
tom.goto(-35,-35)
tom.end_fill()

#Left inside orange 3 
tom.penup()
tom.goto(-90,85)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)
tom.goto(-113,113)
tom.goto(-105,185)
tom.goto(-40,160)
tom.goto(-27,130)
tom.goto(-90,85)
tom.end_fill()

#Left inside red 3 
tom.penup()
tom.goto(-80,70)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)
tom.goto(-103,98)
tom.goto(-95,170)
tom.goto(-30,145)
tom.goto(-17,115)
tom.goto(-80,70)
tom.end_fill()

#Left inside pink 3 
tom.penup()
tom.goto(-70,55)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)
tom.goto(-93,83)
tom.goto(-85,155)
tom.goto(-20,130)
tom.goto(-7,100)
tom.goto(-70,55)
tom.end_fill()

#Left inside pink purple 3 
tom.penup()
tom.goto(-60,40)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(249,131,236)
tom.goto(-83,68)
tom.goto(-75,140)
tom.goto(-10,115)
tom.goto(3,85)
tom.goto(-60,40)
tom.end_fill()

#Left inside purple 3 
tom.penup()
tom.goto(-60,25)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)
tom.goto(-73,53)
tom.goto(-65,125)
tom.goto(0,100)
tom.goto(13,70)
tom.goto(-50,25)
tom.end_fill()

#Left inside darker purple 3 
tom.penup()
tom.goto(-50,10)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)
tom.goto(-63,38)
tom.goto(-55,110)
tom.goto(10,90)
tom.goto(23,60)
tom.goto(-40,10)
tom.end_fill()

#Left inside darker darker purple 3 
tom.penup()
tom.goto(-40,-5)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)
tom.goto(-53,23)
tom.goto(-45,95)
tom.goto(20,75)
tom.goto(33,45)
tom.goto(-40,-5)
tom.end_fill()

#Left inside blue 3 
tom.penup()
tom.goto(-30,-20)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)
tom.goto(-43,8)
tom.goto(-35,80)
tom.goto(30,60)
tom.goto(43,30)
tom.goto(-30,-20)
tom.end_fill()

#Right inside orange 1

tom.penup()
tom.goto(197,-65)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)

tom.goto(155,-65)
tom.goto(145,5)
tom.goto(177,23)
tom.goto(245,-10)
tom.goto(197,-65)
tom.end_fill()

#Right inside red 1

tom.penup()
tom.goto(197,-65)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)

tom.goto(135,-65)
tom.goto(125,5)
tom.goto(157,23)
tom.goto(225,-10)
tom.goto(177,-65)
tom.end_fill()

#Right inside pink 1 
tom.penup()
tom.goto(177,-65)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)

tom.goto(115,-65)
tom.goto(105,5)
tom.goto(137,23)
tom.goto(205,-10)
tom.goto(157,-65)
tom.end_fill()

#Right inside pink-purple1
tom.penup()
tom.goto(157,-65)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(248,131,236)

tom.goto(95,-65)
tom.goto(85,5)
tom.goto(117,23)
tom.goto(185,-10)
tom.goto(137,-65)
tom.end_fill()

#Right inside purple1
tom.penup()
tom.goto(137,-65)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)

tom.goto(75,-65)
tom.goto(65,5)
tom.goto(97,23)
tom.goto(165,-10)
tom.goto(117,-65)
tom.end_fill()

#Right inside darker purple1
tom.penup()
tom.goto(127,-65)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)

tom.goto(55,-65)
tom.goto(45,5)
tom.goto(77,23)
tom.goto(145,-10)
tom.goto(97,-65)
tom.end_fill()

#Right inside darkerdarker purple1
tom.penup()
tom.goto(107,-65)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)

tom.goto(35,-65)
tom.goto(25,5)
tom.goto(57,23)
tom.goto(125,-10)
tom.goto(77,-65)
tom.end_fill()

#Right inside blue 1
tom.penup()
tom.goto(87,-65)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)

tom.goto(15,-65)
tom.goto(5,5)
tom.goto(37,23)
tom.goto(105,-10)
tom.goto(57,-65)
tom.end_fill()

#Right inside orange 2
tom.penup()
tom.goto(140,15)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)
tom.goto(175,33)
tom.goto(198,103)
tom.goto(120,107)
tom.goto(90,80)
tom.goto(140,15)
tom.end_fill()

#Right inside red 2 
tom.penup()
tom.goto(140,5)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)
tom.goto(160,23)
tom.goto(183,93)
tom.goto(105,97)
tom.goto(75,70)
tom.goto(125,5)
tom.end_fill()

#Right inside pink 2 
tom.penup()
tom.goto(125,-5)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)
tom.goto(145,13)
tom.goto(168,83)
tom.goto(90,87)
tom.goto(60,60)
tom.goto(110,-5)
tom.end_fill()

#Right inside pink-purple 2 
tom.penup()
tom.goto(110,-15)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(249,131,236)
tom.goto(130,3)
tom.goto(153,73)
tom.goto(75,77)
tom.goto(45,50)
tom.goto(95,-15)
tom.end_fill()

#Right inside purple 2 
tom.penup()
tom.goto(95,-25)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)
tom.goto(115,-3)
tom.goto(138,63)
tom.goto(60,67)
tom.goto(30,40)
tom.goto(80,-25)
tom.end_fill()

#Right inside darker purple 2 
tom.penup()
tom.goto(80,-35)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)
tom.goto(100,-13)
tom.goto(123,53)
tom.goto(45,57)
tom.goto(15,30)
tom.goto(65,-35)
tom.end_fill()

#Right inside darker darker purple 2 
tom.penup()
tom.goto(65,-45)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)
tom.goto(85,-23)
tom.goto(108,43)
tom.goto(30,47)
tom.goto(0,20)
tom.goto(50,-45)
tom.end_fill()

#Right inside blue 2
tom.penup()
tom.goto(50,-55)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)
tom.goto(70,-33)
tom.goto(93,33)
tom.goto(15,37)
tom.goto(-15,10)
tom.goto(35,-35)
tom.end_fill()

#Right inside orange 3 
tom.penup()
tom.goto(90,85)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)
tom.goto(113,113)
tom.goto(105,185)
tom.goto(40,160)
tom.goto(27,130)
tom.goto(90,85)
tom.end_fill()

#Right inside red 3 
tom.penup()
tom.goto(80,70)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)
tom.goto(103,98)
tom.goto(95,170)
tom.goto(30,145)
tom.goto(17,115)
tom.goto(80,70)
tom.end_fill()

#Right inside pink 3 
tom.penup()
tom.goto(70,55)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)
tom.goto(93,83)
tom.goto(85,155)
tom.goto(20,130)
tom.goto(7,100)
tom.goto(70,55)
tom.end_fill()

#Right inside pink purple 3 
tom.penup()
tom.goto(60,40)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(249,131,236)
tom.goto(83,68)
tom.goto(75,140)
tom.goto(10,115)
tom.goto(-3,85)
tom.goto(60,40)
tom.end_fill()

#Right inside purple 3 
tom.penup()
tom.goto(60,25)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)
tom.goto(73,53)
tom.goto(65,125)
tom.goto(0,100)
tom.goto(-13,70)
tom.goto(50,25)
tom.end_fill()

#Right inside darker purple 3 
tom.penup()
tom.goto(50,10)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)
tom.goto(63,38)
tom.goto(55,110)
tom.goto(-10,90)
tom.goto(-23,60)
tom.goto(40,10)
tom.end_fill()

#Right inside darker darker purple 3 
tom.penup()
tom.goto(40,-5)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)
tom.goto(53,23)
tom.goto(45,95)
tom.goto(-20,75)
tom.goto(-33,45)
tom.goto(40,-5)
tom.end_fill()

#Right inside blue 3 
tom.penup()
tom.goto(30,-20)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)
tom.goto(43,8)
tom.goto(35,80)
tom.goto(-30,60)
tom.goto(-43,30)
tom.goto(30,-20)
tom.end_fill()

#Middle orange 
tom.penup()
tom.goto(-25,130)
tom.pendown()
tom.pencolor(255,187,85)
tom.begin_fill()
tom.fillcolor(255,187,85)
tom.goto(-35,160)
tom.goto(0,225)
tom.goto(40,160)
tom.goto(25,130)
tom.goto(-25,130)
tom.end_fill()

#Middle red 
tom.penup()
tom.goto(-25,110)
tom.pendown()
tom.pencolor(255,132,96)
tom.begin_fill()
tom.fillcolor(255,132,96)
tom.goto(-35,140)
tom.goto(0,205)
tom.goto(40,140)
tom.goto(25,110)
tom.goto(-25,110)
tom.end_fill()

#Middle pink 
tom.penup()
tom.goto(-25,90)
tom.pendown()
tom.pencolor(255,96,136)
tom.begin_fill()
tom.fillcolor(255,96,136)
tom.goto(-35,120)
tom.goto(0,185)
tom.goto(40,120)
tom.goto(25,90)
tom.goto(-25,90)
tom.end_fill()

#Middle pink purple 
tom.penup()
tom.goto(-25,70)
tom.pendown()
tom.pencolor(249,131,236)
tom.begin_fill()
tom.fillcolor(249,131,236)
tom.goto(-35,100)
tom.goto(0,165)
tom.goto(40,100)
tom.goto(25,70)
tom.goto(-25,70)
tom.end_fill()

#Middle purple 
tom.penup()
tom.goto(-25,50)
tom.pendown()
tom.pencolor(219,96,255)
tom.begin_fill()
tom.fillcolor(219,96,255)
tom.goto(-35,80)
tom.goto(0,145)
tom.goto(40,80)
tom.goto(25,50)
tom.goto(-25,50)
tom.end_fill()

#Middle darker purple 
tom.penup()
tom.goto(-25,30)
tom.pendown()
tom.pencolor(139,70,255)
tom.begin_fill()
tom.fillcolor(139,70,255)
tom.goto(-35,60)
tom.goto(0,125)
tom.goto(40,60)
tom.goto(25,30)
tom.goto(-25,30)
tom.end_fill()

#Middle darker darker purple 
tom.penup()
tom.goto(-25,10)
tom.pendown()
tom.pencolor(102,70,255)
tom.begin_fill()
tom.fillcolor(102,70,255)
tom.goto(-35,40)
tom.goto(0,105)
tom.goto(40,40)
tom.goto(25,10)
tom.goto(-25,10)
tom.end_fill()

#Middle blue 
tom.penup()
tom.goto(-25,-20)
tom.pendown()
tom.pencolor(34,84,255)
tom.begin_fill()
tom.fillcolor(34,84,255)
tom.goto(-35,20)
tom.goto(0,85)
tom.goto(40,20)
tom.goto(25,-20)
tom.goto(-25,-20)
tom.end_fill()


##### bodyright side\
tom.penup()
tom.goto(0,-100)
tom.pendown()
tom.pencolor(94,219,255)
tom.begin_fill()
tom.fillcolor(94,219,255)
tom.goto(0,-100)
tom.penup()

tom.right(180)
tom.forward(20)
tom.left(55)
tom.forward(20)
tom.left(50)
tom.forward(105)
   
tom.right(45)
tom.forward(15)
tom.left(45)
tom.forward(15)
tom.left(75)
tom.forward(10)

#left side
tom.forward(10)
tom.left(75)
tom.forward(15)
tom.left(45)
tom.forward(15)
tom.right(45)

tom.forward(105)
tom.left(50)
tom.forward(20)
tom.left(55)
tom.forward(20)
tom.end_fill()
tom.penup()

#left eye 
tom.goto(-7,33)
tom.pendown()
tom.pencolor("black")
tom.begin_fill()
tom.fillcolor("black")
tom.circle(3.5)
tom.end_fill()
tom.penup()
tom.goto(-6.8,38)
tom.pendown()
tom.pencolor("white")
tom.begin_fill()
tom.fillcolor("white")
tom.circle(.5)
tom.end_fill()
tom.penup()
tom.goto(0,0)

#Right eye

tom.goto(7,33)
tom.pendown()
tom.pencolor("black")
tom.begin_fill()
tom.fillcolor("black")
tom.circle(3.5)
tom.end_fill()
tom.penup()
tom.goto(6.8,38)
tom.pendown()
tom.pencolor("white")
tom.begin_fill()
tom.fillcolor("white")
tom.circle(.5)
tom.end_fill()
tom.penup()
tom.goto(5,30)

#beak
tom.pendown()
tom.begin_fill()
tom.goto(0,20)
tom.goto(-4,30)
tom.goto(4,30)
tom.end_fill()
tom.penup()

#blush
tom.goto(8,30)
tom.pendown()
tom.pencolor("lightpink")
tom.pensize(3)
tom.goto(14,30)
tom.penup()
tom.goto(-8,30)
tom.pendown()
tom.goto(-14,30)

#left Leg
tom.pensize(5)
tom.penup()
tom.goto(-33,-88)
tom.pencolor(250,250,131)
tom.begin_fill()
tom.fillcolor(250,250,131)
tom.pendown()
tom.goto(-25,-100)
tom.goto(-25,-125)
tom.goto(-33,-88)
tom.end_fill()

#left foot
tom.penup()
tom.goto(-25,-125)
tom.pendown()
tom.begin_fill()
tom.goto(-45,-125)
tom.goto(-32.5,-135)
tom.goto(-25,-125)
tom.end_fill()

#Right leg
tom.penup()
tom.goto(33,-88)
tom.pencolor(250,250,131)
tom.begin_fill()
tom.fillcolor(250,250,131)
tom.pendown()
tom.goto(25,-100)
tom.goto(25,-125)
tom.goto(33,-88)
tom.end_fill()

#Right foot
tom.penup()
tom.goto(25,-125)
tom.pendown()
tom.begin_fill()
tom.goto(45,-125)
tom.goto(32.5,-135)
tom.goto(25,-125)
tom.end_fill()

#Dot
tom.penup()
tom.goto(0,55)
tom.pencolor(94,219,255)
tom.begin_fill()
tom.fillcolor(94,219,255)
tom.pendown()
tom.circle(4.5)
tom.end_fill()
tom.penup()
tom.goto(-400,-400)
















 

    




    
    
    
    
    
    
