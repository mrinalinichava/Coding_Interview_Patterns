import unittest
def reverseArrayInGroup(arr,k):
    n = len(arr)
    for i in range(0,n,k):
        left = i
        right = min(n-1,i+k-1)
        while(left<=right):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
    return arr

arr =[1,2,3,4,5,6,7,8]
print(reverseArrayInGroup(arr,3))


def testReveseInGroups():
    assert(reverseArrayInGroup([1,2,3],3)==[3,2,1],"Test1 failed")
    assert(reverseArrayInGroup([1,2,3,4,5],2)== [2,1,4,3,5], "Test 2 failed")
    assert reverseArrayInGroup([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == [3, 2, 1, 6, 5, 4, 9, 8, 7], "Test 3 failed"


testReveseInGroups()