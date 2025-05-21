import config


def derivative(f, x0):
	return (f(x0 + config.dx()) - f(x0)) / config.dx()


def find_solution(a, b, f, eps):
	phi = lambda x: f(x) + x
	if abs(derivative(phi, a)) > 1 or abs(derivative(phi, b)) > 1:
		print("Не получилось просто вычесть икс, попробуем с лямбдой")
		der_a = derivative(f, a)
		der_b = derivative(f, b)
		print(f"f'(a)={der_a}, f'(b)={der_b}")
		lmbd = 0
		if abs(der_a) < abs(der_b):
			lmbd = - 1 / der_b
		else:
			lmbd = - 1 / der_a
		print(f'lambda={lmbd}')
		phi = lambda x: x + lmbd * f(x)
	x_prev = a
	print(f'phi(a) = {derivative(phi, a)}, phi(b) = {derivative(phi, b)}')
	if abs(derivative(phi, a)) > 1 or abs(derivative(phi, b)) > 1:
		return {"found": False, "solution": None, "iters": 0, "msg": "Метод не сходится"}
	for i in range(config.MAX_ITERATIONS):
		x = phi(x_prev)
		print(f'{i + 1}. x = {x}')
		if abs(x - x_prev) <= eps:
			if x < a or x > b:
				return {"found": False, "solution": x, "iters": i + 1, "msg": "Значение вне заданного интервала"}
			return {"found": True, "solution": x, "iters": i + 1}
		x_prev = x
	return {"found": False, "solution": x_prev, "iters": config.MAX_ITERATIONS,
			"msg": "Превышено максимальное количество итераций"}
