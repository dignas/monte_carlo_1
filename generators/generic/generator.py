import argparse
from collections.abc import Generator
from typing import Callable, Any


def generate_list(generator: Generator[int]) -> list[list[int]]:
	n, t = __get_n_t()
	return [[next(generator) for i in range(n)] for j in range(t)]


def generate_list_different_seeds[T](generator_with_seed: Callable[[T], Generator[int]], get_seed: Callable[[int], T]) -> list[list[int]]:
	n, t = __get_n_t()
	result = []
	for i in range(t):
		generator = generator_with_seed(get_seed(i))
		result.append([next(generator) for _ in range(n)])
	return result


def __get_n_t() -> tuple[int, int]:
	default_n = 100
	default_t = 1

	parser = argparse.ArgumentParser(description="Monte Carlo project 2023 -- PRNG")
	parser.add_argument('-n', default=default_n, required=False, type=int, help='number of generated pseudo-random numbers (default: %(default)s)')
	parser.add_argument('-t', default=default_t, required=False, type=int, help='number of performed tests (useful for second-level testing) (default: %(default)s)')

	args = parser.parse_args()
	return args.n, args.t
