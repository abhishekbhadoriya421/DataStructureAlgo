def fibonacci(num):
	if num == 1:
		return  0
	if(num == 2):
		return 1

	return fibonacci(num-1) + fibonacci(num-2)

def optimizeFibo(num):
	if num == 1:
		return  0
	if(num == 2):
		return 1

	previouse = 0
	previouse2 = 1
	ans = previouse + previouse2
	for item in range(3,num+1):
		ans = previouse + previouse2
		previouse = previouse2
		previouse2 =ans
	return ans

print(optimizeFibo(8))