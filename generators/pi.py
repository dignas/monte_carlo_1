from generators.generic.generator import generate_list
from generators.generic.digit_generator import digit_generator
from common.stdout import output_test


if __name__ == "__main__":
	url = "http://www.math.uni.wroc.pl/~rolski/Zajecia/data.pi"

	generator = digit_generator(url)
	test = generate_list(generator)
	output_test(test)
