def segregate01s(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        if arr[start] == 1 and arr[end] == 0:
            arr[start], arr[end] = arr[end], arr[start]  # Corrected the typo here
            start += 1
            end -= 1
        elif arr[start] == 0:
            start += 1
        elif arr[end] == 1:  # Changed this condition to check for 1 instead of 0
            end -= 1
    return arr

arr = [1,0,0,1,1,0,1]
print(segregate01s(arr))
