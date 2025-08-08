import math

def isPossibleAnswer(arr,hours,arrayLength,currentIterator):
    timeTakenToEatBanana = 0
    for item in range(0,arrayLength):
        ceilValue = math.ceil((float(arr[item])/currentIterator))
        timeTakenToEatBanana += ceilValue
        if(timeTakenToEatBanana>hours):
            return False
    
    return True


def kokoEatBanana(arr,hours):
    possibleIteration = sum(arr)
    startIteration = max(arr)
    answer = startIteration
    startIteration -= 1
    possibleIteration+=1
    while startIteration >= 1:
        isPos = isPossibleAnswer(arr,hours,len(arr),startIteration)
        if isPos == True:
            answer = startIteration
        startIteration-=1
        
    return answer

def kokoEatBananaOptimize(arr,hours):
    possibleIteration = sum(arr)
    startIteration = max(arr)
    answer = startIteration
    start = 1
    end = startIteration
    while start <= end:
        mid = start + (end - start) // 2
        isPos = isPossibleAnswer(arr,hours,len(arr),mid)
        if isPos == True:
            end = mid -1
            answer = mid
        else:
            start = mid +1
        
    return answer
    
# piles = [3,6,7,11]
# h = 8

piles = [30,11,23,4,20]
h = 6

print(kokoEatBanana(piles,h))
