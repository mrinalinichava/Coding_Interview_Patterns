def seggregate012(arr):
    n = len(arr)
    low = mid = 0
    high = n-1
    while(mid<=high):
        if(arr[mid]==1):
            mid = mid+1
        elif(arr[mid] == 0):
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high = high -1
    return arr

arr = [0,1,1,2,2,0,0,1,2,2]
print(seggregate012(arr))