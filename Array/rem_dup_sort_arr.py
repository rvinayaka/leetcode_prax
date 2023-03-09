
#$ Remove Duplicates from Sorted Array II
#$ each unique element appears at most twice.

arr = [0, 0, 1, 1, 1, 1, 2, 3, 3]
#arr = [1, 1, 1, 2, 2, 3]

k = 1

for i in range(1, len(arr)):
    if arr[i] != arr[i-2]:    #comparing two elements before
        k += 1

print("k", k)  

#? [0, 0, 1, 1, 1, 1, 2, 3, 3]      #7   [0, 0, 1, 1, 2, 3, 3]
#! [1, 1, 1, 2, 2, 3]               #5   [1, 1, 2, 2, 3]  


