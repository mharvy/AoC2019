
import math

# Part 1
def find_best_astroid(layout):
	positions = set()

	# Put all positions in a dict 
	for row in range(len(layout)):
		for c in range(len(layout[row])):
			if layout[row][c] == '#':
				positions.add((c, row))

	# Double iterate over all positions, counting
	# number of seen astroids
	cur_best = ((0, 0), -1)  # pos, number of seen astroids
	for pos1 in positions:
		count = 0
		angles = set()  # x / y
		cardinals = [False, False, False, False]
		for pos2 in positions:
			if pos2 == pos1:
				count += 0
			elif pos1[0] - pos2[0] != 0 and pos1[1] - pos2[1] != 0:
				if (((pos1[0] - pos2[0]) / (pos1[1] - pos2[1])), (pos1[1] - pos2[1]) / abs((pos1[1] - pos2[1]))) not in angles:
					count += 1
					angles.add((((pos1[0] - pos2[0]) / (pos1[1] - pos2[1])), (pos1[1] - pos2[1]) / abs((pos1[1] - pos2[1]))))
			elif pos1[0] == pos2[0]:
				if pos1[1] > pos2[1]:
					if not cardinals[0]:
						count += 1
						cardinals[0] = True
				else:
					if not cardinals[1]:
						count += 1
						cardinals[1] = True
			elif pos1[1] == pos2[1]:
				if pos1[0] > pos2[0]:
					if not cardinals[2]:
						count += 1
						cardinals[2] = True
				else:
					if not cardinals[3]:
						count += 1
						cardinals[3] = True

		if count > cur_best[1]:
			cur_best = (pos1, count)

	return cur_best[0], cur_best[1]


# Part 2
def nth_vaporized(layout, pos1):
	positions = set()

	# Put all positions in a dict 
	for row in range(len(layout)):
		for c in range(len(layout[row])):
			if layout[row][c] == '#':
				positions.add((c, row))

	result = []

	while len(result) < 200:
		angles = set()  # x / y
		cardinals = [False, False, False, False]
		for pos2 in positions:
			if pos2 == pos1:
				# do nothing
				continue
			elif pos1[0] - pos2[0] != 0 and pos1[1] - pos2[1] != 0:
				if (((pos1[0] - pos2[0]) / (pos1[1] - pos2[1])), (pos1[1] - pos2[1]) / abs((pos1[1] - pos2[1]))) not in angles:
					
					result.append((math.degrees(math.atan((pos1[1] - pos2[1]) / (pos1[0] - pos2[0]))) + 90 + 180 * ((((pos1[0] - pos2[0]) / abs((pos1[0] - pos2[0]))) + 1) / 2), pos2))
					
					angles.add((((pos1[0] - pos2[0]) / (pos1[1] - pos2[1])), (pos1[1] - pos2[1]) / abs((pos1[1] - pos2[1]))))
			elif pos1[0] == pos2[0]:
				if pos1[1] > pos2[1]:
					if not cardinals[0]:
						result.append((0, pos2))
						cardinals[0] = True
				else:
					if not cardinals[1]:
						result.append((180, pos2))
						cardinals[1] = True
			elif pos1[1] == pos2[1]:
				if pos1[0] > pos2[0]:
					if not cardinals[2]:
						result.append((270, pos2))
						cardinals[2] = True
				else:
					if not cardinals[3]:
						result.append((90, pos2))
						cardinals[3] = True

		for pos2 in result:
			if pos2 in positions:
				positions.remove(pos2)

	result.sort()
	while result[0][0] < 0:
		result.append(result.pop(0))
	#print(result)
	print(len(result))
	print(result[199])
	return result[200]


test1 = ["......#.#.",
"#..#.#....",
"..#######.",
".#.#.###..",
".#..#.....",
"..#....#.#",
"#..#....#.",
".##.#..###",
"##...#..#.",
".#....####"]

test2 = ["#.#...#.#.",
".###....#.",
".#....#...",
"##.#.#.#.#",
"....#.#.#.",
".##..###.#",
"..#...##..",
"..##....##",
"......#...",
".####.###."]

test3 = [".#..##.###...#######",
"##.############..##.",
".#.######.########.#",
".###.#######.####.#.",
"#####.##.#.##.###.##",
"..#####..#.#########",
"####################",
"#.####....###.#.#.##",
"##.#################",
"#####.##.###..####..",
"..######..##.#######",
"####.##.####...##..#",
".#####..#.######.###",
"##...#.##########...",
"#.##########.#######",
".####.#.###.###.#.##",
"....##.##.###..#####",
".#.#.###########.###",
"#.#.#.#####.####.###",
"###.##.####.##.#..##"]

my_input = [".###.###.###.#####.#",
"#####.##.###..###..#",
".#...####.###.######",
"######.###.####.####",
"#####..###..########",
"#.##.###########.#.#",
"##.###.######..#.#.#",
".#.##.###.#.####.###",
"##..#.#.##.#########",
"###.#######.###..##.",
"###.###.##.##..####.",
".##.####.##########.",
"#######.##.###.#####",
"#####.##..####.#####",
"##.#.#####.##.#.#..#",
"###########.#######.",
"#.##..#####.#####..#",
"#####..#####.###.###",
"####.#.############.",
"####.#.#.##########."]

print(nth_vaporized(test3, (11,13)))
print(nth_vaporized(my_input, (8,16)))
