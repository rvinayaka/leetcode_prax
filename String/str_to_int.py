string = input()    #? "4193 with words"
                    #! "___-42"

# string = "4193 with words"
post = "+"
neg = "-"

num = ""
for i in range(0, 10):
    num += str(i)


res = ""
for char in string:
    if char in ("-", "+"):
        res += char
        #print(string.index(char))
    elif char in num:
        res += char
        #print("num",string.index(char))

print(res)      #? 4193
                #! -42



