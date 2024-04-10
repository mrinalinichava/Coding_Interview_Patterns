def countOnes(arr):
    def findFirstOne(row):
        n = len(row)
        low = 0
        high = n-1
        while(low<=high):
            mid = (low+high)//2
            if(row[mid]==1 and (mid==0 or row[mid-1]==0)):
                return mid
            elif(row[mid]==0):
                low = mid+1
            else:
                high = mid-1
        return n


    high = len(arr[0])
    count = 0
    for row in arr:
        idx = findFirstOne(row)
        count += (high-idx)
    return count

arr = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]

print(countOnes(arr))


# def countOnes(arr):
#     def findFirstOne(row):
#         n = len(row)
#         low = 0
#         high = n - 1
#         while low <= high:
#             mid = (low + high) // 2
#             if row[mid] == 1 and (mid == 0 or row[mid-1] == 0):
#                 return mid
#             elif row[mid] == 0:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return n  # Return n if there's no 1 in the row to indicate full row of 0s
#
#     count = 0
#     for row in arr:
#         idx = findFirstOne(row)
#         count += len(row) - idx  # Correctly calculate the number of 1s in each row
#     return count
#
# arr = [
#     [0, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 0, 1, 1],
#     [0, 0, 0, 0]
# ]
#
# print(countOnes(arr))
# # Expected Output: 6
