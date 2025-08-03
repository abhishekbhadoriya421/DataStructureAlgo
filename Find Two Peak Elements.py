class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size

    def findPeakHelper(self,s,e):
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
     
    
    def findPeekTwoElementOptimize(self):
        s = 0
        e = self.size - 1
        mid = s + (e - s)//2
        if self.size == 1:
            return 0
        rightPeek = self.findPeakHelper(mid,e)
        leftPeek = self.findPeakHelper(s,mid)
        result = []
        if rightPeek != -1:
            result.append(rightPeek)
        if leftPeek != -1:
            result.append(leftPeek)
        return result
    
    def findAllPeekElement(self):
        previous = float('-inf')
        current  = self.arr[0]
        result = []
        next = self.arr[1] if self.size > 1 else -1
        if previous < current > next : result.append(0)
        else:
            previous = self.arr[0]
            for i in range(1,self.size):
                current = self.arr[i]
                next = self.arr[i+1] if i+1 < self.size else float('-inf')
                if previous < current > next:
                    result.append(i)
                previous = current
        return result
        
        


# nums = [1, 2, 1, 3, 5, 4, 6]
nums = [1, 2, 1, 3, 5, 4, 6,7,8]
obj = Array(nums, len(nums))
print(obj.findAllPeekElement())

