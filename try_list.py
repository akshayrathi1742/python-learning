#name = [
      #  'akshay',
    #    'aman',
  #       'kamal',
 #         'rahul'
#]
#massage = " Hello all my dear friend"
#print(name[0] + massage)
#print(name[1]+ massage)
#print(name[2]+ massage)
#print(name[3]+ massage)

guest = [
        'kamal',
        'rahul',
        'rohit',
] 
#print(sorted(guest))
#guest.sort()
massage = " friend i am giveing a party "
guest[0] = 'akshay'
for i in guest :
  print(i + massage)

guest.insert(0,'ramkumar')
print(guest)
guest.insert(3,'laxman')
print(guest)
guest.append('shayam')
print(guest)

appolzi = "sorry i can't invite you"

print(guest.pop()+ " " + appolzi)

print(guest.pop()+ " " +appolzi)

print(guest.pop()+ " " + appolzi)

print(guest.pop()+ " " + appolzi)

print(" only two people invited on dinner")

print(guest)
del guest [0::1] 
print(guest)

