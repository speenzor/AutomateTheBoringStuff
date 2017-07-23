#Chapter 6 Table Printer Challenge

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

#This fuction will take the list of lists and print it out into 3 nice columns
def printTable(list):
    colWidths = [0] * len(list)
    for i in range (len(list)):
        colWidths[i]= (len(max(list[i], key=len)))
    for x in range(4):
	    for y in range(len(list)):
		    print(list[y][x].rjust(colWidths[y]+1), end='')
	    print(' ')
