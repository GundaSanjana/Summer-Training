class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,s):      
        t=self.root
        for i in s:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
          return False
    def search_prefix(self,s):
        t=self.root
        for i in s:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
    def autofill_prefix(self,s):
        def fun(t,s1):
            if(t.flag==1):
                print(s1)
            for i in t.d:
                fun(t.d[i],s1+i)
        t=self.root
        s1=""
        for i in s:
            if i in t.d:
                s1=s1+i
                t=t.d[i]
            else:
                return
        fun(t,s1)

t1=tries()
n=int(input())
for i in range(n):
    a,b=input().split(' ')
    if a=='1':
      t1.insert(b)
    elif a=='2':
      print(t1.search(b))
    elif a=='3':
      print(t1.search_prefix(b))
    elif a=='4':
        t1.autofill_prefix(b)
