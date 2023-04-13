#Theory >> Number of trailing zeroes in a factorial (n!)
#
# Number of trailing zeroes in n! = Number of times n! 
# is divisible by 10 = Highest power of 10 
# which divides n! = Highest power of 5 in n!
#                               cr.https://www.handakafunda.com/number-of-trailing-zeros/

import random as r
#Counting trailling zero accord to formular
def count_zeros(x):
    count = 0
    while x >= 5:
        x //= 5             # Assigns the result back to x.
        count += x
    return count
#Calculate the factorial result
def factorialReplica(n):
    temp_result = n
    while n > 1:
        temp_result *= (n-1)
        n -= 1
    return temp_result
#Main Loop
while(1):
    nFlag = int(input('Input n for Factorial(n!) : '))
    print(factorialReplica(nFlag))
    print('Number of trailling zero is ', count_zeros(nFlag), ' / input is ', nFlag )
