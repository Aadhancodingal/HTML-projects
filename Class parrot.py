class Parrot:
 
 # class attribute
 species = "bird"
# instant attribute

 def __init__(self,name,age):
  self.name = name
  self.age = age
# instiate the parrot class
blu = Parrot("Blu",10)
woo = Parrot("Woo",5)

print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))