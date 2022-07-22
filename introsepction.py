class pc:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} year old ')
pc1 =pc('akshay',22)
# pc1.speak()
print(dir(pc1))