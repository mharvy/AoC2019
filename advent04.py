
def check_valid(input):
	if input >= 1000000 or input < 100000:
		return False

	two_adjacent = False
	prev_digit = 10
	count_adjacent = 1

	while input > 0:
		cur_num = input % 10
		if cur_num == prev_digit:
			count_adjacent += 1
		else:
			if count_adjacent == 2:
				two_adjacent = True
			count_adjacent = 1
		if cur_num > prev_digit:
			return False
		prev_digit = cur_num
		input = input // 10
	if count_adjacent == 2:
		two_adjacent = True

	return two_adjacent


def count_possible(lower, higher):  # lower bound, higher bound
	answer = 0

	cur_pass = lower
	while cur_pass <= higher:
		if check_valid(cur_pass):
			answer += 1
		cur_pass += 1

	return answer


print(check_valid(112233))
print(check_valid(123444))
print(check_valid(111122))
print(check_valid(111112))
print(check_valid(123456))
print(check_valid(123356))
print(check_valid(123354))
print(check_valid(112345))
print(check_valid(223456))
print(count_possible(178416, 676461))
