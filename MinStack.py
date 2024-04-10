class Stack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def top(self):
        return self.stack[-1]

    def push(self,data):
        self.stack.append(data)
        if(not self.minstack or data<self.minstack[-1]):
            self.minstack.append(data)

    def getMin(self):
        return self.minstack[-1]

    def pop(self):
        ele = self.stack.pop()
        if(self.minstack and self.minstack[-1] == ele):
            self.minstack.pop()
        return ele


stack = Stack()
stack.push(9)
stack.push(6)
stack.push(4)
stack.push(5)
stack.push(7)
stack.push(1)
stack.push(0)
stack.push(2)
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
print(stack.minstack)
print(stack.stack)
stack.pop()
print(stack.getMin())


