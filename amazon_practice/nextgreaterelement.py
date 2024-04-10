def nextgreater(arr):
    n = len(arr)
    stack = []
    output = [-1]*n
    stack.append(arr[n-1])
    for i in range(n-2,-1,-1):

        while(stack and arr[i]>=stack[-1]):
            stack.pop()

        if(stack and arr[i]<stack[-1]):
            output[i] = stack[-1]

        stack.append(arr[i])
    return output


def nextgreater1(arr):
    n = len(arr)
    stack = []
    output =[-1]*n
    for i in range(n):
        while(stack and arr[stack[-1]]<arr[i]):
            idx = stack.pop()
            output[idx] = arr[i]
        stack.append(i)
    return output


# arr = [3,2,8,7,9,17,12]
arr = [4,5,3,1,0,6]
print(nextgreater(arr))
print(nextgreater1(arr))


