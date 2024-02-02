#square
my_list = [5,4,3]
print(list(map(lambda item:item**2,my_list)))
#list shorting
a = [(1,5),(-3,2),(4,-1),(8,-5)]
a.sort(key=lambda x: x[1])
print(a)
