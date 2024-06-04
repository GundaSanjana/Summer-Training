'''Input 2 lists which are sorted of different length. Merge both the lists in
ascending order.
ip:
    2 5 7 9
    1 3 6 7 10 13
op:
    1 2 3 5 6 7 7 9 10 13'''
#simple method
l1=list(map(int,input().split(',')))
l2=list(map(int,input().split(',')))
l3=l1+l2
l3.sort()
print(l3)

#Second Method using merge sort concept
l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
l3=[]
i=0
j=0
while(i<len(l1) and j<len(l2)):
    if l1[i]<l2[j]:
        l3.append(l1[i])
        i+=1
    else:
        l3.append(l2[j])
        j+=1
while(j<len(l2)):
    l3.append(l2[j])    #(or) c.extend(l2[j:])
    j+=1                #(or) no need this line
while(i<len(l1)):       
    l3.append(l1[i])    #(or) c.extend(l1[i:])                
    i+=1                #(or) no need this line
print(l3)
