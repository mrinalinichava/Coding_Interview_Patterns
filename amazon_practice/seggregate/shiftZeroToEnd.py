def shiftZerosToEnd(arr):
    # [1,2,0,3,0,4,0,5]
    j = 0
    n = len(arr)
    for i in range(n):
        if(arr[i]!=0 and arr[j]==0):
            arr[i],arr[j]=arr[j],arr[i]
        if(arr[j]!=0):
            j+=1
    return arr

arr = [1, 2, 0, 3, 0, 4, 0, 0,5]
print(shiftZerosToEnd(arr))
