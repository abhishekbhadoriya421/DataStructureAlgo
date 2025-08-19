def mergeTwoSortedArray(array1,array2):
    n = len(array1)
    m = len(array2)
    newSortedArray = []
    i = 0 
    j = 0
    while(i<n and j<m):
        if(array1[i]<array2[j]):
            newSortedArray.append(array1[i])
            i+=1
        else:
            newSortedArray.append(array2[j])
            j+=1
    
    while(i<n):
        newSortedArray.append(array1[i])
        i+=1
        
    while(j<m):
        newSortedArray.append(array2[j])
        j+=1
        
    return newSortedArray

def mergeTwoSortedArrayWithoutExtraSpace( nums1 , m , nums2, n):
    i = m -1 # all positive intger greater than 0 in nums1
    k = len(nums1) -1 # contain's 0 from last 
    j = n - 1 # all positive intger greater than 0 in nums2
    
    while(i>=0 and k>0 and j >=0):
        #check which is greater in between nums1 and nums2 from backward
        if(nums1[i]>nums2[j]):
            temp = nums1[i]
            nums1[i] =  nums1[k]
            nums1[k] = temp
            k-=1
            i-=1
        else:
            temp = nums1[k]
            nums1[k] =  nums2[j]
            nums2[j] = temp
            j-=1
            k-=1

        #handle the edge case 
    while(j>=0 and k>=0):
        temp = nums1[k]
        nums1[k] =  nums2[j]
        nums2[j] = temp
        j-=1
        k-=1
    print(nums1)
    


# array1 = [1,3,5,7,8]
# array2 = [2,4,6,9]
# newSortedArray = mergeTwoSortedArray(array1,array2)
# print(newSortedArray)

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# mergeTwoSortedArrayWithoutExtraSpace(nums1,m,nums2,n)
# mergeTwoSortedArrayWithoutExtraSpace([1,2,3,0,0,0],3,[4,5,6],3)
mergeTwoSortedArrayWithoutExtraSpace([4,5,6,0,0,0],3,[1,2,3],3)