class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def binarySearch(self,target):
        start = 0
        last = self.size -1
        countOcc = 0
        while start <= last:
            # Find Mid
            # mid (3 , 6)  3 + (6-3)/2 => 3 + 3/2 => 3 + 1 => 4
            # mid (0 , 6)  0 + (6-0)/2 => 0 + 6/2 => 0 + 3 => 3
            # mid = int(start + (last - start) / 2)
            mid = start + (last - start) // 2
            
            if self.arr[mid] == target:
                ## first i will check all target values from left side
                countOcc+=1
                checkLeft = mid -1
                while(checkLeft>=start and self.arr[checkLeft] == target):
                    countOcc+=1
                    checkLeft-=1
                
                ## check for right element and count all occurrences of target
                checkRight = mid + 1
                while (checkRight <= last and self.arr[checkRight] == target):
                    countOcc+=1
                    checkRight+=1
                
                return countOcc
            elif self.arr[mid] > target:
                last = mid - 1
            else:
                start = mid + 1
        return 0   
        

arr = [1, 2, 2, 2, 3, 4, 5]
Obj = Array(arr,len(arr))
print(Obj.binarySearch(5))