class Solution:
    def search(self, nums,target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

arr=[4,5,6,7,0,1,2]
sol = Solution()
print(sol.search(arr,0))
