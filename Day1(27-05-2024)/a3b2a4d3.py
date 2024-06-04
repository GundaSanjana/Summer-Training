#Take a string from user ip:aaabbaaaaddd op:a3b2a4d3
#sliding window approach
s='aaabbaaaadddb'
c=1
s1=''
for i in range(len(s)-1):
    if(s[i]==s[i+1]):
        c+=1
    else:
        s1=s1+s[i]+str(c)
        c=1
s1=s1+s[i+1]+str(c) #we can use s[-1] or s[i+1] #we should not use s[i] as it will not work for last element
print(s1)    
    

