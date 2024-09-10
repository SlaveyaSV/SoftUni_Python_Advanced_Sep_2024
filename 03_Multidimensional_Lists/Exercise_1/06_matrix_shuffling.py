def valid_indices(indices, rows_count, cols_count):
    return {indices[0], indices[2]}.issubset(range(rows_count)) and {indices[1], indices[3]}.issubset(range(cols_count))


def swap_matrix_elements(indices, matrix):
    row1, col1, row2, col2 = indices
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]


rows, cols = list(map(int, input().split()))
matrix_data = [input().split() for _ in range(rows)]

while True:
    command_input = input().split()

    if command_input[0] == "END":
        break

    indices_list = [int(x) if x.isdigit() else x for x in command_input[1:]]

    if command_input[0] != "swap" or len(indices_list) != 4 or not valid_indices(indices_list, rows, cols):
        print("Invalid input!")
    else:
        swap_matrix_elements(indices_list, matrix_data)
        [print(*row) for row in matrix_data]
