class MyStack:

    def __init__(self):
        self.q1= deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        for i in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        

    def pop(self) -> int:
        if self.q1:
            return self.q1.popleft()       

    def top(self) -> int:
        if self.q1:
            return self.q1[0]
        

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False
        
