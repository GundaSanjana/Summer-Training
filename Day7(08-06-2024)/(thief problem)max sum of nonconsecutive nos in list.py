'''Suppose a thief is stealing the gold in n houses.He should not steal
in consecutive houses.What is the maximum amount of gold he can steal.
ip:[13,9,4,10,5,7]
op:30'''

def all_combinations(l,k):
    ms=0
    max_combination = []
    def fun(curr,start):
        nonlocal ms,max_combination
        if len(curr)==k:
            cs=sum(curr)
            if cs>ms:
                ms=cs
                max_combination=curr
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+2)
        return 
    fun([],0)
    print(max_combination)
    print(ms)
a=[13,9,4,10,5,7]
k=len(a)//2
all_combinations(a,k)

#or
l=[13,9,4,10,5,7]
def fun(l):
    if(len(l)==0):
        return 0
    if(len(l)==1):
        return l[0]
    if(len(l)==2):
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)
print(fun(l))

