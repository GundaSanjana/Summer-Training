'''Calculate the no of queens that can be placed where the queens
cant be placed in the row and column where elephat is placed.
Elephat can be placed in either 1,2,3 or 4. '''

'''ip:
    6*6
    2
 (1)_ _ _ _ _ r(2)
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
    _ _ _ _ _ _
 (3)_ _ _ _ _ _(4)'''

def solve_n_queen(n,board,row,col,diag,rev_diag,asf):
    if row==n:
        print(asf)
        return
    for i in range(n):
        if col[i]==0 and diag[row+i]==0 and rev_diag[row-i+n-1]==0:
            board[row][i]=1
            col[i]=1
            diag[row+i]=1
            rev_diag[row-i+n-1]=1
            solve_n_queen(n,board,row+1,col,diag,rev_diag,asf+str(row)+"->"+str(i)+" ")
            col[i]=0
            diag[row+i]=0
            rev_diag[row-i+n-1]=0
def main():
    n=4
    board=[[0 for i in range(n)] for j in range(n)]
    col=[0 for i in range(n)]
    diag=[0 for i in range(2*n-1)]
    rev_diag=[0 for i in range(2*n-1)]
    solve_n_queen(n,board,0,col,diag,rev_diag,"")
main()

#or
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")
def is_safe(board,row,col):
    N=len(board)
    for i in range(col):
        if board[row][i]=='Q':
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]=='Q':
            return False
    for i, j in zip(range(row,N,1), range(col,-1,-1)):
        if board[i][j]=='Q':
            return False
    return True
def solve_n_queens_util(board, col):
    N=len(board)
    if col>=N:
        return True
    for i in range(N):
        if is_safe(board,i,col):
            board[i][col]='Q'
            if solve_n_queens_util(board,col+1):
                return True
            board[i][col]='_'  
    return False
def solve_n_queens(N):
    board = [['_' for _ in range(N)] for _ in range(N)]
    if not solve_n_queens_util(board,0):
        print("Solution does not exist")
        return False
    print_board(board)
    count=0
    for row in board:
        for cell in row:
            if cell=='Q':
                count+=1
    print("Number of Q's placed:",count)
N=6
solve_n_queens(N)
 
#or   nqueens with elephant
def nqueen(r):
    if(r==n):
        return
    if(r!=u):
        for c in range(n):
            if(check(r,c)):
                m[r][c]=1
                break
            m[r][c]=0
        return nqueen(r+1)
    else:
        nqueen(r+1)
def check(i,j):
    if(i==u):
        return 0
    elif(j==v):
        return 0
    r=i
    c=j
    for i in range(r+1):
        if(m[i][j]==1):
            return 0
    i=r
    while(i>=0 and j>=0):
        if(m[i][j]==1):
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):
        if(m[r][c]==1):
            return 0
        r=r-1
        c=c+1
    return 1
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
nqueen(0)
print(m)
