class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ret = float('inf')

        while left <= right:
            mid = (left + right) // 2
            totalHours = 0
            for banana in piles:
                totalHours += (banana + mid - 1) // mid

            if totalHours > h:
                left = mid + 1

            if totalHours <= h:
                ret = min(ret, mid)
                right = mid - 1

        return ret
            
