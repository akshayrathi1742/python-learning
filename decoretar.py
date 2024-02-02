# def hello(func):
#     func()

# def greet():
#     print('still here')

# a = hello(greet)
# print(a)

def my_decorater(func):
    def wrap_func(*args,**kargs):
        print("*********")
        func(*args,**kargs)
        print('*********')
    return wrap_func    
@my_decorater
def address(name,sarname='rathi'):
    print(name,sarname)
address('akshay')    

