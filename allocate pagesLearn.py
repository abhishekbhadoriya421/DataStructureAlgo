def isPossible(arr, n, m, maxPages):
    # print(maxPages)
    studentCount = 1
    currentPages = 0

    for i in range(n):
        if arr[i] > maxPages:
            return False

        if currentPages + arr[i] > maxPages:
            studentCount += 1
            currentPages = arr[i]
            if studentCount > m:
                return False
        else:
            currentPages += arr[i]

    return True

def allocateBooks(arr, n, m):
    if m > n:
        return -1  # Not enough books

    res = float('inf')
    for maxPages in range(max(arr), sum(arr) + 1):
        if isPossible(arr, n, m, maxPages):
            return
            res = min(res, maxPages)
    return res


arr = [10,20,30,40,50,60,70]
arr.sort()
# arr = [1, 2, 4, 8, 9]
student = 3

print(allocateBooks(arr,len(arr),student))