import math

def sumofFactors(n) :

   
    if (n % 2 != 0) :
        return 0

    
    res = 1
    for i in range(2, (int)(math.sqrt(n)) + 1) :

        
        count = 0
        curr_sum = 1
        curr_term = 1
        while (n % i == 0) :
            count= count + 1

            n = n // i

            
            if (i == 2 and count == 1) :
                curr_sum = 0

            curr_term = curr_term * i

            curr_sum = curr_sum + curr_term

        res = res * curr_sum


    if (n >= 2) :
        res = res * (1 + n)

    return res





n=int(input("Enter number:"))
sum=sumofFactors(n)
if(n<10):
    print("Invalid Number")
elif(sum == 0):
    print("Please Input Different Number")
else:
    lit=[]
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 0:
                lit.append(i)
    lit.sort(reverse=True)
    print(lit)
    print(sum)