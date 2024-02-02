myfamily = {
            "child1" : {"name" : "Emil","year" : 2004},
            "child2" : {"name" : "Tobias","year" : 2007},
            "child3" : {"name" : "Linus","year" : 2011}
}
people = {'first_name':'akshay',
          'last_name':'rathi',
          'city':'gurugram'
          }
people2 = {'first_name':'ram',
           'last_name':'rathi',
           'city':'goa'
           }
people3 ={'first_name':'rohit',
          'last_name':'yadave',
          'city':'rampura'
          }
all_people =[
            people,
            people2,
            people3
            ]
for info in all_people:
    print(info['first_name'],info['last_name']+ " from ",info['city'])#itrate nestted dict
#giving two arrgument like for k,v in all_people so print key and value when dict not in a list


