#Take input as an array add even integers seperately,odd integers
#seperately and float values seperately.
'''a=input()
e,o,f=0,0,0.0
for i in a:
    if i%1==0 and i%2==0:
        e+=i
    elif i%1==0 and i%2!=0:
        o+=i
    elif i%1!=0:
        f+=i
print("sum of even numbers:",e)
print("sum of odd numbers:",o)
print("sum of float numbers:",f)'''


a = input()
e = 0
o = 0
f = 0.0
items = a.split(',')
for item in items:
    item = item.strip()  
    if '.' in item:
        num = float(item)
        f += num
    else:
        num = int(item)
        if num % 2 == 0:
            e += num
        else:
            o += num
print("Even Sum:",e)
print("Odd Sum:",o)
print("Float Sum:",f)

