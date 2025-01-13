import sys
def initial_phonebook():
  rows,columns = int(input("Enter the number of contacts you want")),5
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
    phonebook.append(temp)
def menu():  
  print("***************************************************************************")
  print("\t\t\tSMARTPHONE DICTIONARY",flush=False)
  print("***************************************************************************")
  print("\tYou can now perform the following operations gven on this phone book\n")
  print("1. Add a new contact")
  print("2. Remove an existing contact")
  print("3. Delete all contacts")
  print("4. Search for a contact")
  print("5. Display all contacts")
  print("6. Exit phonebook")

  choice = int(input("Please enter your choice"))
  return choice

def add_contact(pb):
 dip = []
 for i in range(len(pb[0])):
   if (i==0):
    dip.append(str(input("Enter name :"))) 
   if (i==1):
    dip.append(int(input("Enter number :")))
   if (i==2):
    dip.append(str(input("Enter e-mail address :")))
   if (i==3):
    dip.append(str(input("Enter date of Birth(dd/mm/yy) :")))
   if (i==4):
    dip.append(str(input("Enter category(Family/friends/work/others)")))
 
 pb.append(dip)
 return

def remove_existing(pb):
  query = str(input("Please enter the name of the contack you wish to delete :"))
  temp = 0
  for i in range(len(pb)):
    if query==[i][0]: 
      temp += 1
      print(pb.pop(i))
      print("This query has now been removed")
      return pb
  if temp == 0:
   print("Sorry you have entered a invaild query.\nPlease recheck an laterd try again")
   return pb
def delete_all(pb):
  return pb.clear       