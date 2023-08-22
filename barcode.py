import sys

matrix_A = input(f"Matrix A number of rows and columns: ").split()
matrix_A_row = int(matrix_A[0])
matrix_A_column = int(matrix_A[1])

valid_row_length_A = 0 < matrix_A_row <= 10
valid_column_length_A = 0 < matrix_A_column <= 10
valid_parameters_A = valid_row_length_A and valid_column_length_A

while not valid_parameters_A:
    matrix_A = input(f"Matrix A number of rows and columns: ").split()
    matrix_A_row = int(matrix_A[0])
    matrix_A_column = int(matrix_A[1])
    valid_row_length_A = 0 < matrix_A_row <= 10
    valid_column_length_A = 0 < matrix_A_column <= 10
    valid_parameters_A = valid_row_length_A and valid_column_length_A

matrix_B = input(f"Matrix B number of rows and columns: ").split()
matrix_B_row = int(matrix_B[0])
matrix_B_column = int(matrix_B[1])

valid_row_length_B = 0 < matrix_B_row <= 10
valid_column_length_B = 0 < matrix_B_column <= 10
valid_parameters_B = valid_row_length_B and valid_column_length_B

while not valid_parameters_B:
    matrix_B = input(f"Matrix B number of rows and columns: ").split()
    matrix_B_row = int(matrix_B[0])
    matrix_B_column = int(matrix_B[1])
    valid_row_length_B = 0 < matrix_B_row <= 10
    valid_column_length_B = 0 < matrix_B_column <= 10
    valid_parameters_B = valid_row_length_B and valid_column_length_B
    break

if matrix_A_column != matrix_B_row:
    print(f"Matrix A: ({matrix_A_row}x{matrix_A_column}) Matrix B: ({matrix_B_row}x{matrix_B_column}) cannot be multiplied.")
    sys.exit()

matrix_A = []
row_number_A = 0

print()
for row in range(matrix_A_row):
    row_number_A = row_number_A + 1
    matrix_A_row_user_input = input(f"Matrix A row {row_number_A}: ")
    matrix_A.append(matrix_A_row_user_input)
matrix_A_row_user_input = []

matrix_B = []
row_number_B = 0

print()
for row in range(matrix_B_row):
    row_number_B = row_number_B + 1
    matrix_B_row_user_input = input(f"Matrix B row {row_number_B}: ")
    matrix_B.append(matrix_B_row_user_input)
matrix_B_row_user_input = []
print()

print("Matrix A:")
for row in matrix_A:
    print(" ".join(["{:<6}".format(num) for num in row.split()]))
print()

print("Matrix B:")
for row in (matrix_B):
    print(" ".join(["{:<6}".format(num) for num in row.split()]))
print()

matrix_C = [[0] * matrix_B_column for _ in range(matrix_A_row)]

for a_rows in range(matrix_A_row):
    for b_columns in range(matrix_B_column):
        for b_rows in range(matrix_B_row):
            matrix_C[a_rows][b_columns] += int(matrix_A[a_rows].split()[b_rows]) * int(matrix_B[b_rows].split()[b_columns])

print("Matrix C:")
for row in matrix_C:
    print(" ".join(["{:<6}".format(num) for num in row]))
print()

matrix_T = [[matrix_C[a][b] for a in range(len(matrix_C))] for b in range(len(matrix_C[0]))]

print("Matrix T:")
for row in matrix_T:
    print(" ".join(["{:<6}".format(num) for num in row]))
print()

print(f"Barcode:")
column_sums = [sum(column) for column in zip(*matrix_C)]
barcode = "|".join(str(sum_) for sum_ in column_sums)

print(f"|{barcode}|")
