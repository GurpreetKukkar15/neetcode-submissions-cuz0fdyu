class Solution:
    def isValid(self, s: str) -> bool:
        signs= {'(':')','{':'}','[':']'}
        stack=[]
        for sign in s:
            if sign in signs.values():
                if stack and stack[-1]==sign:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(signs[sign])
        return True if not stack else False
        