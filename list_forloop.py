#magicians = [
    #         'aric',
   #          'gandalv',
  #           'sauron'
 #          ]
#for magician in magicians :
  # print(magician.title() + ", that was a graet trick")
#print("Thankyou everyone.that was a great show")  

pizza = [
  'cheese',
  'loadedvegies',
 'masrum'
]
#for i in pizza :
 # print(i + " " +  "I LIKE PEPPERONI PIZZA ")
#print(" I really love pizza")  

my_food = [
           'pizza',#0
           'bread',#1
           'burger',#2
           'pasta',#3
           'icecream'#4
]
#print("The first three item in the list are :")
#print(my_food[0:3])

#print("Three items of middel in the list are :")
#print(my_food[1:4])

#print("The last item in the list are :")
#print(my_food[2:5])

my_pizza = [
  'loadedvegies',
  'cheese',
  'masrum'
]
your_pizza = my_pizza[:]
my_pizza.append('peproni')
your_pizza.append('onion')
print("my favourite pizza are:\n")
for i in my_pizza :
  print(i)
print("your favourite pizza are:\n")
for i in your_pizza :
  print(i)

print("\nmy friends favourite pizza are :\n")
for i in your_pizza :
  print(i)


# 2 list itration with zip function

l1 = [20,30,40,50,60,70]# giving no error when list lenth is not equal in two seprate two list 
l2 = [1,2,3,4,5,]
for i,n in zip(l1,l2) :
   print(i,n)# first way to do this 

#t =len(l1)
#for i in range(t) :
 # print(l1[i],l2[i])# second way to do this

