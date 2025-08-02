import random

class Array:
    def __init__(self, arr, size):
        self.arr = arr
        self.size = size
    
    def searchInNearlySortedArray(self,target):
        start = 0
        end = len(self.arr) -1
        while start <= end:
            mid = start + (end - start) // 2
            if(self.arr[mid] == target):
                return mid
            elif(start < mid and self.arr[mid-1] == target):
                return mid-1
            elif(end>mid and self.arr[mid+1] == target):
                return mid+1
            elif(self.arr[mid]<target):
                start = mid + 2
            else:
                end = mid - 2
                
        return -1

def generate_nearly_sorted_array(n):
    arr = sorted(random.sample(range(1, 5000), n))  # unique sorted numbers
    for i in range(1, n, 2):  # swap every alternate pair for nearly sorted
        arr[i-1], arr[i] = arr[i], arr[i-1]
    return arr

# Run 1000+ test cases
for i in range(1, 1001):
    size = random.randint(5, 20)  # random array size
    arr = generate_nearly_sorted_array(size)
    target = random.choice(arr) if random.random() > 0.3 else random.randint(1, 5000)
    
    obj = Array(arr, len(arr))
    result = obj.searchInNearlySortedArray(target)
    
    # Validation
    expected = arr.index(target) if target in arr else -1
    if result != expected:
        print(f"❌ Test {i} Failed")
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Your Output: {result}, Expected: {expected}")
        break
else:
    print("✅ All 1000 test cases passed successfully!")
