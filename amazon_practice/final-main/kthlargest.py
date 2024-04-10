import heapq
def kthlargest(arr):

    maxheap = []
    for ele in arr:
        heapq.heappush(maxheap,ele)
        if(len(maxheap)>k):
            heapq.heappop(maxheap)
    return maxheap[0]

arr = [1,2,3,4,5,6,7,8,9]
k =3
print(kthlargest(arr))