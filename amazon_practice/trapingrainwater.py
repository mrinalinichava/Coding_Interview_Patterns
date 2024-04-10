# def trappingrainwater(arr):
#     n = len(arr)
#     max_left =[0]*n
#     max_right = [0]*n
#     max_left[0]= arr[0]
#     rain_water = 0
#     for i in range(1,n):
#         max_left[i]=max(max_left[i-1],arr[i])
#     print(max_left)
#     max_right[n-1] = arr[n-1]
#     for i in range(n-2,-1,-1):
#         max_right[i] = max(max_right[i+1],arr[i])
#     print(max_right)
#     for i in range(n):
#         rain_water = rain_water+ (min(max_left[i],max_right[i])-arr[i])
#     return rain_water


def trappingwater(arr):
    n = len(arr)
    minMax = [0]*n
    minMax[0] = arr[0]
    for i in range(1,n):
        minMax[i] = max(minMax[i-1],arr[i])
    for i in range(n-2,-1,-1):
        minMax[i] = max(minMax[i+1],arr[i])
    print(minMax)



arr =[3,0,2,0,4]

print(trappingwater(arr))
# print(trappingrainwater(arr))
