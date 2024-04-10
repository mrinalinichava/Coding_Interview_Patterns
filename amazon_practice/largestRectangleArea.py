def maxRectangleArea(arr):
    stack = []
    n = len(arr)
    max_area = 0
    area = 0
    for i in range(n):
        count = 1
        while(stack and arr[i]<stack[-1]):
            count+=1
            area = count * (min(stack[-1], arr[i]))
            stack.pop()
        max_area = max(area,max_area)
        print(stack)
        stack.append(arr[i])
    return max_area


arr = [2,1,5,6,2,3]
print(maxRectangleArea(arr))