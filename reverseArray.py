class Array:
    def __init__(self, arr):
        self.arr = arr
    
    def reverseTheArraySimpleWay(self): ## Simple Way
        self.arr = self.arr[::-1]
    
    def reverseWithoutInBuildMethod(self):
        newArray = []
        for i in range(len(self.arr)-1,-1, -1):
            newArray.append(self.arr[i])
        
        self.arr = newArray
    
    def iterateArray(self):
        for item in self.arr:
            print(item)
        
        
arr = [1,2,3,4,5]
obj = Array(arr)
# obj.reverseTheArraySimpleWay()
obj.reverseWithoutInBuildMethod()
obj.iterateArray()