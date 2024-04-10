
def maxicecreams(arr,coins):
    n = len(arr)
    arr.sort()
    total = 0
    count = 0
    for ele in arr:
        total = total + ele
        count+=1
        if(total>=coins):
            break
    return count

arr = [1,3,2,4,1]
print(maxicecreams(arr,7))
