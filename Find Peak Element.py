class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def findPeekElementBruteForce(self):
        previous = -1
        current  = self.arr[0]
        next = self.arr[1] if self.size > 1 else -1

        if previous < current > next : return 0
        else:
            previous = self.arr[0]
            for i in range(1,self.size):
                current = self.arr[i]
                next = self.arr[i+1] if i+1 < self.size else -1
                if previous < current > next:
                    return i
                previous = current
        return -1
    
    def findPeakElementTest(self,arr):
        if(len(self.arr) == 1): return 0
        previousIndex = -1
        previouseVal = -1
        for i in range(0,len(self.arr)):
            current = self.arr[i]
            next = self.arr[i+1] if i+1 < len(self.arr) else -(10**100)
            if(previousIndex >=0):
                if(previouseVal < current > next):
                    return i
            else:
                if current > next:
                    return i
            previouseVal = current
            previousIndex = i
        return -1
    
    def findPeekElementOptimizeForce(self):
        s = 0
        e = self.size - 1
        while(s <= e):
            mid = s + (e-s) // 2
            current = self.arr[mid]
            previous = self.arr[mid-1] if mid-1 >= s else -(10**100)
            next = self.arr[mid+1] if mid+1 <= e else -(10**100)
            if previous < current > next:
                return mid
            elif current < next:
                s = mid + 1
            else:
                e = mid - 1
        return -1
    


nums = [1,2,1,3,5,4,6]
object = Array(nums,len(nums))

print(object.findPeekElementOptimizeForce()) 
