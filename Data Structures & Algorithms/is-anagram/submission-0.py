class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        occ = {}
        if not len(s) == len(t):
            return False
        
        l = len(s)
        for i, char in enumerate(s+t):
            if i < l:
                if char not in occ:
                    occ[char] = 1
                    continue
                
                occ[char] +=1
            else:
                if char not in occ:
                    return False

                occ[char] -=1

                if occ[char] < 0:
                    return False
        return True