# listslicing

jd_mart = [
'tea',
'peanutbutter',
'chocolates',
'cocacola',
'maggie',
'parle-G',
'bread',
]
jd_mart[0] = 'redbull'
new_mart = jd_mart[:]
new_mart[0] = 'pepsi'
print(new_mart)
print(jd_mart)
# print(jd_mart[0:3])# copy a list