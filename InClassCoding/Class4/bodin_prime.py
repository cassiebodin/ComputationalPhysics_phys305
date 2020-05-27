#Cassandra Bodin
#phys 305
#HW1 problem 1
#run code by "python bodin_prime.py"

#starting point
start = 1
#ending point
end =  30
print("prime numbers between 1 and 30")
#for a number (num) in the range [1,30]
for num in range(start,end +1):
    count = 0
#i is a number between 2 and num divided by 2 +1. If num is divisible by i or 2 then the loop breaks and it isn't prime. 
    for i in range (2,num//2 +1):
        if (num %i == 0):
            count = count +1
            break
#If it isn't divisible by i or 2 then it prints the value of num. Num should be prime
    if (count == 0 and num !=1):
        print("%d" %num)
