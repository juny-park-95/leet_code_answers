# To achieve O(logn) runtime complexity, we can use binary search. 
# Binary search is efficient for searching in sorted arrays or lists. 
# The basic idea is to repeatedly divide the search interval in half.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + (right - left) // 2  # To avoid overflow

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half

        # The loop ends when left > right, so the target should be inserted at index left
        return left