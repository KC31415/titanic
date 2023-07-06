def exData(blist,num):
    for r in range(1,num):
        line = blist [r]
        temp = line.split(",")
        print( "Name of Passenger: " + temp[3] + " /Did this person survived? (0 = no, 1 = yes: " + temp [1] +" /Sex: " + temp [5] + " /Age: " + temp [6] + " /Fare Class: " + temp[2])


fi = open("titanic.csv", "r") #read-only, 'w' means write
biglist = fi.readlines()
fi.close()

print(len(biglist))
print(biglist[0])
exData(biglist,11)


#homework: take the code and make it look good: here is the name; did they survive?; 
