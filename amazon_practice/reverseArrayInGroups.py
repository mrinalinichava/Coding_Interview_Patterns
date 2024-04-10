def reverseArrayInGroups(arr,k):
    #[1,2,3,4,5,6,7,8]
    i = 0
    n = len(arr)
    while(i<n):
        left = i
        right = min(i+k-1,n-1)
        while(left<right):
            arr[left],arr[right] = arr[right],arr[left]
            left = left+1
            right = right-1
        i = i + k
    return arr

arr = [1,2,3,4,5,6,7,8]
print(reverseArrayInGroups(arr,3))


