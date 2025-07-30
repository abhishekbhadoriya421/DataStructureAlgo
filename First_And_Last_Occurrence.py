class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def searchTarget(self,target):
        firstIndex = -1
        lastIndex = -1
        for item in range(0, self.size):
            if self.arr[item] == target:
                if firstIndex == -1:
                    firstIndex = item
                lastIndex = item
        return (firstIndex,lastIndex)
   
arr = [5, 2, 5, 1, 5, 6]
Obj = Array(arr,len(arr))


print(Obj.searchTarget(5))