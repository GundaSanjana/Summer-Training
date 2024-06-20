'''If the input is palindrome print it else print the next nearset
palindrome number'''

'''ip1:122
op1:131
ip2:1234
op2:1331
ip3:24
op3:33
ip4:1112
op4:1221
ip5:7564
op5:7667
ip6:56472
op6:56565
ip7:76583
op7:76667'''

def nearest_palindrome(n):
  n_str=str(n)
  if n_str==n_str[::-1]:
    return int(n_str)
  lower=int(n_str) 
  higher=int(n_str)+1
  while True:
    if str(higher)==str(higher)[::-1]:
      return higher
    lower -=1
    higher +=1
num=int(input())
result=nearest_palindrome(num)
if num==result:
  print(num)
else:
  print(result)
    
