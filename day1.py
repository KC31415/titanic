age = 17
pi = 3.14 # this is a float
name = "Mark" # string
iscool = True # boolean

print(age+pi)
print(age - pi)
print(age / pi)
print(age * pi)
niceoutput = round(age * pi,1)
print(niceoutput)

print("Your name is " + name + " and your age is " + str(age))

# sequential, selection, repetition

myage = input("What is your age?: ")
if(int(myage) >= 50):
    print("you are old")
elif(int(myage) <= 19 and int(myage) >= 13):
    print("you are a teen")
elif(int(myage) <= 13 and int(myage) >= 0):
    print("wow, imagine being this young")
elif(int(myage) >= 19 and int(myage) <=30):
    print("how does it feel to be an adult?")
elif(int(myage) >=30 and int(myage) <=50):
    print("I think this is when you are supposed to have your life figured out...have you?")


    
    
    
