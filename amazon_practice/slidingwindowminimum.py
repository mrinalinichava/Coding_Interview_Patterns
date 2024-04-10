from collections import deque
def slidingwindowminimum(arr,k):
    n = len(arr)
    #[8,9,12,5,6,7,23]
    dq = deque()
    output = []
    for i in range(n):
        # remove the elements that are out of the boundary
        while(dq and dq[0]<i-k+1):
            dq.popleft()
        while(dq and arr[i]<arr[dq[-1]]):
            dq.pop()
        dq.append(i)
        if(i>=k-1):
            output.append(arr[dq[0]])
    return output

arr = [8,9,12,5,6,7,23]
k = 3
print(slidingwindowminimum(arr,k))



def slidingmin(arr,k):
    dq = deque()
    n = len(arr)
    output = []
    for i in range(n):
        while(dq and dq[0]<i-k+1):
            dq.popleft()
        while(dq and arr[dq[-1]]>=arr[i]):
            dq.pop()

        dq.append(i)
        if(i>=k-1):
            output.append(dq[0])
    return output


arr = [8,9,12,5,6,7,23]
k = 3
print(slidingmin(arr,k))






