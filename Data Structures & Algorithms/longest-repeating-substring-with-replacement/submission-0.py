class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        hashMap = {}
        max_len = 0
        max_f = 0

        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right],0) +1

            max_f = max(max_f, hashMap[s[right]])

            while right-left+1-max_f > k: #substring length - max frequency
                hashMap[s[left]] -=1
                left+=1

            max_len = max(max_len, right-left+1)
        
        return max_len

