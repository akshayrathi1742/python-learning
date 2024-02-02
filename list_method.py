my_company =[ 

    'Home applinece',

    'lady clothes',

   'Gents clothes',

    'electronics'

]

    #addingmethod

new_company =['This type of product deliverd my_company']

new_company.append(my_company) 

my_company.append('Toys')

my_company.insert( 4,'bags')

my_company.extend(['football'])    



   # removeing method

# my_company.pop()

# my_company.pop(4)

# my_company.remove('electronics')



# othermeathod





# print(my_company.count('bags'))

# print(my_company.sort()

# print(my_company.reverse())

# print('bags'in my_company)

# my_company.clear()

print(new_company)



#print(list(range(100)))
#list comprehension
n = [m for m in range(1,101) if m%2==0]
# print(n)
#zip function 1
l =[10,20,30,40]
l2 = [1,2,3,4]
t = len(l)
for a,b in zip(l,l2):
    print(a,b)
# another way to do this
for h in range(t):
    print(l[h],l2[h])    