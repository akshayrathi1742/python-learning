dictionary = {
  123:[1,2,3],
  'greet': 'hellow',
  'honda':'city',
  't': 'hello'
}

str = 'aksttrd'
print(str[3])
print(object)
print(dictionary[str[3]])
user = {
  'basket':'1,2,3',
  'greet' :'ram',
  'age'   : 20 
} 
user.update({'age':50})
user.get('age', 55)# 55 is a default value
# print(user)
print('age' in user)# key exist in user so he print True another False
print(user.keys())# for find keys in user and used to find value
print(user.items())# fint to items
print(user.clear())#clear to all items in  user
# .copy()is used to copy all items from a dictionary
# user.pop('greet')# remove a key from dictinoary 
# print(user)  
