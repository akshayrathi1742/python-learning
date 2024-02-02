1

age = int(input("Enter your age: "))
if  age <= 0:
  price = 0
  print("invalid age")
elif age <=18 or age <= 60:
  price = 30  
elif age > 60:
   price = 10
else:
   price = 0
print("Your price is: ", price)

#5-5
a_colour = "green"
if a_colour == 'green':
  print("5 point earned")
else:
  print("10 point earned")
#5-6

age  = int(input("Enter your age: "))
statement = (" your age is " + str(age) + " years old")
if age < 2:
  print(statement + " and you are a baby")
elif age >= 2 and age < 4:
  print("you are toddler" + " and your age is " + str(age))
elif age >= 4 and age < 13:
  print("you are a kid" + " and your age is " + str(age))
elif age >= 13 and age < 20:
  print("you are a teenager" + " and your age is " + str(age))
elif age  >= 20 and age < 65:
  print("you are an adult " + " and your agr is " + str(age))
elif age > 65 and age < 120:
  print("you are an elder" + " and your age is " + str(age))
else:
  print("error")

using if staements with lists
available_vegitable = ['broccoli','spinach', 'carrot','potato',
 'onion',
  'pepper',
 'tomato',
           ]
ordered_vegitable = ['broccoli', 'saag', #'tomato']
for vegitable in ordered_vegitable:
if vegitable in available_vegitable:
  print(vegitable)
else:
   print("sorry, we don't have " + #vegitable)