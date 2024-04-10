from collections import deque

def slidingmin(arr,k):
    dq = deque()
    n = len(arr)
    output=[]
    for i in range(n):

        while(dq and dq[0]<i-k+1):
            dq.popleft()

        while(dq and arr[dq[-1]]>arr[i]):
            dq.pop()

        dq.append(i)

        if(i>=k-1):
            output.append(arr[dq[0]])

    return output

arr = [3,4,6,5,1,9]
k = 3
print(slidingmin(arr,k))
