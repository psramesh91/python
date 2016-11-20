#The sum of the squares of the first ten natural numbers is 385
#The square of the sum of the first ten natural numbers is 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640
#Find the difference between the sum of the squares of the first N natural numbers and the square of the sum.
#Sample Input
#2
#3
#10
#Sample Output
#22
#2640

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sm=n*(n+1)/2
    smsq=sm*((2*n)+1)/3
    print(int(abs((sm*sm)-smsq)))
