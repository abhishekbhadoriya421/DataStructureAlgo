class Array:
    def __init__(self, array,size):
        self.array = array
        self.size = size
    
    def findTargetInRotatedArray(self, target):
        start = 0
        end = self.size - 1
        while start <= end:
            mid = start + (end - start) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[start] <= self.array[mid]:
                if self.array[start] <= target and target < self.array[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if self.array[mid] < target and self.array[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1 
                
# arr = [5, 6, 7, 8, 1, 2, 3, 4]
# target = 2
arr = [48, 0, 6, 14, 21, 31, 35, 36, 37, 39, 41, 44, 45]
target = 21
obj = Array(arr,len(arr))

print(obj.findTargetInRotatedArray(target))