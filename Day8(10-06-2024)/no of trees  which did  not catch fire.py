'''Take a n*n matrix as binary input.1->trees,0->bare lands. If (x,y)
loacation in the matrix catches fire.It can spread fire in left,right,
top,or bottom.It cannot spread fire diagonally.Find the number of trees
which did not catch fire.
ip:
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6
op:
    8 '''

'''n = int(input())
a = []
for i in range(n):
    for j in range(n):
        a.append(list(map(int, input().split(" "))))
x=int(input())
y=int(input())
def fun(x,y):
    if(i<0 or j<0 or i>=n or j>=n or a[i][j]!=1):
        return
    if(a[i][j]==1):
        a[i][j]=2
    fun(i-1,j)
    fun(i,j-1)
    fun(i+1,j)
    fun(i,j+1)
    return 
fun(i,j)
c=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            c+=1
print(c)'''

def trees(grid,row,col):
    rows=len(grid)
    cols=len(grid[0])
    if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]==0:
        return 
    grid[row][col]=0
    trees(grid,row-1,col)
    trees(grid,row+1,col)
    trees(grid,row,col-1)
    trees(grid,row,col+1)
def rem(grid):
    c=0
    for row in grid:
        c+=sum(row)
    return c
grid=[[0,1,1,1,0,1],
        [0,1,0,1,0,0],
        [1,0,1,1,0,0],
        [0,0,0,1,1,1],
        [1,1,0,0,0,1],
        [1,1,1,0,1,0]]
row=4
col=6
trees(grid,row-1,col-1)
print(rem(grid))
