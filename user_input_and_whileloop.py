promt = "\n Tell me something , amd i will repeat it back you:"
promt += "\nEnter 'Quit'to end the program: "
# print(promt)
message = ""
#1
# while message != 'Quit':
    # message = input(promt)
    # both are doing same work
    # if message != 'Quit':
        # print(message)
#2        
# active = True
# while active: 
#     message = input(promt)
#     if message == 'Quit' :
#         active = False
#     else:
#         print(message)       
#3 break loops
# promt2 = "\n enter the name of city you have visited:"
# promt2+= "\n Enter 'Quit'when you are finised"
# while True:
#     city = input(promt2)
#     if city == 'Quit':
#         break
#     else:
#         print("I do love goto" + city.title()+"!")     
#4 use continue
# currunt_number = 0
# while currunt_number < 10:
#     currunt_number +=1
#     if currunt_number %2 == 0:
#         continue
#     else:
#         print(currunt_number)           
#excise7.4
promt3 = "\n enter pizza topings: "
while True:
    custmr = input(promt3)
    if custmr == 'quit':
        break
    else:
        print("You'll add that topping to their pizza " + custmr.title())
    
    

