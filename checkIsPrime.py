def isPrimeBruteForce(num):
	countPrime = 0
	for i in range(1,num+1):
		if num % i == 0:
			countPrime+=1

	return countPrime == 2


def isPrimeOptimize(num):
	for i in range(1,num+1):
		if num % i == 0 and i != 1 and i != num:
			return False
	return True

def isPrimeBest(num):
	countPrime = 0
	i = 1
	while(i*i<=num):
		if num % i == 0:
			countPrime+=1
			if(num//i != i):
				countPrime+=1
		i+=1
	return countPrime == 2


if(isPrimeBest(29)):
	print("This is a prime number")
else:
	print("This is not a prime number")