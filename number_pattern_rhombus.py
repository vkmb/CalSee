def beautify(matrix, number_of_elements_per_row):
	"""
	@params
	matrix -> A matrix with variable row length
	number_of_elements_per_row -> maxium number of elements which includes both spaces and integers
	@return:
	matrix -> A square matrix with relative padding to each row of input matrix
	@local var
	len_of_spaces -> determines dynamically for more eye pleasing matrix
	"""
	for row in range(len(matrix)):
		No_of_spaces = number_of_elements_per_row - len(matrix[row])
		len_of_spaces = len(str(matrix[-1][-1]))
		for i in range(No_of_spaces//2):
			matrix[row].append(" "*len_of_spaces)
			matrix[row].insert(0, " "*len_of_spaces)
	return matrix


def createIntegerMatrix(int_elements_per_row):
	"""
	@params:
	int_elements_per_row -> list describing number of integer elements to be printed out per row
	@return:
	output_matrix -> A 2d array with respective number  to be printed out in each row
	"""
	output_matrix    = [[] for i in int_elements_per_row]
	int_to_print     = 1
	len_of_digits    = len(str(sum(int_elements_per_row)))

	for i in range(len(int_elements_per_row)):
		int_count = 0
		while (int_count < int_elements_per_row[i]):
			_ = str(int_to_print)
			while(len(_) < len_of_digits):
				_ = "0" + _ 
			output_matrix[i].append(_)
			int_to_print += 1
			int_count += 1
	return output_matrix

no_of_rows       = int(input("Max row no : "))
elements_per_row = [i  for i in range(1, no_of_rows * 2) if(i%2!=0)]
elements_per_row = elements_per_row + sorted(elements_per_row[:-1], reverse=True)
max_no_of_int_elements   = elements_per_row[no_of_rows-1]
output_matrix = createIntegerMatrix(elements_per_row)
output_matrix = beautify(output_matrix, max_no_of_int_elements)

for row in output_matrix:
	for column in row:
		print(column, end=" ")
	print()