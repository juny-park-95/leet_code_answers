class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closestSum = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total

                if abs(total - target) < abs(closestSum - target):
                    closestSum = total

                if total < target:
                    left += 1
                else:
                    right -= 1

        return closestSum
