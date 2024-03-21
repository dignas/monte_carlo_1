from generators.generic.generator import generate_list
from generators.generic.python import python
from common.stdout import output_test


if __name__ == "__main__":
	M = 2**10

	generator = python(M)
	test = generate_list(generator)
	output_test(test)
