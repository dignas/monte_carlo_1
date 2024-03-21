from generators.generic.generator import generate_list
from generators.generic.rc4 import rc4
from common.stdout import output_test


# We will use one fixed-length key (seed) and for second level testing will take consecutive sequences.

if __name__ == "__main__":
	m = 32

	generator = rc4(m, [13, 2, 4])
	test = generate_list(generator)
	output_test(test)
