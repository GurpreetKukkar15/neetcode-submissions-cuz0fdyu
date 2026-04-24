from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # Define the operators we care about
        operators = {'+', '-', '*', '/'}

        for char in tokens:
            if char in operators:
                # 1. It's an operator. Pop two numbers.
                # Note: We convert to int() *as we pop*.
                second = int(stack.pop())
                first = int(stack.pop())
                
                # 2. Perform the correct operation
                if char == '+':
                    stack.append(first + second)
                elif char == '-':
                    stack.append(first - second)
                elif char == '*':
                    stack.append(first * second)
                else: # char == '/'
                    # 3. Handle the special "truncate toward zero" division
                    stack.append(int(first / second))
            
            else:
                # 4. It's not an operator, so it's a number.
                # Convert to int() *as we push*.
                stack.append(int(char))
        
        # 5. The final answer is the last item on the stack.
        return stack.pop()