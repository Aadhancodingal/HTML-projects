import sys
def initial_phonebook():
  rows,columns = int(input("Enter the number of contacts you want"))
  phonebook = []
  print(phonebook)
  for i in range(rows):
   print("\nEnter the Contact %d detials in order(ONLY):" % (i+1))
   print("NOTE: * indicates mandatory fields")
  print("......................................................")
  temp = []
  for j in range(columns):
    if (j == 0):
     temp.append(str(input("Enter name*:")))
     if (temp[j]== '' or temp[j]== ' '):
      sys.exit("Name is a mandatory field,Process exiting due to blank field...")
    if (j==1):
     temp.append(int(input("Enter number*:")))
    if (j==2):
     temp.append(str(input("Enter e-mail address:")))  
     if(temp[j]==''or temp[j==' ']):
      temp[j=='None']
    if (j==3):
     temp.append(str(input("Enter date of birth(dd/mm/yy):")))
     if(temp[j]==''or temp[j==' ']):
      temp[j=='None']
    if (j==4):
     temp.append(str(input("Enter address:")))
     if(temp[j]==''or temp[j==' ']):
      temp[j=='None']    