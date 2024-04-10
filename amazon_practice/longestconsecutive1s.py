def longestConsecutiveOnes(arr):
    n = len(arr)
    count = 0
    maxcount = 0
    for i,ele in enumerate(arr):
        if(ele ==1):
            count+=1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return maxcount

arr = [1, 1, 0, 1, 1, 1]
print(longestConsecutiveOnes(arr))

arr  = [0,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1]
print(longestConsecutiveOnes(arr))

