s = input()     #"aa"
p = input()     #".*"




result = ""

for i in range(len(s)):
    if len(p) < 2:
        result = False
        break
    elif p[i] == "*":
        result = True
    elif p[i] == ".":
        p.replace(p[i],s[i])

print(result)

