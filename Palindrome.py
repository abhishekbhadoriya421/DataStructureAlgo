def checkPalindrome(num):
    number = num
    reverseNumber = 0
    while(number>0):
        digit = number%10
        reverseNumber = digit + (reverseNumber * 10)
        number = number//10
    
    print(reverseNumber)
    return num == reverseNumber


if(checkPalindrome(122)):
    print("Yes Its Palindrome")
else:
    print("No Its Not Palindrome")
