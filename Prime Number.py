num =int(input("Enter a number"))
flag = False
if(num>1):
# check for factors
 for i in range(2,num):
  if(num%i==0):
   flag = True
   break
if (flag):
 print("It is not a prime Number")
else:
 print("It is a prime number")    