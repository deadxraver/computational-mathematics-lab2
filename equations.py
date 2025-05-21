import numpy as np

systems_numbered = [
	"\tx^3 - y + 4 = 0\n\tx^2 - y + 2 = 0",
	"\tsin(x) - y = 0\n\tx - y = 0"
]

systems = {
	systems_numbered[0]: [
		lambda x_vector: x_vector[0] ** 3 - x_vector[1] + 4,
		lambda x_vector: x_vector[0] ** 2 - x_vector[1] + 2,
	],
	systems_numbered[1]: [
		lambda x_vector: np.sin(x_vector[0]) - x_vector[1],
		lambda x_vector: x_vector[0] - x_vector[1],
	]
}

equations_numbered = [
	"x^3",
	"x^2 - x + 4",
	"sin(x)"
]

equations = {
	equations_numbered[0]: lambda x: x ** 3,
	equations_numbered[1]: lambda x: x ** 2 - x + 4,
	equations_numbered[2]: lambda x: np.sin(x),
}
