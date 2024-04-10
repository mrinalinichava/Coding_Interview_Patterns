from collections import  defaultdict
import heapq
def kmostfrequent(arr,k):
    d = defaultdict(int)
    res = []
    for ele in arr:
        d[ele]+=1
    maxheap=[(-freq,num) for (num,freq) in d.items()]
    heapq.heapify(maxheap)

    # one way :
    for i in range(k):
        res.append(heapq.heappop(maxheap)[1])

    # second way :
    # list = heapq.nsmallest(k,maxheap)
    # print([val[1] for val in list])
    return res

arr = [1,1,1,2,2,2,2,3,4,4,5,6]
k = 3
print(kmostfrequent(arr,k))





