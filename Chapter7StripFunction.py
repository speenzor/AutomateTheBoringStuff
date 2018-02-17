#Automate the Boring Stuff Chapter 7 Challenge

#Make a strip() function using regular expressions
#If nothing in second argument then will remove whitespace

def strip1(string, *remove):
	re1=re.compile(r'\S.*\S')
	re2=re.compile(r'[^('+re.escape(remove)+')].*[^('+re.escape(remove)+')]')
	if remove == None:
		print (re1.search(string).group())
	else:
		print (re2.search(string).group())
