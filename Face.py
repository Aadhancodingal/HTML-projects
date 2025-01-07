from turtle import *
class Face:
 def __init__(self,xpos,ypos):
  self.size = 90
  self.coord = (xpos,ypos)
  self.nose_size ='small'

 def setsize(self,radius):
  self.size = radius

 def draw(self):
  self.gohome()
  pensize(3)
  speed(0)
  self.drawOutiline()
  self.drawEye(135)
  self.drawEye(45)
  self.drawNose()
  self.drawMouth()
  pensize(5)

 def gohome(self):
  penup()
  goto(self.coord)

  setheading(0)
 def drawOutiline(self):
  penup()
  forward(self.size)
  left(90)
  pendown()
  circle(self.size)
  self.gohome()

 def drawEye(self,turn):
  penup()
  left(turn)
  forward(self.size/2)
  pendown()
  dot(self.size)
  self.gohome()

 def drawMouth(self):
  penup()
  right(135)
  forward(self.size/1.7)
  left(90)
  pendown()
  circle(self.size/1.7,90)
  self.gohome()

 def drawNose(self):
  if (self.nose_size == 'large'):
   dot(self.size/2,'grey')
  elif(self.nose_size == 'small'):
   dot(self.size/6,'grey')
  else:
   dot(self.size/4,'grey')

f1 = Face(0,0)
f1.draw()

showturtle()
done()
   