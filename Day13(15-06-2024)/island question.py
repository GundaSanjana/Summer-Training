'''Calculate the number of islands which are distinct.
1-land,0-water
ip:
    5
    0 1 0 0 1 #1  (1,1,1 are connected so they are consired as 1)
    1 0 0 1 1 #1 1
    0 0 0 0 0
    1 0 0 0 0 #1   (1,1 are connected so they are consired as 1)
    1 0 0 0 1 #1
op:5'''

def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
        return 0
    grid[row][col] = '0'
    area = 1
    area += dfs(grid, row-1, col)
    area += dfs(grid, row+1, col)
    area += dfs(grid, row, col-1)
    area += dfs(grid, row, col+1)
    return area
def numIslands(grid):
    if not grid:
        return 0
    count = 0
    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                area = dfs(grid, row, col)
                max_area = max(max_area, area)
                count += 1
    return count, max_area
grid = [['0','1','0','0','1'],
        ['1','0','0','1','1'],
        ['0','0','0','0','0'],
        ['1','0','0','0','0'],
        ['1','0','0','0','1']]
count, largest_island = numIslands(grid)
print(f"Number of islands: {count}, Largest island size: {largest_island}")

#or
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
a=[[0,1,0,0,1],[1,0,0,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,1]]
n=5
m=0
for i in range(n):
    for j in range(n):
        if(a[i][j]==1):
            k=fun(i,j,0)
            if(k>m):
                m=k
            co=co+1
print(co,m)
