class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0

        total = len(nums1) + len(nums2)
        mid = total // 2

        previous = 0
        current = 0

        median = 0

        for _ in range(mid + 1):
            previous = current

            if p1 < len(nums1) and (p2 >= len(nums2) or nums1[p1] <= nums2[p2]):
                current = nums1[p1]
                p1 += 1
            else:
                current = nums2[p2]
                p2 += 1

        if total % 2 == 0:
            median = (previous + current) / 2
        else:
            median = current

        return median

