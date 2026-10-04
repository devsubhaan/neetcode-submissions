class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stoneOne = -heapq.heappop(stones)
            stoneTwo = -heapq.heappop(stones)

            if stoneTwo < stoneOne:
                heapq.heappush(stones, -(stoneOne - stoneTwo))

        stones.append(0)
        return abs(stones[0])