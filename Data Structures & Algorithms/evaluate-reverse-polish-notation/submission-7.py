import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation={'+':op.add,
            '-': op.sub, 
            '/':op.truediv,
            '*':op.mul
            }
        
        stack= []
        for token in tokens:
            if token in operation:
                    right, left= stack.pop(), stack.pop()
                    stack.append(int(operation[token](left, right)))

            else:
                stack.append(int(token))
        return stack.pop()

