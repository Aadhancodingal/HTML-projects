with open("Codingal.txt","w") as file:
 file.write("Hi I am penguin I am 1 yr old")
file.close

with open("Codingal.txt","r") as file:
 data = file.readlines()
 print("Words in the files are ......")
 for line in data:
  word = line.split()
  print(word)
 file.close() 