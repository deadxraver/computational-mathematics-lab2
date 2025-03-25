def find_solution(x0, f, eps):
	x_prev_prev = x0
	x_prev = x_prev_prev + eps
	x = 0
	for i in range(1000):
		x = x_prev - f(x_prev) * (x_prev - x_prev_prev) / (f(x_prev) - f(x_prev_prev))
		if abs(x_prev - x) <= eps or abs(f(x)) <= eps:
			return {"found": True, "x": x, "iters": i + 1}
		x_prev_prev = x_prev
		x_prev = x
	return {"found": False, "x": x, "iters": 1000, "msg": "Слишком много итераций, вероятно не сходится"}