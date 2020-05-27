#Cassandra Bodin
#lecture 19 random numbers

#generate random 20 numbers using linear congruential generator algorithm
#i=(ai+b)%m for a=4,b=1, m=9, initial seed =3

def lcga():
    a=4
    b=1
    m=9
    seed=3

    for i in range(0,21):
        seed=(a*seed+b)%m
        i+=1
        print(seed)
#lcga()

#estimate probability that 2 students have the same birthday using random number generator. 22 students in the class

import random

def birthday():
    ClassSize = 22
    duplicateCount=0
    numTrials = 10000

    for trial in range(numTrials):
        birthdayList=[]
        for i in range(ClassSize):
            newbirthday=random.randrange(365)
            birthdayList.append(newbirthday)

        foundDuplicate = False
        for num in birthdayList:
            if birthdayList.count(num) >1:
                foundDuplicate = True
        if foundDuplicate == True:
            duplicateCount = duplicateCount +1

    prob = duplicateCount/numTrials
    print("the probability of two people having the same birthday is ", prob)
birthday()
