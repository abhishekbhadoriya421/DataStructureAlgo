import random

class Array:
    def __init__(self, array, size):
        self.array = array
        self.size = size
    
    # 🔹 YOUR FUNCTION GOES HERE
    def findTargetInRotatedArray(self, target):
        start = 0
        end = self.size - 1
        while start <= end:
            mid = start + (end - start) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[start] <= self.array[mid]:
                if self.array[start] <= target and target < self.array[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if self.array[mid] < target and self.array[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


def rotate_array(arr, pivot):
    """Helper to rotate array at pivot."""
    return arr[pivot:] + arr[:pivot]

def brute_force(arr, target):
    """Simple brute force search to compare results."""
    try:
        return arr.index(target)
    except ValueError:
        return -1

def run_tests(num_tests=1000):
    # Special edge cases before random tests
    edge_cases = [
        ([2], 2),
        ([3,1], 1),
        ([30,40,50,10,20], 10),
        ([2,2,2,3,4,2], 3)
    ]

    for arr, target in edge_cases:
        obj = Array(arr, len(arr))
        result = obj.findTargetInRotatedArray(target)
        expected = brute_force(arr, target)
        if result != expected:
            print(f"❌ Failed edge case arr={arr}, target={target}")
            print(f"Expected: {expected}, Got: {result}")
            return
    
    print("✅ All edge cases passed! Now running random tests...\n")

    # Randomized tests
    passed = 0
    for _ in range(num_tests):
        size = random.randint(1, 20)
        arr = sorted(random.sample(range(0, 50), size))

        pivot = random.randint(0, size - 1)
        rotated_arr = rotate_array(arr, pivot)

        target = random.choice(range(0, 50))

        obj = Array(rotated_arr, len(rotated_arr))
        result = obj.findTargetInRotatedArray(target)
        expected = brute_force(rotated_arr, target)

        if result != expected:
            print(f"❌ Failed for arr={rotated_arr}, target={target}")
            print(f"Expected: {expected}, Got: {result}")
            return

        passed += 1

    print(f"✅ All {passed} random tests passed successfully!")


# Run tests
run_tests(1000)
