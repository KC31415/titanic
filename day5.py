
def getKidz(data):
    #the math numsrv / numkids * 100
    numkids = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""): # error check for missing data
            if (float(temp[6]) < 16.0):
                numkids = numkids + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkids) * 100

def getGrp(data,sex):
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[5] == sex):
             numgrp = numgrp + 1
             if (temp[1] == "1"):
                 numsurv = numsurv + 1
    return (numsurv / numgrp) * 100
        

#open our titanic database
file = open("titanic.csv", "r") #r is read only; csv = comma seperated value
cols = file.readline() # gets first line of data
data = file.readlines()
file.close()

#create 'game loop' using while

keepgoing = True
while (keepgoing == True):
    key = input ("w for female, k for kids, m for men, q for quit")
    if (key == "q"):
        keepgoing = False
        print ("bye")
    elif (key == "w"):
        k = getGrp(data, "female")
        print(round (k,1))
    elif (key == "m"):
        k = getGrp(data, "male")
        print(round (k,1))
    elif (key == "k"):
        k = getKidz(data)
        print (round(k,1))
    else:
        print ("umm follow instructions please")

