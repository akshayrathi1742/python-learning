# if_friend = True
# can_massage = "allow massage" if if_friend else "nat allow to massege"

# print(can_massage)
# shortcutting
#practice
it_magician = False# False replace with true so print if condition
it_expert = True

if it_magician and it_expert:
    print("you are master")
elif  it_magician  and not  it_expert:
    print("you are not expert need more practice")
elif not it_magician:
    print("you need magic power")    