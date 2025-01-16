file = open("Codingal.txt","r")
content = file.read()
counter = 0
Colist = content.split("\n")
for i in Colist:
   counter += 1
print("This is the number of lines in the file")
print(counter)   