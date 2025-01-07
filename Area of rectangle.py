class Rectangle:
 def __init__(self,l,w):
  self.length = l
  self.width = w
   
 def areaof_rec(self): 
  return self.length*self.width

newrectangle = Rectangle(10,12)
print("Dimesions of rectangle: length:",newrectangle.length, "width :",newrectangle.width  )
print("Area of rectangle: ",newrectangle.areaof_rec())  
  