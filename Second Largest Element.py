class Array:
    def __init__(self,array):
        self.array = array
    
    def secondLargest(self):
        if len(self.array) <=1:
            print("Array does not have enough space")
            return -1 
        firstLargest =float('-inf')
        secondLargest =float('-inf')
        
        for i in self.array:
            if i > firstLargest:
                secondLargest = firstLargest
                firstLargest = i
            elif  i > secondLargest and i < firstLargest:
                secondLargest = i
        
        if secondLargest == float('-inf'):
            print("There is no second largest number in the array")
            return None
        return secondLargest

arr = [5,5,5]
obj = Array(arr)

print(obj.secondLargest())