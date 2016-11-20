#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

%Sample Input
#2
#10
#100
#Sample Output
#23
#2318
for i in range(int(input())):
    l=(int(input())-1)
    n3=l//3
    n5=l//5
    n15=l//15
    print(((3*(n3*(n3+1)))+(5*(n5*(n5+1)))-(15*(n15*(n15+1))))//2)
