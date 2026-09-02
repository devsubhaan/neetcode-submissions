class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newNums = set(nums)

        longestSequence = 0
        for num in newNums:
            if not num-1 in newNums:
                i = 1
                tmp = 1
                while num + i in newNums:
                    tmp +=1
                    i+=1

                if tmp > longestSequence:
                    longestSequence = tmp
        
        return longestSequence



