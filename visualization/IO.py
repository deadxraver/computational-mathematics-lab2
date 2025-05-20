class IO:
	def __init__(self, filename):
		if filename is None:
			self.file = None
		else:
			self.file = open(filename)

	def read(self, prompt='', err='', cast_type=str, additional_cond=lambda x: True):
		if self.file is None:
			while 1:
				try:
					ret = cast_type(input(prompt))
					if not additional_cond(ret):
						raise ValueError
					return ret
				except ValueError:
					print(err)
		else:
			try:
				ret = cast_type(self.file.readline().strip())
				if not additional_cond(ret):
					raise ValueError
			except ValueError:
				print(err)
				exit(-1)
