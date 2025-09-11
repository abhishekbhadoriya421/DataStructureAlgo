def findLeaderInAnArray(array):
    result = [array[len(array)-1]]
    maxi = array[len(array)-1]

    end = len(array)-2
    while(end >= 0):
        if(array[end] > maxi):
            maxi = array[end]
            result.append(maxi)
        end-=1
    result.reverse()
    return result



nums = [1, 2, 5, 3, 1, 2]
print(findLeaderInAnArray(nums))