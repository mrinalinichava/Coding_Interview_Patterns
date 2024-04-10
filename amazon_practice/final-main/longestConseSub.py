def longestconsecutivesubsequence(arr):
    #arr= [100,4,200,1,3,2]
    s = set()
    maxcount = 0
    for ele in arr:
        s.add(ele)
    for i,ele in enumerate(arr):
        if(ele-1 in s):
            continue
        else:
            count = 1
            while(ele+count in s):
                count=count+1
            maxcount=max(maxcount,count)
    return maxcount

arr =  [100,4,200,1,3,2,5]
print(longestconsecutivesubsequence(arr))