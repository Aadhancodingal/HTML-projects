my_tupl = ()
print(my_tupl)
my_tupl = (1,4,35,63)
print(my_tupl)
my_tupl = (1,"HAIR",True,35)
print(my_tupl)
my_tupl = ("mouse", [8,4,6],(1,2,3))
print(my_tupl)
my_tupl = ("p","e","r","m","i","t")
print(my_tupl[0])
print(my_tupl[5])
n_tupl = ("mouse", [8,4,6],(1,2,3))
print(n_tupl[0][3])
print(n_tupl[1][1])
print("Sliced:",my_tupl[1:4])
for letter in(my_tupl):
 print("Hello",letter)