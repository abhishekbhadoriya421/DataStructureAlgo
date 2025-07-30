class Array:
    def __init__(self,arr):
        self.arr = arr
    def searchTheTarget(self, target):
        result = -1
        for i in range(0, len(self.arr)):
            if self.arr[i] == target:
                return i
        return result

arr = [5, 2, 9, 1, 5, 6]

Object = Array(arr)
result = Object.searchTheTarget(61)
print(result)
