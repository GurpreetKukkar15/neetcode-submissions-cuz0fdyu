class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack= []
        for num in operations:            
            if num =="+":
                new_score= stack[-1]+stack[-2]
                stack.append(new_score)
            elif num =="D":
                new_score= 2*stack[-1]
                stack.append(new_score)
            elif num=="C":
                stack.pop()
            else:
                stack.append(int(num))
        return sum(stack)
            


        
            
