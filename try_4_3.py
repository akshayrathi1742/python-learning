for i in range(1, 21):
 print(i)

list_1 = list(range(1, 1000001))
print(min(list_1))
print(sum(list_1))
print(max(list_1))         

list_2 =list(range(1, 31))
for i in list_2:
 print(i*3)
  
list_3 = list(range(1, 11))
for i in list_3:
 print(i**2)

list_4 = [i**2 for i in range(1, 11)]# this is list coomprehension
print(list_4)

#1
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
  if i % 2 == 0:
    print(i,"is even")
print ("I predict even num write\n")    

#2
f_name = ("akshay")
l_name = ("Rathi")
if f_name == "akshay" or l_name == "Rathi":
    print(f_name +" "+ l_name +"\n" + "I predict name write\n")
#3
list_1 = ['pizza','orange','mangos,','ladyfinger']
if 'pizza' or 'orange' in list_1 == True:
  print(True)
  

#4
st = ("kamal ia good boy and he is very intelligent")
if "good"  in st:
   print("\nwrite pridiction"+ "\n" + "i predict good write")
else:
   print("worng  pridiction")
#5
name = "\nkamal"
if name == "kamal":
  print(name.upper())
else:
  print(name.lower())
#6
for i in range(1,101):
  if i >= 50 or i % 2 == 0: 
    print(i)