import argparse

import equations
import visualization.graph_drawer
from visualization.IO import IO
import single.half_div
import single.secant
import single.simple_iteration

help_msg = '''
Данная программа предназначена для решения нелинейных уравнений и систем нелинейных уравнений
'''
parser = argparse.ArgumentParser(description=help_msg)
parser.add_argument('--filename', '-f', help='Использовать файл для ввода данных')

args = parser.parse_args()
io_manager = IO(args.filename)

print('Я хочу решать 1 - уравнение, 2 - систему')
is_system = io_manager.read('', 'Введите 1 или 2', int, lambda x: x == 1 or x == 2) - 1
if is_system:
	print('Доступные системы:')
	[print(f'{i + 1}: {equations.systems_numbered[i]}') for i in range(len(equations.systems_numbered))]
	system_index = io_manager.read('Введите номер: ', f'Номер должен быть от 1 до {len(equations.systems_numbered)}',
								   int, lambda x: 0 < x <= len(equations.systems_numbered)) - 1
else:
	print('Доступные уравнения:')
	[print(f'{i + 1}: {equations.equations_numbered[i]}') for i in range(len(equations.equations_numbered))]
	equation_index = io_manager.read('Введите номер: ',
									 f'Номер должен быть от 1 до {len(equations.equations_numbered)}',
									 int, lambda x: 0 < x <= len(equations.equations_numbered)) - 1
	method_index = io_manager.read('Выберите метод (1 - половинного деления, 2 - секущей, 3 - простой итерации): ',
								   'Введите число от 1 до 3!', int, lambda n: 1 <= n <= 3)
	visualization.graph_drawer.draw_single_graph(equation_index, -20, 20)
	eps = io_manager.read('Введите точность: ', f'Введите число от 0 до 1(не вкл)!', float, lambda x: 0 < x < 1)
	if method_index == 1:
		a = io_manager.read('Введите левую границу: ', 'Введите число!', float)
		b = io_manager.read('Введите правую границу: ', f'Введите число, большее {a}!', float, lambda x: x > a)
		solution = single.half_div.find_solution(a, b,
												 equations.equations[equations.equations_numbered[equation_index]],
												 eps)
		if solution["found"]:
			print(f'Решение: {solution["solution"]}, количество итераций: {solution["iters"]}')
			visualization.graph_drawer.draw_single_graph(equation_index, a - 5, b + 5, solution["solution"],
														 equations.equations[
															 equations.equations_numbered[equation_index]](
															 solution["solution"]))
		else:
			print(f'Решение не найдено, {solution["msg"]}')
	elif method_index == 2:
		x0 = io_manager.read('Введите начальное приближение: ', f'Введите число!', float)
	else:
		a = io_manager.read('Введите левую границу: ', 'Введите число!', float)
		b = io_manager.read('Введите правую границу: ', f'Введите число, большее {a}!', float, lambda x: x > a)
