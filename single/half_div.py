import config


def find_solution(a, b, f, eps) -> dict[str, bool | float | int | str | None]:
	if f(a) * f(b) > 0:
		return {"found": False, "solution": None, "iters": 0, "msg": "Функция имеет одинаковые знаки на границах, имеет четное количество корней на отрезке"}
	for i in range(config.MAX_ITERATIONS):
		x = (a + b) / 2
		if abs(a - b) <= eps or abs(f(x)) <= eps:
			return {"found": True, "solution": x, "iters": i + 1}
		if f(a) * f(x) < 0:
			b = x
		else:
			a = x
	return {"found": False, "solution": (a + b) / 2, "iters": config.MAX_ITERATIONS, "msg": "Превышен предел итераций"}