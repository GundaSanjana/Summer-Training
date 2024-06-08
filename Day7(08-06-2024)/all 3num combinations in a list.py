#Write a program to print all the possible 3 combinations in a list.

def fun(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            for k in range(j+1,len(a)):
                print(f"{a[i]},{a[j]},{a[k]}")        
a=[3,2,5,4,1,6,8]
fun(a)
print()

#or
def all_combinations(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,2,5,4,1,6,8]
k=3
all_combinations(a,k)

