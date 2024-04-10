class Stack:
    def __init__(self):
        self.stack = []
        self.minstack = []


    def top(self):
        return self.stack[-1]

    def pop(self):
        ele = self.stack.pop()
        if(ele == self.minstack[-1]):
            self.minstack.pop()
        return ele

    def push(self,value):
        self.stack.append(value)
        if(not self.minstack or self.minstack[-1]>value):
            self.minstack.append(value)

    def getMin(self):
        if(self.minstack):
            return self.minstack[-1]
        return -1

stack = Stack()
arr = [4,3,0,5]
for ele in arr:
    stack.push(ele)
stack.pop()
stack.pop()
print(stack.getMin())