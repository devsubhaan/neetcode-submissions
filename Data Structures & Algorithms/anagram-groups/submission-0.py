class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in hsh:
                hsh[key].append(word)
            else:
                hsh[key] = [word]
        
        return list(hsh.values())
