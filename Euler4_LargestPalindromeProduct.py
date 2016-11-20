#A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101=143*707. 
#Find the largest palindrome made from the product of two 3-digit numbers which is less than N.
#Sample Input
#2
#101110
#800000
#Sample Output
#101101
#793397

#!/bin/python3
import math
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=n
    flag=1
    while flag==1:
        if str(i) == str(i)[::-1]:
            for j in range(int(math.sqrt(n)),99,-1):
                    if i%j==0:
                        print(i)
                        flag=0
                        break
        i-=1
