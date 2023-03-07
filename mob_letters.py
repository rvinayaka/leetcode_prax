buttons = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

num = "23"

result = [""]
for digit in num:
    temp = []
    for char in buttons[digit]:
        for combination in result:
            temp.append(combination + char)
    result = temp

print(result)







