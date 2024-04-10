def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:  # Found the target
            return mid

        # Determine if the left half is sorted
        if nums[low] <= nums[mid]:
            # If target is in the sorted left half
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # The right half must be sorted
            # If target is in the sorted right half
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Target not found


arr = [4,5,6,7,0,1,2]
k = 2
print(search(arr,k))
