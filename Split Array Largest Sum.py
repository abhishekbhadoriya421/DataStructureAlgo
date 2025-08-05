class Solution:
   
    def canBeAPossibleSolution(self,arr,arrayLength,k,item):
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
        
    def allocatePages(self,arr,k):
        high = sum(arr)
        low = max(arr)
        ans = -1
        while(low<=high):
            mid = low + (high - low) //2
            if(self.canBeAPossibleSolution(arr,len(arr),k,mid)):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
            
        return ans

    def splitArray(self, nums: List[int], k: int) -> int:
        return self.allocatePages(nums,k)
        