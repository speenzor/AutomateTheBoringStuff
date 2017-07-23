#Chapter 7 Practice Projects

#Strong Password Detection
#Will tell you if input password is strong. To be considered strong it must have:
#at least 1 digit, 8 or more characters, and have upper and lower case characters
def pw():
	print ('Please print your password:')
	pw = str(input())
	digitRegex= re.compile(r'\d')
	upperRegex= re.compile(r'[A-Z]')
	lowerRegex= re.compile(r'[a-z]')
	lengthRegex= re.compile(r'.{8,}')
	if digitRegex.search(pw) != None and upperRegex.search(pw) != None and lowerRegex.search(pw) != None and lengthRegex.search(pw) != None:
		print('Strong password!')
	else:
		print('Weak password.')

#Make a strip() function using regular expressions
#If nothing in second argument then will remove whitespace
def strip1(string, *remove):
	re1=re.compile(r'\S.*\S')
	re2=re.compile(r'[^('+re.escape(remove)+')].*[^('+re.escape(remove)+')]')
	if remove == None:
		print (re1.search(string).group())
	else:
		print (re2.search(string).group())
