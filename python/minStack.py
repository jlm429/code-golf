class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.min=10000

    def push(self, x):
        self.stack.append(x)
        if x<=self.min:
            self.min=x
            self.minStack.append(x)

    def pop(self):
        if self.stack==[]:
            return
        temp=self.stack.pop()
        if temp==self.min:
            self.minStack.pop()
            if self.minStack!=[]:
                self.min=self.minStack.pop()
                self.minStack.append(self.min)

    def top(self):
        temp=self.stack.pop()
        self.stack.append(temp)
        return temp

    def getMin(self):
        if self.minStack==[]:
            temp=self.stack.pop()
            self.stack.append(temp)
        else:
            temp=self.minStack.pop()
            self.minStack.append(temp)
        return temp





# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(6)
#obj.push(5)
#print obj.stack
#print "minstack=", obj.minStack
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()
        
minStack = MinStack();
minStack.push(395);
print minStack.getMin() #395
print minStack.top() #395
print minStack.getMin() #395
minStack.push(276)
minStack.push(29)
print minStack.getMin() #29
minStack.push(-482)
print minStack.getMin() #-482
minStack.pop()
minStack.push(-108)
minStack.push(-251)
print minStack.stack, minStack.minStack
print minStack.getMin() #-251






