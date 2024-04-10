def firstNonRepeating(arr):
    n = len(arr)
    for i in range(1,n-1):
        if(arr[i]==arr[i-1] and arr[i]!=arr[i+1]):
            continue
        else:
            if(arr[i]!=arr[i-1] and arr[i]!=arr[i+1]):
                return arr[i]
    return -1





arr = [1,1,2,2,3,3,4,5,5,6,6]
print(firstNonRepeating(arr))