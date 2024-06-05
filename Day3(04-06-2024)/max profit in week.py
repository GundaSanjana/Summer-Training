'''What would the maximum profit made in that week.
we need to buy and sell once compulsory. we cannot buy on saturday and
sell on monday. we sholud buy and sell in the same week.
ip1:15 3 2 7 8 4
     m t w t f s
op1:6
ip2:5 3 2 7 8 4
    m t w t f s
op2:6
ip3:5 4 2 9 1 1
    m t w t f s
op3:7
ip4:9 8 7 6 5 4
    m t w t f s
op4:0 '''

#Brute force method TC:O(n^2)
a=[15,3,2,7,8,4]
pr=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if(a[i]<a[j] and a[j]-a[i]>pr):
            pr=a[j]-a[i]
print(pr)

#or TC:O(n)
a=[15,3,2,7,8,4]
b=a[0]
p=0
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        b=a[i]
    else:
        p=a[i+1]-b
print(p)
