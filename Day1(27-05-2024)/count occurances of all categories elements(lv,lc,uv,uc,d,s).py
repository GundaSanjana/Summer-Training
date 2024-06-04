'''list as input and count occurances of following:
ip:
    f46feLK9y56u#@&56hIjbn6KJhA
op:
    lv - 2 #lowercasevowels
    uv -2  #uppercasevowels
    lc -   #lowercaseconsonants
    uc -   #uppercaseconsonants
    d -    #digits
    s -    #special characters'''

'''[def count_character(s):
    counts = {
        "lv": 0,
        "uv": 0,
        "lc": 0,
        "uc": 0,
        "d": 0,
        "s": 0 }
    lv = set("aeiou")
    uv = set("AEIOU")
    for char in s:
        if char in lv:
            counts["lv"] += 1
        elif char in uv:
            counts["uv"] += 1
        elif char.islower():
            counts["lc"] += 1
        elif char.isupper():
            counts["uc"] += 1
        elif char.isdigit():
            counts["d"] += 1
        else:
            counts["s"] += 1
    for char_type, count in counts.items():
        print(f"{char_type} - {count}")
s='f46feLK9y56u#@&56hIjbn6KJhA'
count_character(s)'''

#Second Method
s = 'f46feLK9y56u#@&56hIjbn6KJhA'
uv, uc, lv, lc, d, special = 0, 0, 0, 0, 0, 0

for i in s:
    if i.isupper():
        if i in 'AEIOU':
            uv += 1
        else:
            uc += 1
    elif i.islower():
        if i in 'aeiou':
            lv += 1
        else:
            lc += 1
    elif i.isdigit():
        d += 1
    elif not i.isalnum():
        special += 1

print("uv- ",uv)
print("uc - ",uc)
print("lv - ",lv)
print("lc - ",lc)
print("d - ",d)
print("s - ",special)

