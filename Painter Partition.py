
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
        print(studentSum)
              
    return True      
            


def painterPartition(arr,k):
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

# def painterPartition(arr,k):
#     high = sum(arr)
#     low = max(arr)
#     ans = -1
#     while(low<=high):
#         if(canBeAPossibleSolution(arr,len(arr),k,low)):
#             ans = low
#         low+=1

arr = [10,20,30,40,50,60,70]
arr.sort()
# arr = [1, 2, 4, 8, 9]
student = 3

print(painterPartition(arr,student))
