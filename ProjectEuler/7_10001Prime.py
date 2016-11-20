#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#Sample Input
#2
#3
#6
#Sample Output
#
#5
#13

#!/bin/python3
primes=[2]
index=10
x=3
while len(primes)<10001:
    is_x_prime=1
    for n in primes:
        if x%n==0:
            is_x_prime=0
            break
    if is_x_prime==1:
        primes.append(x)
    x+=2
for i in range (int(input())):
    print(primes[int(input())-1])
