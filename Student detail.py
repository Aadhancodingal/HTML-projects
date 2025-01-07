class CssStudent:
  stream = "css"

  def __init__(self,roll):
    self.roll = roll

  def setAddress(self,address):
    self.address = address

  def getAdress(self):
    return self.address

add = CssStudent(101)
add.setAddress("Rasipuram,Tamilnadu")
print(add.getAdress)

a = CssStudent(101)
b = CssStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)

print(CssStudent.stream)