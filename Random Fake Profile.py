import random
fname = ['John', 'Jane', 'Lionel', 'Cristiano', 'Lamine', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria','Adam','Sturt','Nikolson','Tom','Harry','Ruskin','Thor','Rocky','Ravid','David','Harris','Eion','Elon','Mark','Will','Chris']
lname = ['Smith', 'Doe', 'Ronaldo', 'Messi', 'Yamal', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin','Potter','Jukerberg','Smith','Nebula','Downy','Downy Jr']
street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']
fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

class Name:
    def __init__(self,num=1):
        '''
        num = Total No. of Name You Want To Print
        deafult is 1
        To Print More Than one Name Change value of num
        ''' 
        self.num = num

    def first_name(self):
        #print first name
        for i in range(self.num):
          first = random.choice(fname)
          print(first)

    def last_name(self):
        #print last name
        for i in range(self.num):
          last = random.choice(lname)
          print(last)
   
    def full_name(self):
        #print full name
        for i in range(self.num):
          first = random.choice(fname)
          last = random.choice(lname)
          print(f'{first} {last}')

    def full_profile(self):
        #print full profile
        
        for i in range(self.num):
          first = random.choice(fname)
          last = random.choice(lname)
          phone = f'+91-{random.randint(800, 999)}{random.randint(800, 999)}{random.randint(1000,9999)}'

          street_num = random.randint(100, 999)
          street = random.choice(street_names)
          city = random.choice(fake_cities)
          state = random.choice(states)
          zip_code = random.randint(10000, 99999)
          
          address = f'{street_num} {street} St., {city} {state} {zip_code}'
          email = first.lower() + last.lower() + '@bogusemail.com'
          print(f'{first} {last} \n {address}- Us\n{phone}\n{email}')
          print('-'*30)
        print('*'*30)
  
num = int(input("Number of Profiles you want to create :"))
ob = Name(num)
print("\nRandom First Names :")
ob.first_name()
print("\nRandom Last Names :")
ob.last_name()
print("\nRandom Full Names :")
ob.full_name()
print("\nRandom Profiles :")
ob.full_profile()