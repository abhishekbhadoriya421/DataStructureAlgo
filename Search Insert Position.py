class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def searchIndexPosition(self,target):
        start = 0
        end = len(self.arr) -1
        while start <= end:
            mid = start + (end - start) // 2
            if(self.arr[mid] == target):
                return mid
            elif(self.arr[mid] < target):
                start = mid + 1
            else:
                end = mid - 1
                
        return start
    
        
        
 
   
# arr = [5, 2, 5, 1, 5, 6]
# arr = [1, 1, 2, 5, 5, 6]
# arr = [5,5,5,5,5,5,5]
# arr = [1,2,3,4,6,7,8,9,10]
# arr = [1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8]
arr = [6]
Obj = Array(arr,len(arr))

print(Obj.searchIndexPosition(5))