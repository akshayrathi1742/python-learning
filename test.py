mylist =[
    
        [{'google / organic': '33'},
         {'WSFU / facebook': '29'},
          {'WSFY / WPOP': '15'},
           {'(direct) / (none)': '7'},
            {'linktr.ee / referral': '5'}],

    [{'google / organic': '45'},
     {'WSFU / facebook': '6'},
      {'(direct) / (none)': '4'},
       {'WSFY / WPOP': '2'},
        {'linktr.ee / referral': '1'}],
     
    [{'google / organic': '33'},
     {'(direct) / (none)': '4'},
      {'linktr.ee / referral': '1'}]
]

for item in mylist:
    for x in item:
        x.keys
        print(x)
        
        
        
#         resp = {
#     k: [d.get(k) for d in data if k in d]
#     for k in set().union(*data)
# }