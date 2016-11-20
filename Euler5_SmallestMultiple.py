#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
#What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?
#Sample Input
#2
#3
#10
#Sample Output
#6
#2520

#!/bin/python3
for i in range(int(input())):
    n=int(input())
    ans=n
    while True:
        temp=ans
        for j in range(n,1,-1):
            if ans%j!=0:
                ans+=n
                break
        if temp==ans:
            print(ans)
            break
