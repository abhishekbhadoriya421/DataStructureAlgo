def FindGCD(num1,num2):
	mini = min([num1,num2])
	answer = 1 # because 1 will always be a divisor of any two number
	for i in range(2,mini+1):
		if(num1%i ==0 and num2%i==0):
			answer = i
	return answer

def findGCDBest(num1,num2):

	while(num1>0 and num2>0):
		if(num1>=num2):
			num1 = num1%num2
		else:
			num2 = num2%num1
	
	return num1 if num1!=0 else num2
 
number1 = int(input('Enter Num 1 Value:'))
number2 = int(input('Enter Numb 2 Value:'))

print(findGCDBest(number1,number2))