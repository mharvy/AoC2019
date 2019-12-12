import math


# Part 1
def calculate_energy(pos, steps):

	step = 0

	# Calculate final position and velocity
	vel = [[0,0,0] for i in range(len(pos))]
	while step < steps:

		to_change = [[0,0,0] for i in range(len(pos))]
		for p1 in range(len(pos)):

			for p2 in range(len(pos)):
				if pos[p1][0] != pos[p2][0]: vel[p1][0] += (int(pos[p1][0] < pos[p2][0]) * 2 - 1)
				if pos[p1][1] != pos[p2][1]: vel[p1][1] += (int(pos[p1][1] < pos[p2][1]) * 2 - 1)
				if pos[p1][2] != pos[p2][2]: vel[p1][2] += (int(pos[p1][2] < pos[p2][2]) * 2 - 1)

		for p in range(len(pos)):
			pos[p][0] += vel[p][0]
			pos[p][1] += vel[p][1]
			pos[p][2] += vel[p][2]

		step += 1

	# Calculate total energy
	energy = 0
	for p in range(len(pos)):
		pot = abs(pos[p][0]) + abs(pos[p][1]) + abs(pos[p][2])
		kin = abs(vel[p][0]) + abs(vel[p][1]) + abs(vel[p][2])
		energy += pot * kin

	return energy


# Part 2 
def find_repeat(pos):
	found = [{}, {}, {}]
	bases = [-1, -1, -1]
	spaces = [0, 0, 0]
	step = 0

	vel = [[0,0,0] for i in range(len(pos))]
	while bases[0] == -1 or bases[1] == -1 or bases[2] == -1:
		search = [[p[0] for p in pos] + [v[0] for v in vel], [p[1] for p in pos] + [v[1] for v in vel], [p[2] for p in pos] + [v[2] for v in vel]]
		if tuple(search[0]) in found[0] and bases[0] == -1:
			bases[0] = found[0][tuple(search[0])]
			spaces[0] = step - found[0][tuple(search[0])]
			print(0, step)
		if tuple(search[1]) in found[1] and bases[1] == -1:
			bases[1] = found[1][tuple(search[1])]
			spaces[1] = step - found[1][tuple(search[1])]
			print(1, step)
		if tuple(search[2]) in found[2] and bases[2] == -1:
			bases[2] = found[2][tuple(search[2])]
			spaces[2] = step - found[2][tuple(search[2])]
			print(2, step)

		found[0][tuple(search[0])] = step
		found[1][tuple(search[1])] = step
		found[2][tuple(search[2])] = step

		to_change = [[0,0,0] for i in range(len(pos))]
		for p1 in range(len(pos)):

			for p2 in range(len(pos)):
				if pos[p1][0] != pos[p2][0]: vel[p1][0] += (int(pos[p1][0] < pos[p2][0]) * 2 - 1)
				if pos[p1][1] != pos[p2][1]: vel[p1][1] += (int(pos[p1][1] < pos[p2][1]) * 2 - 1)
				if pos[p1][2] != pos[p2][2]: vel[p1][2] += (int(pos[p1][2] < pos[p2][2]) * 2 - 1)

		for p in range(len(pos)):
			pos[p][0] += vel[p][0]
			pos[p][1] += vel[p][1]
			pos[p][2] += vel[p][2]

		step += 1

	temp = spaces[0] * spaces[1] // math.gcd(spaces[0], spaces[1])
	return temp * spaces[2] // math.gcd(temp, spaces[2])



test1 = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
my_input = [[-4, -9, -3], [-13, -11, 0], [-17, -7, 15], [-16, 4, 2]]
#print(calculate_energy(test1, 10))
#print(calculate_energy(my_input, 1000))
print(find_repeat(test1))
print(find_repeat(my_input))

