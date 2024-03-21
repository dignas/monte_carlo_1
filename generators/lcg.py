from generators.generic.generator import generate_list
from generators.generic.lcg import lcg
from common.stdout import output_test


if __name__ == "__main__":
	M = 2**10
	a = 3
	c = 7
	x0 = 621

	generator = lcg(M, a, c, x0)
	test = generate_list(generator)
	output_test(test)
