aliens = []
for alien_new in range(0,30):
  alien_new = {'colour': 'yelow', 'points': 5,'speed': 'slow'}
  aliens.append(alien_new)
# print(aliens)
for alien_n in aliens[0:3]:
  if alien_n['colour'] == 'green':
    alien_n['colour'] = 'yellow'
    alien_n['speed'] = 'medium'
    alien_n['points'] = 10 
  else:
    alien_n['colour'] == 'yellow'
    alien_n['colour'] = 'red'
    alien_n['point'] = 15
    alien_n['speed'] = 'fast'
for i in aliens[0:5]:
  print(i)  
print("totale no of alien" + str(len(aliens)))  


