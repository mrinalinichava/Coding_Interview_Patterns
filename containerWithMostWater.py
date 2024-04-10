def containerMostWater(arr):
    # [1,5,4,3]
    # [1,8,6,2,5,4,8,3,7]

    n = len(arr)
    left = 0
    right = n-1
    maxwater = 0
    while(left<=right):
        width = right - left
        minele = min(arr[left],arr[right])
        maxwater = max(maxwater, minele*width)
        if(arr[left]<arr[right]):
            left+=1
        else:
            right-=1
    return maxwater

arr1 = [1,5,4,3]
arr2 = [1,8,6,2,5,4,8,3,7]
print(containerMostWater(arr1))
print(containerMostWater(arr2))

