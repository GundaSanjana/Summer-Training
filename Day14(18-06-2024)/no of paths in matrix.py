def is_valid(x,y,n,m,visited):
    return 0<=x<n and 0<=y<m and not visited[x][y]

def find_all_paths(x,y,n,m,visited,path,paths):
    if x==n-1 and y==m-1:
        paths.append(path+[(x, y)])
        return
    directions=[(0,1),(1,0),(0,-1),(-1,0)]  
    visited[x][y]=True
    for dx, dy in directions:
        new_x,new_y=x+dx,y+dy
        if is_valid(new_x,new_y,n,m,visited):
            find_all_paths(new_x,new_y,n,m,visited,path+[(x,y)],paths)
    visited[x][y]=False
n=4
m=3
visited=[[False]*m for _ in range(n)]
paths=[]
find_all_paths(0,0,n,m,visited,[],paths)
print(len(paths))

#or
def unique_paths_with_paths(m, n):
    def dfs(x,y,visited,path,all_paths):
        if x==m-1 and y==n-1:
            all_paths.append(path[:])  
            return
        visited.add((x, y))
        directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                path.append((nx,ny))
                dfs(nx,ny,visited,path,all_paths)
                path.pop()  
        visited.remove((x,y))
    if m==0 or n==0:
        return 0,[]
    all_paths=[]
    dfs(0,0,set(),[(0, 0)],all_paths)
    
    return len(all_paths),all_paths
num_paths,paths=unique_paths_with_paths(2,3)
print(f"Number of unique paths: {num_paths}")
print("Paths:")
for path in paths:
    print(path)
    
#or
'''def fun(i,j,c):
    if(i>0 or i>=n or j<0 or j>=m):
        return
    if(i==m-1 and j==n-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        fun(i-1,j,c)
    if((i,j-1) not in vi):
        fun(i,j-1,c)
    if((i+1,j) not in vi):
        fun(i+1,j,c)
    if((i,j+1) not in vi):
        fun(i,j+1,c)
    vi.pop()
    return c
n=4
m=3   
vi=[]
print(fun(0,0,0))'''

#or
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m):  
        return 0 
    if(i==n-1 and j==m-1):
        return c+1 
    if (i,j) in vi: 
        return 0 
    vi.append((i,j))
    c += fun(i-1,j,0) 
    c += fun(i,j-1,0)
    c += fun(i+1,j,0)
    c += fun(i,j+1,0)
    vi.pop()
    return c 
n=4
m=3  
vi=[]
print(fun(0,0,0))
