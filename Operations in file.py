file = open("Codingal.txt","r")
print(file.read())
file.close()

file = open("Codingal.txt","r")
print("Read in parts -")
print(file.read(8))
file.close()

file = open("Codingal.txt","a")
file.write("\nHi, I am penguin, I am 1 year old.")