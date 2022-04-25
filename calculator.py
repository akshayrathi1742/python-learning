
def calculator(num1, sign, num2):

    if sign ==  "+":
       solution =  num1 + num2
    elif sign ==  "*":
        solution =  num1 * num2
    elif sign ==  "-":
       solution = num1 - num2
    elif sign ==  "/":
       solution =  num1 / num2
    else:
        solution = 'error: please enter a valid sign'
        
    return solution

num1 = int(input("enter first number"))
sign = input("enter sign")
num2 = int(input("enter second number"))

print(calculator(num1, sign, num2))