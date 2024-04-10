def twosum(arr,k):
    n = len(arr)
    d={}
    for i,ele in enumerate(arr):
        req = k-arr[i]
        if(req in d):
            return [d[req],i]
        d[ele] = i

arr = [1,2,3,4,5]
k = 6
print(twosum(arr,k))