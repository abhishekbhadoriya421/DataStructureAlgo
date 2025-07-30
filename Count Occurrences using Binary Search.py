def findFirst(arr,start,end,target):
    while(start <= end):
        mid = start + (end - start) // 2
        if ((arr[mid] == target and mid == start)
        or (mid > start and arr[mid] == target and arr[mid-1] != target)):
            return mid
        elif mid > start and arr[mid - 1] == target:
            end = mid - 1
        else :
            start = mid + 1
           
def FindLast(arr,start,end,target):
    while(start <= end):
        mid = start + (end - start) // 2
        if ((arr[mid] == target and mid == end)
        or (mid < end and arr[mid] == target and arr[mid+1] != target)):
            return mid
        elif mid < end and arr[mid + 1] == target:
            start = mid + 1
        else :
            end = mid - 1

def findMidElement(arr,size,target):
    start = 0
    end = size - 1
    firstIndex = -1
    endIndex = -1
    while(start<=end):
        mid = start + (end - start) // 2
        if arr[mid] == target:
            firstIndex = findFirst(arr,start,mid,target)
            endIndex = FindLast(arr,mid,end,target)
            return endIndex - firstIndex +1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# arr = [1,2,3,4,5,6,7,8]
# arr2 = [1,1,2,2,2,2,2,8]
# arr2 = [1, 2, 2, 2, 3, 4]
# target = 3
# arr = [1, 2, 2, 3, 3, 3, 4]
# print(findMidElement(arr, len(arr), 3))  # E

arr = [1,1,3,4,5,5,5,5,5]
print(findMidElement(arr, len(arr), 3))
# print(findMidElement(arr2,len(arr2),3))
