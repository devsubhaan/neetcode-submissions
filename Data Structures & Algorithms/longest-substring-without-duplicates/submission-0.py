class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxSS = 0
        left = 0
        chrs = set()

        for right in range(len(s)):
            while s[right] in chrs:
                chrs.remove(s[left])
                left+=1
            
            chrs.add(s[right])
            maxSS = max(maxSS, right-left+1)

        return maxSS