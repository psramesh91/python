#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Sample Input
#2
#10
#100
#Sample Output
#10
#44

l=[]
l.append(1)
l.append(2)
for i in range(3,10000):
    a=int(l[i-3])+int(l[i-2])
    if(a)<4000000:
        l.append(a)
        continue
    else:
        break
res=[]
for i in range(0,len(l)):
    if (l[i] % 2) == 0:
        res.append(l[i])
print(sum(res))
