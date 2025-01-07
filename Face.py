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
    