class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
    
        # Step 1: Separate positive and non-positive integers
        # Move all non-positive integers to the left side of the array
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap nums[i] to its correct position
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        # Step 2: Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positive integers are in their correct positions, return n + 1
        return n + 1