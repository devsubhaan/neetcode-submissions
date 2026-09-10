class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        hmap = {}
        testMap= {}

        for val in s1:
            testMap[val] = testMap.get(val,0)+1

        for right in range(len(s2)):
            hmap[s2[right]] = hmap.get(s2[right],0)+1
            if (right-left+1) > len(s1):
                hmap[s2[left]] -=1
                if hmap[s2[left]] == 0:
                    del hmap[s2[left]]
                    
                left+=1
            if testMap == hmap:
                return True
            
        return False