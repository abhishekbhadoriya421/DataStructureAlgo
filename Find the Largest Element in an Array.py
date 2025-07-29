class Array:
    def __init__(self, nums):
        self.nums = nums

    def largestNumberInAList(self):
        result = float('-inf')
        for i in self.nums:
            if i > result:
                result = i
        return result
    

nums = [1111, 8, 7, 56, 90]
obj = Array(nums)
print(obj.largestNumberInAList())
