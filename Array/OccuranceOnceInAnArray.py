
def findOccurance(array):
    ans = 0
    for i in array:
      ans = ans ^ i
    return ans  



array = [1,2,3,3,6,2,1,4,5,4,5]
print(findOccurance(array))