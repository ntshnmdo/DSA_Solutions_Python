from collections import deque

class MyStack:

    def __init__(self): # initializer or constructor
        self.q = deque() # deque(): double ended queue.

    def push(self, x: int) -> None:
        self.q.append(x)

    def top(self) -> int:
        return self.q[-1]
    
    def empty(self) -> bool:
        return len(self.q) == 0
    
    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()