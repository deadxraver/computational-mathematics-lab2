import numpy as np
import matplotlib.pyplot as plt

import equations


def draw_single_graph(f_index, a=-20, b=20, x0=None, y0=None):
	f = equations.equations[equations.equations_numbered[f_index]]
	x = np.linspace(a, b, 400)
	y = f(x)

	plt.plot(x, y, label=f'Функция: {equations.equations_numbered[f_index]}')

	if x0 is not None and y0 is not None: plt.scatter(x0, y0, color='red')

	plt.title('График функции')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()

	plt.grid(True)
	plt.show()


def draw_system(system_index, a=-20, b=-20, x0=None, y0=None):
	functions = [f for f in equations.equations_numbered[system_index]]
	x = np.linspace(a, b, 400)
	# а я не знаю как нарисовать

	# честно говоря
