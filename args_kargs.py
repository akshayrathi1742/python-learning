def func (*args, **kargs):
    total = 0
    for item in kargs.values():
        total += item
    return sum(args)+total
print(func(1,2,3,4,5, num1 = 4,num2 =13 ))
# def high_even(li):
#     my_list = []
#     for item in li:
#         if item % 2== 0:
#             my_list.append(item)
#     return max(my_list)        
# print(high_even([1,3,6,5,13,43,56]))
