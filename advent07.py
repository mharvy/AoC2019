
import itertools as it

class Computer(object):
	def __init__(self, program, phase):
		self.program = program
		self.eip = 0
		self.phase = phase
		self.phase_done = False

	def get_params(self):
		params = []

		cur_instruction = self.program[self.eip] % 100

		param_count = 0
		if cur_instruction in [1, 2, 7, 8]:
			param_count = 3
		elif cur_instruction in [5, 6]:
			param_count = 2
		elif cur_instruction in [3, 4]:
			param_count = 1

		modes = self.program[self.eip] // 100

		cur_idx = 1
		while cur_idx <= param_count:
			if modes % 10 == 1:
				params.append(self.program[self.eip + cur_idx])
			else:
				params.append(self.program[self.program[self.eip + cur_idx]])
			cur_idx += 1
			modes = modes // 10

		return params

	def __call__(self, in_signal):

		# run opcodes
		while (self.program[self.eip] != 99):

			# Get instruction
			instruction = self.program[self.eip] % 100
			modes = self.program[self.eip] // 100

			# Get parameters
			params = self.get_params()

			# Addition
			if instruction == 1:
				self.program[self.program[self.eip + 3]] = params[0] + params[1]
				self.eip += 4

			# Multiplication
			elif instruction == 2:
				self.program[self.program[self.eip + 3]] = params[0] * params[1]
				self.eip += 4

			# input
			elif instruction == 3:
				if not self.phase_done:
					self.program[self.program[self.eip + 1]] = self.phase
					self.phase_done = True
				else:
					self.program[self.program[self.eip + 1]] = in_signal
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
					self.program[self.program[self.eip + 3]] = 1
				else:
					self.program[self.program[self.eip + 3]] = 0
				self.eip += 4

			# Equals
			elif instruction == 8:
				if params[0] == params[1]:
					self.program[self.program[self.eip + 3]] = 1
				else:
					self.program[self.program[self.eip + 3]] = 0
				self.eip += 4

			else:
				return -1, True

		return -1, True

# Part 2 
def permutations(program):
	answer = [-1 * float("inf"), None]
	for phases in list(it.permutations([5, 6, 7, 8, 9])):
		amps = []
		for phase in phases:
			amps.append(Computer(program.copy(), phase))

		cur_signal = 0
		cur_answer = 0 

		idx = 0
		done = False 
		while not done:
			#print(idx, cur_signal)
			cur_signal, done = amps[idx](cur_signal)

			if idx == 4:
				cur_answer = cur_signal

			idx = (idx + 1) % 5

		if answer[0] < cur_answer:
			answer = [cur_answer, phases]

	return answer



program = [3,8,1001,8,10,8,105,1,0,0,21,34,51,64,73,98,179,260,341,422,99999,3,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,1001,9,4,9,1002,9,3,9,1001,9,5,9,4,9,99,3,9,101,5,9,9,102,5,9,9,4,9,99,3,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,1001,9,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
test1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
test2 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
test3 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,9]

print(permutations(program))

