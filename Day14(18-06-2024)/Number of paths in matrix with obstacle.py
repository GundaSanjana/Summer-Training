#Number of paths in matrix with obstacle
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m or(i==k and j==k)):  
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
k=1
l=2
vi=[]
print(fun(0,0,0))
