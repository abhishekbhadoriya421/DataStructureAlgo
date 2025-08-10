def checkArmStrongNumber(num):
	number = num
	result = 0
	while(number>0):
		digit = number%10
		number = number//10
		i = 1
		temp = digit
		while(i<3):
			i+=1
			temp = temp * digit
		result+=temp
	return result == num


if(checkArmStrongNumber(153)):
	print("Yes Its Armstrong Number")
else:
	print("No Its Not Armstrong Number")