class MathProblem:
    def __init__(self,number):
        self.number = number

    def extract_digits(self):
        digits = []
        num = self.number
        while num>0 :
            curDig = num%10
            digits.append(curDig)
            num = num//10

        s = 0
        e = len(digits)-1
        while(s<=e):
            temp = digits[s]
            digits[s] = digits[e]
            digits[e] = temp
            s+=1
            e-=1
        return digits

    def extractDigitsFromAnArray(self,arr):
        digits = []
        s = 0
        for num in arr:
            while num>0 :
                curDig = num%10
                digits.append(curDig)
                num = num//10  
            e = len(digits)-1 
            while(s<=e):
                temp = digits[s]
                digits[s] = digits[e]
                digits[e] = temp
                s+=1
                e-=1  
            s = len(digits)
        return digits

    def extractDigitsFromAnArrayOptimize(self,arr):
        digits = []
        for num in arr:
            tempArray = []
            while num>0 :
                curDig = num%10
                tempArray.append(curDig)
                num = num//10 
            s = 0 
            e = len(tempArray)-1 
            while(s<=e):
                temp = tempArray[s]
                tempArray[s] = tempArray[e]
                tempArray[e] = temp
                s+=1
                e-=1
            digits.extend(tempArray)
        return digits

       


# number = int(input("Enter a number: "))
number = 1
math_problem = MathProblem(number)

print(math_problem.extractDigitsFromAnArrayOptimize([13,256,83,7797]));
# print(math_problem.extract_digits())