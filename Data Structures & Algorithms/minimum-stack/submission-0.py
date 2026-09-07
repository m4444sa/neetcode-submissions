class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val) #min of input or toop of prev stack
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1] #only called when stack is nonempty
        
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
