class Array:
    def __init__(self, num):
        self.num = num
    
    def squareRootOfNumber(self):
        s = 1
        e = self.num
        while(s<=e):
            mid = s+(e-s)//2
            root = mid * mid
            if (root == self.num):
                return mid
            elif (root > self.num):
                e = mid -1
            else:
                s = mid +1
            # check for next value roo 
            root2 =(mid+1) * (mid+1)
            if(root < self.num and root2 >  self.num):
                return mid
        return -1
    
    def squareRootOfNumberBetter(self):
        s = 1
        e = self.num
        ans = -1
        
        while s <= e:
            mid = s + (e - s) // 2
            root = mid * mid

            if root == self.num:
                return mid
            elif root < self.num:
                ans = mid  
                s = mid + 1
            else:
                e = mid - 1
        
        return ans

object = Array(2)
print(object.squareRootOfNumberBetter())