from generators.generic.generator import generate_list_different_seeds
from generators.generic.rc4 import rc4
from common.stdout import output_test

from typing import Callable
from collections.abc import Generator


# For each sequence taken for second level testing we take a different key. They will have a fixed length, and their bit representation will be
# consecutive numbers 0, 1, 2, ..., R - 1, where R is the number of performed tests.


def build_get_seed(m: int) -> Callable[[int], list[int]]:
	def get_seed(i: int) -> list[int]:
		k0 = i % m
		i //= m
		k1 = i % m
		i //= m
		k2 = i % m
		return [k2, k1, k0]
	return get_seed


def build_generator_with_seed(m: int) -> Callable[[list[int]], Generator[int]]:
	def generator_with_seed(l: list[int]) -> Generator[int]:
		return rc4(m, l)
	return generator_with_seed



if __name__ == "__main__":
	m = 32

	generator_with_seed = build_generator_with_seed(m)
	get_seed = build_get_seed(m)
	test = generate_list_different_seeds(generator_with_seed, get_seed)
	output_test(test)
