#Leetcode-3120. Count the Number of Special Characters I
'''You are given a string word. A letter is called special if it appears
both in lowercase and uppercase in word.
Return the number of special letters in word.
Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters in word are 'a', 'b', and 'c'.
Example 2:
Input: word = "abc"
Output: 0
Explanation:
No character in word appears in uppercase.
Example 3:
Input: word = "abBCab"
Output: 1
Explanation:
The only special character in word is 'b'.
Constraints:
1 <= word.length <= 50
word consists of only lowercase and uppercase English letters. '''

word="aaAbcBC"
ls=set()
us=set()
c=0
for i in word:
    if i.islower():
        ls.add(i)
    elif i.isupper():
        us.add(i)
for i in ls:
    if i.upper() in us:
        c+=1
print(c)

#or
word="aaAbcBC"
a=set(word)
c=0
for i in a:
    if(i.islower() and i.upper() in a):
        c+=1
print(c)
