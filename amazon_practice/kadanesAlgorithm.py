import sys
def kadanesAlgorithm(arr):
    #[-2,-3,4,-1,-2,1,5,-3]
    n = len(arr)
    max_final = 0
    curr_max =0
    for i in range(n):
        curr_max = curr_max+arr[i]
        curr_max = max(curr_max,arr[i])
        max_final = max(curr_max,max_final)
    return max_final

arr = [-2,-3,4,-1,-2,1,5,-3]
print(kadanesAlgorithm(arr))



def kadanes_indexes(arr):
    curr_max=0
    max_final= -sys.maxsize
    start = end = s= 0
    for i in range(len(arr)):
        curr_max = curr_max+arr[i]
        if(max_final<curr_max):
            max_final=curr_max
            start = s
            end = i
        if(curr_max<0):
            curr_max=0
            s=s+1

    print("Maximum contiguous sum is %d" % (max_final))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
    return max_final

arr = [-2,-3,4,-1,-2,1,5,-3]
print(kadanes_indexes(arr))
