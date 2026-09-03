class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            '[' : ']',
            '(' : ')',
            '{' : '}',
        }

        stack = []
        for bracket in s:
            if bracket in hm:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                
                if bracket == hm[stack[-1]]: 
                    #check if closing bracket = opening bracket at top of the stack
                    stack.pop()
                else:
                    return False

        return not stack


        