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
arr=[]
for i in range(999,99,-1):
    for j in range(999,99,-1):
        x=str(i*j)
        if x==x[::-1]:
            arr.append(int(x))
arr=sorted(list(set(arr)),reverse=True)
n=int(input())
for i in range(n):
    limit=int(input())
    for i in arr:
        if i < limit:
            print(i)
            break
