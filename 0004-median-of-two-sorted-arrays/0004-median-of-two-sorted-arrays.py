class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        merged = []

        i = 0  # Pointer for nums1
        j = 0  # Pointer for nums2

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Add remaining elements from nums1 or nums2, if any
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        if total_length % 2 == 0:
            # If the total length is even, return the average of the middle two elements
            mid = total_length // 2
            return (merged[mid-1] + merged[mid]) / 2
        else:
            # If the total length is odd, return the middle element
            mid = total_length // 2
            return merged[mid]