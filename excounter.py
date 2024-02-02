# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
# for item in my_list:
#     counter = counter + item
# print(counter)
import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts').json()
for item in res:
    print(item['title'])
