class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
        
    def findPeekElement(self):
        s = 0
        e = self.size -1
        while s <= e:
            mid = s+(e-s)//2
            previous = self.arr[mid - 1] if mid > s else float('-inf')
            next = self.arr[mid + 1] if mid < e else float('-inf')
            
            if(previous < self.arr[mid] > next):
                return mid
            elif self.arr[mid] <= next:
                s = mid + 1
            else:
                e = mid - 1
        return -1
      
        
# arr = [0,10,5,2]
# arr = [0,1,2,2,1]
arr = [18,29,38,59,98,100,99,98,90]
Obj = Array(arr,len(arr))

print(Obj.findPeekElement())