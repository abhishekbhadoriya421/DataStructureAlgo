class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def searchInNearlySortedArray(self,target):
        start = 0
        end = len(self.arr) -1
        while start <= end:
            mid = start + (end - start) // 2
            if(self.arr[mid] == target):
                return mid
            elif(start < mid and self.arr[mid-1] == target):
                return mid-1
            elif(end>mid and self.arr[mid+1] == target):
                return mid+1
            elif(self.arr[mid]<target):
                start = mid + 2
            else:
                end = mid - 2
                
        return -1
    
    
        
        
 
   
# arr = [5, 2, 5, 1, 5, 6]
# arr = [1, 1, 2, 5, 5, 6]
# arr = [5,5,5,5,5,5,5]
# arr = [1,2,3,4,6,7,8,9,10]
# arr = [1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8]
arr = [974, 604, 2071, 1179, 3129, 2075, 4163, 4077, 4666, 4516]

Obj = Array(arr,len(arr))

print(Obj.searchInNearlySortedArray(4516))





