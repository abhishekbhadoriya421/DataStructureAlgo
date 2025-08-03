class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
        
    def leftHelper(self,s,e,target):
        # 99,98,90
        
        while s<=e:
            mid = s+(e-s)//2
            if(self.arr[mid] == target):
                return mid
            elif self.arr[mid] < target:
                s = mid+1
            else:
                e = mid-1
        return -1
    
    def rightHelper(self,s,e,target):
        # 99,98,90
        # 90
        
        while s<=e:
            mid = s+(e-s)//2
            if(self.arr[mid] == target):
                return mid
            elif self.arr[mid] > target:
                s = mid+1
            else:
                e = mid-1
        return -1
    
    def findTargetInMountainArray(self,target):
        s = 0
        e = self.size -1
        while s <= e:
            mid = s+(e-s)//2
            previous = self.arr[mid - 1] if mid > s else float('-inf')
            next = self.arr[mid + 1] if mid < e else float('-inf')
            if(previous < self.arr[mid] > next):
                if self.arr[mid] == target:
                    return mid
                ## search for the element on the left and right side
                left = self.leftHelper(0,mid-1,target)
                right = self.rightHelper(mid+1,self.size-1,target)
                if left != -1 : return left
                if right != -1 : return right
                return -1
            elif self.arr[mid] <= next:
                s = mid + 1
            else:
                e = mid - 1
        return -1
      
        
# arr = [0,10,5,2]
# arr = [0,1,2,2,1]
arr = [18,29,38,59,98,100,99,98,90]
# arr = [90]

Obj = Array(arr,len(arr))
# print(Obj.findTargetInMountainArray(100))   # peak element → should return 5
# print(Obj.findTargetInMountainArray(18))    # left boundary → should return 0
# print(Obj.findTargetInMountainArray(90))    # right boundary → should return 8
# print(Obj.findTargetInMountainArray(59))    # middle ascending → should return 3
# print(Obj.findTargetInMountainArray(38))    # left half → should return 2
# print(Obj.findTargetInMountainArray(1))     # not present → should return -1

# print(Obj.findTargetInMountainArray(900))