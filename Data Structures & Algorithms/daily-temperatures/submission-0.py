class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        result = [0] * l

        for i in range(l):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prevDay = stack.pop()
                result[prevDay] = i - prevDay
            stack.append(i)

        return result

