file_read = open("Codingal.txt","r")
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open("Codingal.txt","w")
print("File in write mode - ")
file_write.write("Hi I am penguin I am 1 year old ")
file_write.close()

file_append = open("Codingal.txt","a")
print("File in append mode - ")
file_append.write("Hi I am penguin I am 1 year old")
file_append.close()