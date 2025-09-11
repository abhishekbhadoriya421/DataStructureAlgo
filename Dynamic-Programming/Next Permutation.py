def reverseArray(array,s,e):
    while(s<e):
        array[s],array[e] = array[e],array[s]
        s+=1
        e-=1
    return array

def nextPermutation(nums):
    index = -1
    e = len(nums) - 2
    while(0<=e):
        if(nums[e]<nums[e+1]):
            index = e
            break
        e-=1
        
    if(index==-1):
        return reverseArray(nums,0,len(nums)-1)

    e = len(nums) - 1
    while(nums[index]>=nums[e]):
        e-=1

    nums[index],nums[e] = nums[e],nums[index]
    return reverseArray(nums,index+1,len(nums)-1)


nums = [1,2,3]
print(nextPermutation(nums))