def nextGreater(arr):
    stack = []
    n = len(arr)
    output = [-1]*n
    for i,ele in enumerate(arr):
        while(stack and arr[stack[-1]]<arr[i]):
            idx = stack.pop()
            output[idx] = arr[i]
        stack.append(i)
    return output

arr = [4,5,3,1,0,6]
print(nextGreater(arr))