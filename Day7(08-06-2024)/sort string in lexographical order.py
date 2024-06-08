#sort the string in lexographical order.
'''ip:
    2
    polikujmnhytgbvfredcxswqaz
    abbcdd
    qwryupcsfoghjkldezxvbintma
    ativedoc
op:
    bbddca
    codevita  '''

n=int(input())
b=[]
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1
    
