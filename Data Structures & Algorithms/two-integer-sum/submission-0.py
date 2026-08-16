class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = len(nums)

        for i in range(l):
            for j in range(i+1):
                if nums[i] + nums[j] == target and i != j:
                    return [j,i]
        