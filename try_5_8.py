user_name = ['akshay',
            'admin',
            'rahul',
            'kamal',
            'suresh',
            ]
user_name.clear()    
if len(user_name) == 0:
  print("We need to find some users")
for name in user_name:
  if name == 'admin':
    print("Hello admin, would you like to see a status report")
  else:
    print("Hello " + name + ", thank you for logging in aganin")

list = [1,2,3,4,5,6,7,8,9,]
for i in list:
  if i == 1:
    print(str(i) + "st")
  elif i == 2:
    print(str(i) + "nd")
  elif i == 3:
    print(str(i) + "rd")
  else:
    print(str(i) + "th")
