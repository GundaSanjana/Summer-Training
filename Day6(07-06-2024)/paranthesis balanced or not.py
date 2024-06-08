'''Paranthesis balanced or not.If it is balanced return -1 else return
position where it breaks.
ip1:"(([{}]))"
op1:-1
ip2:"[{()]]"
op2:5
ip3:"[()]()"
op3:-1
ip4:"[(){}{()}]"
op4=-1  '''

def par_bal(s):
    stack = []
    for i, char in enumerate(s):
        if char in "({[":
            stack.append((char, i))
        elif char in ")}]":
            if not stack:
                return i  
            top, top_index = stack.pop()
            if not ((top == '(' and char == ')') or
                    (top == '{' and char == '}') or
                    (top == '[' and char == ']')):
                return i+1  
    if stack:
        return stack[0][1]
    return -1 
s1 = "(([{}]))"
s2 = "[{()]]"
s3 = "[()]()"
s4 = "[(){}{()}]"
print(par_bal(s1))  
print(par_bal(s2))  
print(par_bal(s3)) 
print(par_bal(s4)) 

#or
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
def check(myStr):
    stack = []
    for i, char in enumerate(myStr):
        if char in open_list:
            stack.append((char,i))
        elif char in close_list:
            pos = close_list.index(char)
            if stack and open_list[pos] == stack[-1][0]:
                stack.pop()
            else:
                return i+1
    if not stack:
        return -1
    else:
        return stack[-1][1]
s = input()
print(check(s))

#or
a=input()
s=[]
f=0
c=0
for i in a:
    if(i in '{[('):
        s.append(i)
    elif(not s):
        if(i=='}' and s[-1]=='{' or i==']' and s[-1]=='[' or i=='('
           and s[-1]==')'):
            s.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
    c=c+1
if(f==0):
    print(-1)

    
