#list,set,dictionary
from multiprocessing.reduction import duplicate


my_list = [char for char in 'hello']
my_list2 =[num for num in range (1,100)]
my_list3 =[num**2 for num in range (1,100)]
my_list4 =[num**2 for num in range (1,100) if num%2 == 0]
# for char in 'hello': first way of doing this
    # my_list.append(char)
print(my_list)

print(my_list2)

print(my_list3)

print(my_list4) 

# exercise first way to do this
list = [
    'd','a','b','c','b','d','f','c','a'
    ]
duplicate = []
for item in list:
    if list.count(item) > 1:
        if item not in duplicate:
            duplicate.append(item)
print(duplicate)         
 # And second way   

duplicate2 = set([x for x in list if list.count(x) > 1])

print(duplicate2)