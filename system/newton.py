import copy

import config


def find_solutions(f_system, x0_vector, eps):
	x_vector = x0_vector[:]
	for iters in range(config.MAX_ITERATIONS):
		matrix = []
		for i in range(len(f_system)):
			matrix.append([])
			for j in range(len(f_system)):
				matrix[i].append(derivative(f_system[i], x_vector, j))
			matrix[i].append(-f_system[i](x_vector))
		x_d_vector = solve_linear_system(matrix)
		if x_d_vector is None: return {"solution": x_vector, "iters": iters, "found": False, "msg": "Система приращений не может быть решена"}
		x_vector_new = [x_vector[i] + x_d_vector[i] for i in range(len(x_vector))]
		if max(abs(c) for c in x_d_vector) <= eps: return {"solution": x_vector_new, "iters": iters, "found": True}
		x_vector = x_vector_new
	return {"solution": x_vector, "iters": config.MAX_ITERATIONS, "found": False}


def derivative(f, x_vector, index):
	f_x = f(x_vector)
	x_vector_dx = x_vector[:]
	x_vector_dx[index] += config.dx()
	f_xdx = f(x_vector_dx)
	return (f_x - f_xdx) / config.dx()


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
	return sum((1 if i % 2 == 0 else -1) * matrix[0][i] * determinant(exclude_row_and_column(matrix, i)) for i in
			   range(len(matrix)))
