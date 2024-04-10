import heapq

def kthsmallest(arr,k):
    minheap = []
    for ele in arr:
        heapq.heappush(minheap,ele)
    print(minheap)
    for i in range(k-1):
        heapq.heappop(minheap)
        print(minheap)
    return minheap[0]

arr =[3,9,1,7,0,5,6]
k = 3
print(kthsmallest(arr,k))
