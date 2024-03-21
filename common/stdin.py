import fileinput


def input_test() -> list[list[int]]:
	result = []
	current_list = []
	
	for line in fileinput.input('-'):
		if line.strip() == "":
			result.append(current_list)
			current_list = []
			continue

		n = int(line)
		current_list.append(n)

	return result


def input_p_values() -> list[float]:
	result = []

	for line in fileinput.input('-'):
		p = float(line)
		result.append(p)

	return result
