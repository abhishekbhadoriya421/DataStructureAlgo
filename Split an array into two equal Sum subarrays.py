class Array:
    def __init__(self, arr,size):
        self.arr = arr
        self.size = size
    
    def splitAndArrayIntoTwoParts(self):
        rightSum = sum(arr)
        leftSum = 0
        for i in range(0,len(arr)):
            leftSum += arr[i]
            rightSum -=arr[i]
            # print(rightSum,' ',leftSum)
            if(leftSum == rightSum):
                return True
        return False

arr = [1,5,11,5]
arr.sort()
Obj = Array(arr,len(arr))
print(Obj.splitAndArrayIntoTwoParts())