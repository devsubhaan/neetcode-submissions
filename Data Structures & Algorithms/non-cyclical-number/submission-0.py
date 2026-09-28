class Solution:
    def isHappy(self, n: int) -> bool:
        
        total = 0
        hmap = set()
        while n not in hmap:
            hmap.add(n)
            total = 0
            while n:
                val = n % 10
                total += val ** 2
                n = n // 10

            n = total
            if n == 1:
                return True
        return False
