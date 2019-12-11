
class Computer(object):
	def __init__(self, program):
		self.program = program
		self.eip = 0
		self.base = 0
		self.memory = {}

	def get_params(self):
		params = []
		source = 0

		cur_instruction = self.program[self.eip] % 100

		param_count = 0
		if cur_instruction in [1, 2, 7, 8]:
			param_count = 3
		elif cur_instruction in [5, 6]:
			param_count = 2
		elif cur_instruction in [3, 4, 9]:
			param_count = 1

		modes = self.program[self.eip] // 100

		cur_idx = 1
		while cur_idx <= param_count:
			if cur_idx == param_count:
				if modes % 10 == 2:
					source = self.base + self.program[self.eip + param_count]

				elif modes % 10 == 1:
					source = self.eip + param_count

				else:
					source = self.program[self.eip + param_count]


			if modes % 10 == 2:
				if self.base + self.program[self.eip + cur_idx] < len(self.program):
					params.append(self.program[self.base + self.program[self.eip + cur_idx]])
				else:
					if (self.base + self.program[self.eip + cur_idx]) in self.memory:
						params.append(self.memory[self.base + self.program[self.eip + cur_idx]])
					else:
						params.append(0)
			elif modes % 10 == 1:
				if self.eip + cur_idx < len(self.program):
					params.append(self.program[self.eip + cur_idx])
				else:
					if (self.eip + cur_idx) in self.memory:
						params.append(self.memory[self.eip + cur_idx])
					else:
						params.append(0)
			else:
				if self.program[self.eip + cur_idx] < len(self.program):
					params.append(self.program[self.program[self.eip + cur_idx]])
				else:
					if (self.program[self.eip + cur_idx]) in self.memory:
						params.append(self.memory[self.program[self.eip + cur_idx]])
					else:
						params.append(0)
			cur_idx += 1
			modes = modes // 10

		return params, source

	def __call__(self, in_signal):

		# run opcodes
		while (self.program[self.eip] != 99):

			# Get instruction
			instruction = self.program[self.eip] % 100
			modes = self.program[self.eip] // 100

			# Get parameters
			params, source = self.get_params()

			# Addition
			if instruction == 1:
				if source < len(self.program):
					self.program[source] = params[0] + params[1]
				else:
					self.memory[source] = params[0] + params[1]
				self.eip += 4

			# Multiplication
			elif instruction == 2:
				if source < len(self.program):
					self.program[source] = params[0] * params[1]
				else:
					self.memory[source] = params[0] * params[1]
				self.eip += 4

			# input
			elif instruction == 3:
				if source < len(self.program):
					self.program[source] = in_signal
				else:
					self.memory[source] = in_signal
				self.eip += 2

			# Output
			elif instruction == 4:
				out = params[0]
				self.eip += 2
				return out, False

			# Jump if true
			elif instruction == 5:
				if params[0]:
					self.eip = params[1]
				else:
					self.eip += 3

			# Jump if False
			elif instruction == 6:
				if not params[0]:
					self.eip = params[1]
				else:
					self.eip += 3

			# Less than
			elif instruction == 7:
				if params[0] < params[1]:
					if source < len(self.program):
						self.program[source] = 1
					else:
						self.memory[source] = 1
				else:
					if source < len(self.program):
						self.program[source] = 0
					else:
						self.memory[source] = 0
				self.eip += 4

			# Equals
			elif instruction == 8:
				if params[0] == params[1]:
					if source < len(self.program):
						self.program[source] = 1
					else:
						self.memory[source] = 1
				else:
					if source < len(self.program):
						self.program[source] = 0
					else:
						self.memory[source] = 0
				self.eip += 4

			# Relative base change
			elif instruction == 9:
				self.base += params[0]
				self.eip += 2

			else:
				return -1, True

		return -1, True
