class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer for the position to place non-val elements
        pos = 0

        # Iterate through the array with a pointer
        for i in range(len(nums)):
            if nums[i] != val:
                # If the current element is not equal to val, place it at the position 'pos'
                nums[pos] = nums[i]
                pos += 1

        # The value of 'pos' is the number of elements in nums which are not equal to val
        return pos