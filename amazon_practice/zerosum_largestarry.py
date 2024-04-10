def largest_zero_sum_subarray(arr):
    d = {}
    max_len = 0
    summ = 0
    n = len(arr)
    for i in range(n):
        summ = summ+arr[i]
        if(summ == 0):
            max_len = i+1
        if(summ in d):
            max_len = max(max_len,i - d[summ])
        else:
            d[summ]=i
    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 13]
print(largest_zero_sum_subarray(arr))
