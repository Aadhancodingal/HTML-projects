class Parrot:
 def __init__(self,name,age):
  self.name = name
  self.age = age

 def sing(self,song):
   print("{} is singing {}".format(self,song))

 def dance(self):
   print("{} is dancing")

 print(sing("Blu","Open it up"))
 print(dance("Woo"))