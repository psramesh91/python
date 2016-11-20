#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of a given number N?
#Sample Input
#2
#10
#17
#Sample Output
#5
#17

test = int(input())
for _ in range(test):
    n = int(input())
    r = [2] + list(range(3,int(n**0.5)+1,2))
    for i in r:
        while n%i ==0:
            n= int(n/i)
            if n==1:
                print(i)
                break
    if n!=1:
        print(n)
