my_dict = {}
my_dict = {1:'Ball',2:'apple'}
my_dict = {"Name":"Jack" ,1:[2,4,3]}
my_dict = {"Name":"Jack","Age":"26"}
print(my_dict["Name"])
print(my_dict.get('age'))
my_dict['Age'] = 27 
print(my_dict)
my_dict['address']= "Namakal" 
print(my_dict)
my_dict.pop('Age')
print(my_dict)
print("Address :",my_dict.get('address'))
my_dict.clear()
print(my_dict)