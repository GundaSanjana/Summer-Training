'''Take a string from user and print all vowels in uppercase and all
consonants in lowercase.
ip1:
    placements
op1:
    plAcEmEnts
ip2:
    School
op2:
    schOOl'''
s=input()
s1=''
for i in s:
    if(i in 'aeiou'):
        s1+=i.upper()
    elif(not i in 'AEIOU'):
        s1+=i.lower()
print(s1)

