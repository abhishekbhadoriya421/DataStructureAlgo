

def helper(str,s,e):
	if s >= e:
		return True
	print(s,e,str[s],str[e])
	# check if both are valid character
	asciiValueOf_S = ord(str[s])
	asciiValueOf_E = ord(str[e])

	if( ((asciiValueOf_S >= 97 and asciiValueOf_S <=122) or (asciiValueOf_S >= 48 and asciiValueOf_S <=57)) and ((asciiValueOf_E >= 97 and asciiValueOf_E <=122) or  (asciiValueOf_E >= 48 and asciiValueOf_E <=57))):
		if str[s] == str[e]:
			return helper(str,s+1,e-1)
		else:
			return False

	if((asciiValueOf_S < 97 or asciiValueOf_S > 122) and  (asciiValueOf_S < 48 or asciiValueOf_S > 57) ):
		return helper(str,s+1,e)
	else:
		return helper(str,s,e-1)


def checkPali(str):
	new_str = str.lower()
	return helper(new_str,0,len(str)-1)




# str = "A man, a plan, a canal: Panamam"
str = "8V8K;G;K;V;"
# 8V8KGKV
print(checkPali(str))