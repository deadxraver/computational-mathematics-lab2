def parse(json):
	if json["found"]:
		return f"Ответ: {json['solution']}\nКоличество итераций: {json['iters']}"
	else:
		return f"{json['msg']}\nПоследнее приближение: {json['solution']}\nКоличество итераций: {json['iters']}"
