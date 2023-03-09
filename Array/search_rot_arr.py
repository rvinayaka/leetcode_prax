
def search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:                         #! check sorted or not
        mid = start + (end-start) // 2

        if arr[mid] == target:                  #! check if target present at middle
            return True
        
        #$ check which half is sorted and if target lies at start or mid or end
                #$ then increase the start and decrease the end
        elif arr[start] == arr[mid] and (arr[end] == arr[mid]):
            start += 1
            end -= 1
        
        #$ check if left part is sorted
        elif arr[start] <= arr[mid]:
            if (arr[start] <= target) and (arr[end] > target):      #$ if yes target lies in left half
                end = mid - 1
            else:                                                   #$ if no target lies in right half
                start = mid + 1
        
        #$ right part is sorted
        else:
            if (arr[mid] < target) and (arr[end] >= target):        #$ if yes target lies in left half
                start = mid + 1
            else:                                                   #$ if no target lies in right half
                end = mid - 1
    return False


arr = [2,5,6,0,0,1,2]
target = 0

print(search(arr, target))