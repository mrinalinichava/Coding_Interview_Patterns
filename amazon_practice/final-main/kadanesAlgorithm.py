def kadanes(arr):
    #[-2,-3,-9,-10,-4,-1]
    maxsofar = float("-inf")
    currmax =0

    for ele in arr:
        currmax = max(currmax+ele,ele)
        maxsofar = max(currmax,maxsofar)
    return maxsofar
arr = [-2,-3,-9,10,4,-1]
print(kadanes(arr))