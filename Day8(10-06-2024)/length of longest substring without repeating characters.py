#length of longest substring without repeating characters.
'''ip:abfgresagtyuiofds
op:12'''

'''a="abfgresagtyuiofds"
d={}
s=""
m=0
i=0
while(i<len(a)):
    while(i<len(a)):
        if(a[i] not in s):
            s=s+a[i]
            d[s[i]]=i
        else:
            if(len(s)>m):
                m=len(s)
            s=""
            break
    i=i+1
    i=d[a[i]]+1
print(m)'''

#or
def longes_substr(s):
    start=0
    max_len=0
    d={}
    for i in range(len(s)):
        if s[i] in d and d[s[i]]>=start:
            start=d[s[i]]+1
        d[s[i]]=i
        max_len=max(max_len,i-start+1)
    return max_len
s="abfgresagtyuiofds"
print(longes_substr(s))
