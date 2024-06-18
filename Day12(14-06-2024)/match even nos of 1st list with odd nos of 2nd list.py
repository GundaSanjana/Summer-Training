'''Take 2 lists as input. Match the even elements of first list with all
the odd elements of second list'''
'''ip:
    6,3,2,9,4,7
    8,7,5,3,6,9
op:
    [13,11,9,15,9,7,5,11,11,9,7,13]'''
            
def fun(l1, l2):
    l3 = []
    even_numbers = [num for num in l1 if num % 2 == 0]
    odd_numbers = [num for num in l2 if num % 2 != 0]
    for even in even_numbers:
        for odd in odd_numbers:
            l3.append(even + odd) 
    return l3
l1 = list(map(int, input().strip().split(",")))
l2 = list(map(int, input().strip().split(",")))
result = fun(l1, l2)
print(result)

def fun(l1, l2):
    l3 = []
    i = 0
    even_numbers = []
    while i < len(l1):
        if l1[i] % 2 == 0:
            even_numbers.append(l1[i])
        i += 1
    j = 0
    odd_numbers = []
    while j < len(l2):
        if l2[j] % 2 != 0:
            odd_numbers.append(l2[j])
        j += 1
    k = 0
    while k < len(even_numbers):
        m = 0
        while m < len(odd_numbers):
            l3.append(even_numbers[k] + odd_numbers[m])
            m += 1
        k += 1
    return l3
l1 = list(map(int, input().strip().split(",")))
l2 = list(map(int, input().strip().split(",")))
result = fun(l1, l2)
print(result)

def fun(l1,l2):
    l3=[]
    i,j=0,0
    while(i<len(l1) and j<len(l2)):
        if(l1[i]%2==0 and l2[j]!=0):
            l3.append(l1[i]+l2[j])
    return l3
l1=list(map(int,input().strip().split(",")))
l2=list(map(int,input().strip().split(",")))
result=fun(l1,l2)
print(result)
