import config


def derivative(f, x0):
	return (f(x0 + config.dx()) - f(x0)) / config.dx()


def find_solution(a, b, f, eps):
	der_a = derivative(f, a)
	der_b = derivative(f, b)
	lmbd = 0
	if abs(der_a) < abs(der_b):
		lmbd = - 1 / der_b
	else:
		lmbd = - 1 / der_a
	x_prev = a
	phi = lambda x: x + lmbd * f(x)
	if abs(derivative(phi, a)) > 1 or abs(derivative(phi, b)) > 1:
		return {"found": False, "x": None, "iters": 0, "msg": "Метод не сходится"}
	for i in range(config.MAX_ITERATIONS):
		x = phi(x_prev)
		if abs(x - x_prev) <= eps:
			return {"found": True, "x": x, "iters": i + 1}
		x_prev = x
	return {"found": False, "x": x_prev, "iters": config.MAX_ITERATIONS, "msg": "Превышено максимальное количество итераций"}
