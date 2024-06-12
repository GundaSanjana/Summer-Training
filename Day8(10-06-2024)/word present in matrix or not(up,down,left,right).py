'''ip:
    4
    tued
    fwow
    roer
    drui
    word
op:
    yes '''

def searchword(n,worfs,target):
    rows=len(grid)
    cols=len(grid[0])
    def backtrack(row,col,idx):
        if idx==len(target):
            return True
        if row<0 or col<0 or row>=rows or col>=cols or grid[row][col]!=target[idx]:
            return False
        temp=grid[row][col]
        grid[row][col]='2'        
        dorikindhi=(backtrack(row-1,col,idx+1) or backtrack(row+1,col,idx+1) or backtrack(row,col-1,idx+1) or backtrack(row,col+1,idx+1))        
        grid[row][col]=temp
        return dorikindhi
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==target[0]:
                if backtrack(i,j,0):
                    print("yes")
                    return
    print("no")   
n=int(input())
grid=[]
target="boook"
for i in range(n):
    a=input()
    grid.append(a)
grid=[list(row) for row in grid]
searchword(n,grid,target)


'''def fun(i,j,k,t):
    if(k==len(s)):
       return 1
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=s[k]):
        return
    if(a[i][j]==s[k]):
        a[i][j]=0
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j-1,k+1)
    t=fun(i,j+1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if(a[i][j]==s[0]):
            fun(i,j,1,0)
            if(c==1):
                print("Yes")
                break
if(c==0):
    print("No")'''
