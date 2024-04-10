class Stack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self,data):
        self.stack.append(data)
        data = min(data,self.minstack[-1] if self.minstack else data)
        self.minstack.append(data)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def getmin(self):
        return self.minstack[-1]

    def top(self):
        if(self.stack):
            return self.stack[-1]

s= Stack()
arr = [1,2,3,4,5,6]
for ele in arr:
    s.push(arr)
print(s.getmin())
print(s.top())