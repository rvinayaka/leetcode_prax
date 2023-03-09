arr = [1, 2, 3]

result = [[]]
for i in range(len(arr)+1):
    for j in range(i):
        result.append(arr[j:i])

print(result)   #? [[], [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]