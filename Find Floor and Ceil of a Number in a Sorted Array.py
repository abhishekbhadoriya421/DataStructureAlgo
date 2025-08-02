class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def findFloorAndCeil(self,target):
        start = 0
        end = len(self.arr) -1
        floor = -1
        ceil = -1
        while start <= end:
            mid = start + (end - start) // 2
            if  self.arr[mid] == target:
                return target,target
            elif self.arr[mid] > target:
                ceil = self.arr[mid]
                end = mid - 1
            else:
                floor = self.arr[mid]
                start = mid + 1  
        return [floor,ceil]
    
    
        

arr = [8, 10]
Obj = Array(arr,len(arr))
print(Obj.findFloorAndCeil(7))





