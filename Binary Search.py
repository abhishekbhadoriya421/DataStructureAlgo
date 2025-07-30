class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def binarySearch(self,target):
        start = 0
        last = self.size -1
        
        while start <= last:
            # Find Mid
            # mid (3 , 6)  3 + (6-3)/2 => 3 + 3/2 => 3 + 1 => 4
            # mid (0 , 6)  0 + (6-0)/2 => 0 + 6/2 => 0 + 3 => 3
            # mid = int(start + (last - start) / 2)
            mid = start + (last - start) // 2
            
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                last = mid - 1
            else:
                start = mid + 1
        return -1   
        

arr = [1, 2, 3, 4, 7, 9,18]
Obj = Array(arr,len(arr))
print(Obj.binarySearch(7))