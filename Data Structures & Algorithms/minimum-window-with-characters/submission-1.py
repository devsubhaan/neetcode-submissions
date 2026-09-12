class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l = 0
        res = [-1,-1]
        resLen = float('infinity')

        hmap = {}
        vals = {}

        for val in t:
            vals[val] = vals.get(val,0)+1

        have = 0
        need = len(vals)

        for r in range(len(s)):
            c = s[r]
            hmap[s[r]] = hmap.get(s[r],0)+1

            if c in vals and hmap[c] == vals[c]:
                have +=1

            while have == need:

                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                hmap[s[l]] -=1
                if s[l] in vals and hmap[s[l]] < vals[s[l]]:
                    have-=1
                l +=1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""

                


            
