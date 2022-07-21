class user:
    def __init__(self,email):
        self.email=email

    def sing_in(self):
        print('logged in')

class wizard(user):
    def __init__(self,name,power,email):
        user.__init__(self,email)
        self.name=name
        self.power=power

    def attact(self):
        print(f'attact with power of {self.power}')
class archer(user):              
    def __init__(self,name,num_arrow):
        self.name=name
        self.num_arrow=num_arrow
    def attact(self):
        print(f'attacting with arrows : arrows are left {self.num_arrow}')
wizard1=wizard('Akshay','Nano Tachnology','akshayrathi1742@gmail.com')
archer1=archer('kamal',20)
# wizard1.attact()
# archer1.attact()
print(wizard1.email)