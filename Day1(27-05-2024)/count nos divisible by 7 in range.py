'''count of numbers divisible by 7 in the given range.
ip:
   300
   400
op:
'''
c=0
for i in range(300,401):
    if i%7==0:
        c+=1
print(c)

#Second Method
c1=(400//7)-(300//7)
print(c1)

'''#Third Method
c2=(400-300)//7
print(c2)'''

