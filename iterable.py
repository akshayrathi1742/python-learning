user = {
    "Name":"akshay",
    "city":"gurugram",
    "age" : 56
}
for item in user:#its print only keys 
    print(item)
for item in user.items():#its print all item in this dictionary
    print(item)
for item in user.values():#its print only value in dictionary
    print(item)        
for keys,value in user.items():# this is short hand to get only keys and value
    print(keys,value)    