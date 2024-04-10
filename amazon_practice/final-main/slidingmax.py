from collections import deque
def slidingmax(arr,k):
    n = len(arr)
    q = deque()
    output = []
    for i,ele in enumerate(arr):

        while(q and q[0]<i-k+1):
            q.popleft()

        while(q and arr[q[-1]]<ele):
            q.pop()
        q.append(i)

        if(i>=k-1):
            output.append(arr[q[0]])
    return output

arr=[4,3,2,1,5,0,2,9]
print(slidingmax(arr,3))