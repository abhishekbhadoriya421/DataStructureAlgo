class Array:
    def __init__(self, array,size):
        self.array = array
        self.size = size
    
    def findPeekBinarySearch(self):
        # handle base case
        if self.size == 1:
            return 0
        if self.size == 2:
            if self.array[0] > self.array[1]:
                return 0
            else:
                return 1
            
        start = 0
        end = self.size - 1
        while(start <= end):
            mid = start +(end - start) // 2
            # All the cases where my code can have the answer
            # print(f"start[{start}]: ",self.array[start])
            # print(f"mid[{mid}]: ", self.array[mid])
            # print(f"end[{end}]: ", self.array[end])
            if(
               (start == end) or
               (mid == start and mid < end and self.array[mid]> self.array[mid+1]) or
               (mid > start and mid < end and self.array[mid] > self.array[mid-1] and self.array[mid] > self.array[mid+1]) or
               (mid == end and mid > start and self.array[mid] > self.array[mid -1 ])
            ):
                return mid
            
            if(mid < end and self.array[mid] < self.array[mid+1] ):
                start = mid + 1
            else :
                end = mid - 1
        
        return -1
    
    def findPeekBinarySearchOptimized(self):        
        start = 0
        end = self.size - 1
        while(start <= end):
            mid = start +(end - start) // 2
            if(start == end):
                return mid
            if(mid < end and self.array[mid] < self.array[mid+1] ):
                start = mid + 1
            else :
                end = mid - 1
        
        return -1

arr = [1, 3, 5, 6, 4, 2]
arr = [1,2,3] 
# arr = [1,3,2]
# arr = [3,2,1] # output 0
obj = Array(arr,len(arr))

print(obj.findPeekBinarySearchOptimized())