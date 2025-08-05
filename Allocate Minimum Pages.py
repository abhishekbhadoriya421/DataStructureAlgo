
def canBeAPossibleSolution(arr,arrayLength,k,item):
    studentCount = 1
    studentSum = 0
    for i in range(0,arrayLength):
        if arr[i] > item: return False
        
        if studentSum + arr[i] <=item:
            studentSum += arr[i]
        else:
            studentCount += 1; 
            studentSum = arr[i]
            
        if (k < studentCount):
            return False
              
    return True      
            


def allocatePages(arr,k):
    high = sum(arr)
    low = max(arr)
    ans = -1
    while(low<=high):
        mid = low + (high - low) //2
        if(canBeAPossibleSolution(arr,len(arr),k,mid)):
            ans = mid
            high = mid -1
        else:
            low = mid + 1
        
    return ans
    

arr = [12,34,67,90]
arr.sort()
# arr = [1, 2, 4, 8, 9]
student = 2

print(allocatePages(arr,student))
