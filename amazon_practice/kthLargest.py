import heapq
def kthLargest(nums,k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap,-num)
    size = len(max_heap)
    if(size>k):
        heapq.heappop(max_heap)
    return -max_heap[0]

arr =[3,2,1,5,6,4]
k =3
print(kthLargest(arr,k))