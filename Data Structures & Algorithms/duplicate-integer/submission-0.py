class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set(n for n in nums)
        return len(nums) != len(x)