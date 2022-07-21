def car_drive():
    age = int(input("Enter your age = "))
    if    age< 18:
        return " waring! 'you are not above 18 so car not powering on "
    elif  age== 18:
        return "you first year of car driveing keep safe"
    elif  age> 18 and age<60:
        return "powering on you can drive this car"
    elif  age>70:
        return " waring! 'You are over age powering off" 

    else:
        return "error"
print(car_drive())                  