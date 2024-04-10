def longestconsecutive(arr):
    s = set(arr)
    n = len(arr)
    max_count = 0
    count = 0
    for i in range(n):
        if(arr[i]-1 not in s):
            count = 1
            while(arr[i]+count in s):
                count = count+1
            max_count = max(max_count,count)
        else:
            continue
    return max_count

arr =[1,9,3,10,4,20,2,19,5,88,6,90,7]
print(longestconsecutive(arr))