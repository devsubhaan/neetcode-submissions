class Solution:

    def encode(self, strs):
        result = []
        for s in strs:
            result.append(f"{len(s)}#{s}")
        return "".join(result)

    def decode(self, s):
        result = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
        
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            result.append(s[start:end])
            
            i = end
            
        return result