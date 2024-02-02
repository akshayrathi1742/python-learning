def getdate():
    import datetime
    return datetime.datetime.now()
def fitness(k):
    if k==1:
        c = int(input("press 1 for ex and press 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("rahul.txt","a")as first:
                first.write(str[str(getdate())]+":"+value+"\n")
            print ("successfully written")       
        elif (c==2):
             value = input("type here\n")
             with open("rahul.txt","a")as first:
                first.write(str[str(getdate())]+":"+value+"\n")
    elif (k==2):
        c = int(input("press 1 for ex and press 2 for food"))
        if (c==1):
            value = input("type here\n")
            with open("boxer.txt"  ,"a")as first:
                first.write(str[str(getdate())]+":"+value+"\n")
            print ("successfully written")       
        elif (c==2):
             value = input("type here\n")
             with open("boxer.txt","a")as first:
                first.write(str[str(getdate())]+":"+value+"\n")
                 