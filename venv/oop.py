class Demo:
    a=10
    def __init__(self):
        print('welcome my pracitice section')

    def multiplyvalue(self):
        self.c = self.a*self.a
        print(self.c)
    def sumvalue(self,a,b):
        print(a+b)     
obj=Demo()
obj.multiplyvalue()
obj.sumvalue(10,33)     