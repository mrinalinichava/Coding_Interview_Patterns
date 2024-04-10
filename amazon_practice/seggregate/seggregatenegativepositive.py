def seggregateNegativePositive(arr):
    n = len(arr)
    low = mid = 0
    high = n-1
    while(mid<=high):
        if(arr[mid]==0):
            mid+=1
        elif(arr[mid]<0):
            arr[mid],arr[low]= arr[low],arr[mid]
            low+=1
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
arr =[-1,1,0,2,-4,-5,-6,1,2,0]
print(seggregateNegativePositive(arr))
