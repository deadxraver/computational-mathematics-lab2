import config


def find_solution(a, b, f, eps) -> dict[str, bool | float | int | str | None]:
	if f(a) * f(b) > 0:
		return {"found": False, "solution": None, "iters": 0,
				"msg": "Функция имеет одинаковые знаки на границах, вероятно имеет четное количество корней на отрезке, или не имеет их вовсе, нельзя применить данный метод"}
	for i in range(config.MAX_ITERATIONS):
		x = (a + b) / 2
		if abs(a - b) <= eps or abs(f(x)) <= eps:
			if x < a or x > b:
				return {"found": False, "solution": x, "iters": i + 1, "msg": "Значение вне заданного интервала"}
			return {"found": True, "solution": x, "iters": i + 1}
		if f(a) * f(x) < 0:
			b = x
		else:
			a = x
	return {"found": False, "solution": [(a + b) / 2], "iters": config.MAX_ITERATIONS,
			"msg": "Превышен предел итераций"}
