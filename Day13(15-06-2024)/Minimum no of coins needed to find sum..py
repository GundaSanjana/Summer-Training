#Minimum no of coins needed to find sum.
def min_coins(coins,target):
  dp=[float('inf')]*(target+1)
  dp[0]=0  
  for i in range(1,target+1):
    for coin in coins:
      if coin<=i:
        dp[i]=min(dp[i],dp[i-coin]+1)
  return dp[target] if dp[target]!=float('inf') else -1
coins=[1,3,4,5]
target=17
result=min_coins(coins,target)
if result!=-1:
  print("Minimum coins required:",result)
else:
  print(-1)

#or
def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=list(map(int,input().split(',')))
n=int(input())
fun()


