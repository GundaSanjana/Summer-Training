'''Given n no of constraints 1 represents to be inserted, 2 represents
to search and return true or false and 3 represents the search of
prefix and return true or false.'''

'''ip1:
    7
    1 school
    1 world
    1 word
    1 scholar
    2 word
    2 wood
    3 sch
op1:True
   False
   True '''

'''ip2:
    7
    1 car
    1 cap'''

n=int(input())
l=[]
def prefix(l,n):
    for i in l:
        if i.startswith(n):
            return "True"
        else:
            return "False"
for i in range(n):
    m,n=input().split(' ')
    if m=='1':
        l.append(n)
    elif m=='2':
        if n in l:
            print("True")
        else:
            print("False")
    elif m=='3':
        print(prefix(l,n))
    elif m=='4':
        if n in l:
            l.remove(n)
            print(l)
        else:
            print(l)
        
#or
n=int(input())
l=[]
def prefix(l,n):
    c=0
    l=set(l)
    for i in l:
        if i.startswith(n):
            c+=1
    return c
for i in range(n):
    m,n=input().split(' ')
    if m=='1':
        l.append(n)
    elif m=='2':
        if n in l:
            print("True")
        else:
            print("False")
    elif m=='3':
        print(prefix(l,n))
    elif m=='4':
        if n in l:
            l.remove(n)
            print(l)
        else:
            print(l)


