#Leetcode-1859
'''ip:s="is2 sentence4 This1 a3"
op:"This is a sentence" '''

a=input().split()
re=[0]*len(a)
for i in a:
    re[int(i[-1])-1]=i[:-1]
print(' '.join(re))
