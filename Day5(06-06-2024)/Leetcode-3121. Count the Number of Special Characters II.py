#Leetcode-3121. Count the Number of Special Characters II
'''You are given a string word. A letter c is called special if it
appears both in lowercase and uppercase in word, and every lowercase
occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word.
Example 1:
Input: word = "aaAbcBC"
Output: 3
Explanation:
The special characters are 'a', 'b', and 'c'.
Example 2:
Input: word = "abc"
Output: 0
Explanation:
There are no special characters in word.
Example 3:
Input: word = "AbBCab"
Output: 0
Explanation:
There are no special characters in word.
Constraints:
1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters. '''

word="AbBCab"
a=""
c=0
for i in word:
    if(i.islower() and i not in a and i.upper() in word):
        a=a+i
        if(word.rindex(i)<word.index(i.upper())): #rindex means last index
            c+=1
print(c)
        
