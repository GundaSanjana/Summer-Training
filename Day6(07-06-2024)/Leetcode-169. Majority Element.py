#Print the number whose frequency(occurance) is more than half of list.
#Leetcode-169. Majority Element
'''Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋
times. You may assume that the majority element always exists in the
array.
Example 1:
Input: nums = [3,2,3]
Output: 3
Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109'''

'''ip1:[4,8,2,4,4,8,4]
op2:4
ip2:[2,1,2,2]
op2:2
ip3:[6,6,6,6,7]
op3:6
ip4:[1,1,1,2,2,1]
op4:1
ip5:[4,2,4,4,4,8,8]
op:4'''

a=list(map(int,input().split(",")))
max=0
for i in a:
    if(a.count(i)>max):
       max=a.count(i)
       p=i
print(p)

#or
a=list(map(int,input().split(",")))
c=1
p=a[0]
for i in range(1,len(a)):
    if(a[i]==p):
        c=c+1
    else:
        c=c-1
        if(c==0):
            c=1
            p=a[i]
print(p)
