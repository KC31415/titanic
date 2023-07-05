#built in functions - round(), print()

#when using def, if, if you have : and then indent

def getAge(age):
    cat = "baby"
    if (age <= 5):
        cat = "baby"
    elif (age > 5 and age <= 13):
        cat = "kids"
    else:
        cat = "big people"
    return cat

myage = input("enter your age as an interger (ex. 5): ")
print (getAge(int(myage)))

friends = ["anny", "aaron", "kc"]
friends.append("william")
friends.remove("kc")
friends.sort()

for f in friends: 
    if (f == "aaron"):
        print(f + " is cool")
    else:
        print(f + " is ok")

for i in range(3):#it's looping three times, 0[first time], 1[second time], 2[third time]
    print(friends[i])

keepgoing = True
while (keepgoing == True):
    key = input("press q to quit: ")
    if (key == "q"):
        keepgoing = False
        print("bye")

#homework: upload the code to Github - add a README file



