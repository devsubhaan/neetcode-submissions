class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        vals = [1] * l

        p = 1
        for i in range(l):
            vals[i] = p
            p *= nums[i]

        s = 1
        for i in range(l-1,-1,-1):
            vals[i] *= s
            s *= nums[i]

        return vals 

        