#Leetcode 2574
'''Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105'''

#Method1
a=[10,4,8,3]
b=[]
for i in range(len(a)):
    b.append(abs(sum(a[:i])-sum(a[i+1:])))
print(b)   #TC is O(n*n+n)

#Method2
nums=[10,4,8,3]
s=sum(nums)
x=0
r=[]  #Extra space
for i in nums:
    r.append(abs((x)-(s-i-x)))
    x=x+i
print(r) #TC is O(n)

#Third Method
nums=[10,4,8,3]
s=sum(nums)
x=0
j=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(nums)
    
