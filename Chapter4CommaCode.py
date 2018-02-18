#Automate the Boring Stuff Chapter 4 Challenge - Comma Code

#returns string with commas and "and"s, also does not change the string
def commacode(listvalue):
	if len(listvalue) ==1:
		return listvalue[0]
	return '{}, and {}'.format(', '.join(listvalue[:-1]), listvalue[-1])

#This returns a string with commas and "and" but also changes the string
def commacode(listvalue):
    if len(listvalue) == 1:
            return listvalue[0]
    listvalue.insert(-1,'and')
    return ', '.join(listvalue)

#Another possible answer to the Chapter 4 Comma Code challenge
def commaCode(list):
    newString = ''
    newString = newString + (list[0]) + ', '
    for i in range(len(list)-1):
        newString = newString + (list[i]) + ', '
    newString = newString + 'and ' + (list[len(list)-1])
    print (newString)
