class MinStack:

    def __init__(self):
        self.stack= []
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        else:
            self.min_stack.append(val)
                

    def pop(self) -> None:
        if self.stack:

            if self.stack[-1]==self.min_stack[-1]:
                self.min_stack.pop()
                return self.stack.pop()
            return self.stack.pop()
            
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack and self.min_stack:
            return self.min_stack[-1]
        
