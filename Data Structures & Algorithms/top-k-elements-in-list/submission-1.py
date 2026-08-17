class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            frequency[count].append(num)
        
        result = []
        for i in range(len(frequency)-1, 0, -1):
            for n in frequency[i]:
                result.append(n)
                if len(result) == k:
                    return result