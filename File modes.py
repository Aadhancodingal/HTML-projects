file_read = open("Codingal.txt","r")
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open("Codingal.txt","w")
print("File in write mode -")
file_write.write("Hi I am Aadhan, I am 10 years old")
file_write.close()

file_append = open("Codingal.txt","a")
print("\n File in append mode-")
file_append.write("Hi I am Aadhan, I am 10 years old")
file_append.close()