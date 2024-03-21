from generators.generic.generator import generate_list
from generators.generic.msws import msws
from common.stdout import output_test


if __name__ == "__main__":
	m = 2**10

	generator = msws(m)
	test = generate_list(generator)
	output_test(test)
