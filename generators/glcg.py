from generators.generic.generator import generate_list
from generators.generic.glcg import glcg
from common.stdout import output_test


if __name__ == "__main__":
	M = 2**10
	ai = [3, 7, 68]
	xi = [88, 89, 121]

	generator = glcg(M, ai, xi)
	test = generate_list(generator)
	output_test(test)
