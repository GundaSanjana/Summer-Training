#Minimum no of coins needed to find sum.
'''ip:[1,2,4,5]
sum=15
op:3'''

'''ip:[4,3,7]
sum=16
op:4'''

def min_coins(coins,target):
  dp=[float('inf')]*(target+1)
  dp[0]=0  
  for i in range(1,target+1):
    for coin in coins:
      if coin<=i:
        dp[i]=min(dp[i],dp[i-coin]+1)
  return dp[target] if dp[target]!=float('inf') else -1
coins=[1,2,4,5]
target=15
result=min_coins(coins,target)
if result!=-1:
  print("Minimum coins required:",result)
else:
  print(-1)


