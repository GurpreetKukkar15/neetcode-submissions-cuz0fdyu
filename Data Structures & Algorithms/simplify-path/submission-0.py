class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        names= path.split('/')
        
        for word in names:
            if word=='.' or word=='':
                continue
            elif word=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(word)
        return '/'+ '/'.join(stack)
                



        

