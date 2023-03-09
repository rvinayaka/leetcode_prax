
def answer(string):
    for word in string:
        prefix = ""
        for i, char in enumerate(string[0]):
            for s in string[1:]:
                if i >= len(s) or s[i] != char:
                    return string[0][:i]
    return string[0]


str1 = ["dog","racecar","car"]
str2 = ["flower","flow","flight"]

print(answer(str1))         #? 
print(answer(str2))         #? "fl"