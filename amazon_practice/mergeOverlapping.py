def mergeOverlappting(arr):
    arr.sort(key= lambda x:x[0])
    output = []
    for i,ele in enumerate(arr):
        if(not output or output[-1][1]<ele[0]):
            output.append((ele))
        elif(output[-1][1]>arr[i][0]):
            output[-1][1] = max(output[-1][1],ele[1])
    return output

arr = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlappting((arr)))


def minimumPlatfroms(arr):
    arr.sort(key = lambda x:x[0])
    output = []
    count = 0
    for i,ele in enumerate(arr):
        if(not output or output[-1][1]<ele[0]):
            output.append(ele)
        elif(output and output[-1][1]>ele[0]):
            output[-1][1] = max(output[-1][1],ele[1])
            count+=1
    return count
arr = [[1,3],[2,6],[8,10],[9,18], [11,23]]
print(minimumPlatfroms((arr)))
