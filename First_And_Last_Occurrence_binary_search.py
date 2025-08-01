class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def firstAndLastOccurrenceOfTarget(self,target):
        midIndex = -1
        s = 0 
        e = len(self.arr) -1
        while(s<=e):
            mid = s + (e - s) // 2
            if(self.arr[mid] == target): ## if target is found get midIndex as min
                midIndex = mid
                break
            elif(self.arr[mid] > target):
                e = mid - 1
            else:
                s = mid + 1
        
        if midIndex != -1:
            # Find First Index
            first = -1
            last  = -1 
            e = midIndex - 1
            while(e >= 0 and self.arr[e] == target):
                first = e
                e -= 1
            
            s = midIndex + 1
            while(s <=  len(self.arr) -1 and self.arr[s] == target):
                last = s
                s += 1
            if first == -1:
                first = midIndex
            if last == -1:
                last = midIndex
            return [first,last]
        else:
            return [-1,-1]
    
    def firstAndLastOccurrenceOfTargetOptimize(self,target):
        midIndex = -1
        s = 0 
        e = len(self.arr) -1
        while(s<=e):
            mid = s + (e - s) // 2
            if(self.arr[mid] == target): ## if target is found get midIndex as min
                midIndex = mid
                break
            elif(self.arr[mid] > target):
                e = mid - 1
            else:
                s = mid + 1
        
        if midIndex != -1:
            # Find First Index
            first = -1
            last  = -1 
            s1 = 0
            e1 = midIndex - 1
            while(s1<=e1):
                mid1 = s1 + (e1 - s1) // 2
                if((self.arr[mid1] == target) and (s1 == mid1 or self.arr[mid1 - 1] != target)):
                    first = mid1
                    break
                else: ## if target not found then it makes sure that target will be found one step ahead
                    if self.arr[mid1] == target:
                        e1 = mid1 - 1
                    else:
                        s1 = mid1 + 1
            
            s2 = midIndex + 1
            e2 = len(self.arr)-1
            while(s2<=e2):
                mid2 = s2 + (e2 - s2) // 2
                if((self.arr[mid2] == target) and (e2 == mid2 or self.arr[mid2 + 1] != target)):
                    last = mid2
                    break
                else: ## if target not found then it makes sure that target will be found one step ahead
                    if self.arr[mid2] == target:
                        s2 = mid2 + 1
                    else:
                        e2 = mid2 - 1
                
            if first == -1:
                first = midIndex
            if last == -1:
                last = midIndex
            return [first,last]
        else:
            return [-1,-1]
    
        
        
 
   
# arr = [5, 2, 5, 1, 5, 6]
# arr = [1, 1, 2, 5, 5, 6]
# arr = [5,5,5,5,5,5,5]
# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8]
arr = [5]

Obj = Array(arr,len(arr))

print(Obj.firstAndLastOccurrenceOfTargetOptimize(5))