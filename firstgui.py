picture = [

[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]

]
for item in picture:
    for x in item:
        if x==1:
            print("*", end = "")
        else:
            print(" ", end="")    
    print("")        