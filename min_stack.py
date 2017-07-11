class MinStack(object):
    #minNum = None
    #array = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minNum = None
        self.array = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.array.append(x)
        if x < self.minNum or self.minNum == None: 
            self.minNum = x
        

    def pop(self):
        """
        :rtype: void
        """
        popVal = self.array[-1]
        self.array = self.array[0:len(self.array)-1]
        
        if popVal == self.minNum:
            try:
                self.minNum=min(self.array)
            except ValueError:
                self.minNum = None
    

    def top(self):
        """
        :rtype: int
        """
        return self.array[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minNum
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
