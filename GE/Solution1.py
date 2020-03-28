test_case = [
['a', 'b' , 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n' , 'o', 'p'],
]

#i. Output column at nth position
def findNthColumn(matrix, nth_column):
	no_of_rows = len(matrix)
	no_of_cols= len(matrix[0])
	_output = []
	for i in range(0, no_of_rows):
		_output.append(matrix[i][nth_column-1])
	return _output

#ii. Output row at nth position
def findNthRow(matrix, nth_row):
	return matrix[nth_row-1]

#iii. Output quadrant at nth position
def findNthQuadrant(matrix, _row, _col):
	no_of_rows = len(matrix)
	no_of_cols= len(matrix[0])
	return [matrix[_row][_col], matrix[_row][_col+1], matrix[_row+1][_col], matrix[_row+1][_col+1]]

switcher = { 1: findNthColumn, 2: findNthRow, 3: findNthQuadrant}

cli = True
while(cli):
	try:
		print('Enter 1 for outputting column at nth position.')
		print('Enter 2 for outputting row at nth position')
		print('Enter 3 for outputting quadrant at nth position')
		print('Enter 4 for terminating the process.')
		_input = int(input())
		if isinstance(_input, int):
			if _input > 0 and _input < 3:
				nth_position = int(input('Please enter the nth position: '))
				print(switcher[_input](test_case, nth_position))
			elif _input == 3:
				_col = int(input('Please enter the column number: '))
				_row = int(input('Please enter the row number: '))
				print(switcher[3](test_case, _row-1, _col-1))
			elif _input == 4:
				break
			else:
				print('Invalid option.')
		else:
			print('Please enter a valid option.')
	except:
		print('Invalid input.')
