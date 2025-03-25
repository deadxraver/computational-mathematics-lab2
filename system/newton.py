import copy

import config


def find_solutions(f_system, x0, eps):
	...


def solve_linear_system(matrix) -> list[float] | None:
	free_coef = [matrix[i].pop(-1) for i in range(len(matrix))]
	d = determinant(matrix)
	ans = []
	if d == 0: return None
	for i in range(len(matrix)):
		ans.append(determinant(replace_column(matrix, free_coef, i)) / d)
	return ans


def replace_column(matrix, vector, index) -> list[list[float]]:
	new_matrix = copy.deepcopy(matrix)
	for i in range(len(new_matrix)):
		new_matrix[i][index] = vector[i]
	return new_matrix


def exclude_row_and_column(matrix, index):
	new_matrix = copy.deepcopy(matrix)
	new_matrix.pop(0)
	for i in range(len(new_matrix)):
		new_matrix[i].pop(index)
	return new_matrix


def determinant(matrix: list[list[float]]) -> float:
	if len(matrix) == 1:
		return matrix[0][0]
	return sum((1 if i % 2 == 0 else -1) * matrix[0][i] * determinant(exclude_row_and_column(matrix, i)) for i in range(len(matrix)))

