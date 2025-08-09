
def canBeAPossibleSolution(stalls,arrayLength,cows,distance):
    # Brute force approach to check if it is possible to place the cows at the given distance
    count = 1 # we have already placed one cow at starting
    indexOfPreviousCow =  0 # My first cow is always placed at first position
    for currentIndex in range(1,arrayLength):
        distanceBetweenTowCows = stalls[currentIndex] - stalls[indexOfPreviousCow]
        if distanceBetweenTowCows >= distance:
            count+=1
            indexOfPreviousCow = currentIndex
        
        if(count == cows):
            return True
    return False

def aggressiveCowsOptimize(stalls,cows):
    maximumDistance = stalls[-1] - stalls[0]
    ans = 1
    s = 2
    e = maximumDistance
    while(s<=e):
        mid = s + (e-s) // 2
        isPossibleSol = canBeAPossibleSolution(stalls,len(stalls),cows,mid)
        if isPossibleSol:
            ans = max(ans,mid)
            s = mid + 1
        else:
            e = mid - 1
    return ans

        


def aggressiveCowsBruteForce(stalls,cows):
    maximumDistance = stalls[-1] - stalls[0]
    ans = 1
    for dis in range(1,maximumDistance+1):
        possibleSolution = canBeAPossibleSolution(stalls,len(stalls),cows,dis)
        if possibleSolution:
            ans = max(ans,dis)
    return ans

arr = [6,4,3,16,20,7,18,10]
    # [3,4,6,7,10,16,18,20]
arr.sort()
# arr = [1, 2, 4, 8, 9]
cows = 5
print(aggressiveCowsOptimize(arr,cows))

