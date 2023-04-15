# Write a program to make a tea!
w = (input("You are here to make a tea press Enter to make a tea: "))
x = int(input("You choose Sugar in Grams for tea! => "))
y = int(input("You choose tea leaves in gram for tea! => " ))
z = int(input("You choose milk in ml a tea! => " ))


def makeTea():
    if x < 100:
        if y < 30:
            if z < 300:
                print("you can make  a tea")
            else:
                print("you can't make tea")
        else:
            print("you can't make a tea")
    else:
        print("you can't make a tea")

makeTea()
