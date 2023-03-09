arr1 = [1, 1, 2]
arr2 = [1, 1, 2, 3, 3]


res = []
for i in arr1:
    if i not in res:
        res += [i]


print(res)  


#? [1, 1, 2]       -> [1, 2]
#? [1, 1, 2, 3, 3] -> [1, 2, 3]




