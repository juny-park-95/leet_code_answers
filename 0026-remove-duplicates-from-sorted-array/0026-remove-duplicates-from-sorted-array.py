class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # Initialize pointers
        slow = 0

        # Iterate through the array with the fast pointer
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        # The first 'slow + 1' elements are the unique elements
        return slow + 1