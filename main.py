import math

import single.secant, single.half_div, single.simple_iteration
import system.newton

systems_numbered = [
	"1\tx^3 - y + 4 = 0\n\tx^2 - y + 2 = 0"
]

systems = {
	"1\tx^3 - y + 4 = 0\n\tx^2 - y + 2 = 0": [
		lambda x_vector: x_vector[0] ** 3 - x_vector[1] + 4,
		lambda x_vector: x_vector[0] ** 2 - x_vector[1] + 2,
	]
}

equations_numbered = [
	"x^3 - x + 4",
	"x^2 - x + 2",
	"sin(x)"
]

equations = {
	"x^3 - x + 4": lambda x: x ** 3 - x + 4,
	"x^2 - x + 2": lambda x: x ** 2 - x + 2,
	"sin(x)": lambda x: math.sin(x),
}

f = equations[equations_numbered[2]]
eps = 0.00001
print("half div: ", single.half_div.find_solution(-2, 2, f, eps))
print("secant: ", single.secant.find_solution(-2, f, eps))
print("simple iter: ", single.simple_iteration.find_solution(-1, 1, f, eps))
print("newton: ", system.newton.find_solutions(systems[systems_numbered[0]], [0, 0], eps))
