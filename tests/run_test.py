from tests.level_test.first_level_test import first_level_test
from tests.level_test.second_level_test import second_level_test
from tests.level_test.birthday_spacing import birthday_spacing_test_l1, birthday_spacing_test_l2

from tests.generic.chi_squared import chi_squared
from tests.generic.frequency_monobit import frequency_monobit
from tests.generic.poker_test import poker_test
from tests.generic.cumsum import cumsum_test

from common.stdin import input_test
from common.stdout import output_list

import argparse
from enum import Enum


class AvailableTests(Enum):
	CHI2 = "chi2"
	FREQUENCY_MONOBIT = "frequency_monobit"
	POKER = "poker"
	BIRTHDAY_SPACING = "birthday_spacing"
	CUMSUM = "cumsum"


def parse_args(available_tests: list[str]) -> tuple[int, str, int]:
	parser = argparse.ArgumentParser(description="Monte Carlo project 2023 -- statistical testing")

	parser.add_argument("-l", required=True, choices=[1, 2], type=int, help="Choose level of testing")
	parser.add_argument("--test", required=True, choices=available_tests, type=str, help="Choose a test")
	parser.add_argument("-m", required=True, type=int, help="Indicates that the generator returned numbers in range {0, 1, ..., M-1}. Choose 2 for monobit generators.")

	args = parser.parse_args()
	return args.l, args.test, args.m


if __name__ == "__main__":
	l, test, m = parse_args([test.value for test in AvailableTests])

	if l == 1:
		level_testing = first_level_test
	else:
		level_testing = second_level_test

	if test == AvailableTests.CHI2.value:
		k = 16 if m > 16 else 2
		statistical_test = lambda data, M=m, K=k: chi_squared(M, K, data)
	elif test == AvailableTests.FREQUENCY_MONOBIT.value:
		statistical_test = frequency_monobit
	elif test == AvailableTests.POKER.value:
		statistical_test = lambda data, M=m: poker_test(M, data)
	elif test == AvailableTests.BIRTHDAY_SPACING.value:
		if l == 1:
			level_testing = lambda data, _, M=m: birthday_spacing_test_l1(M, data)
		else:
			level_testing = lambda data, _, M=m: birthday_spacing_test_l2(M, data)
		statistical_test = None
	elif test == AvailableTests.CUMSUM.value:
		statistical_test = lambda data, M=m: cumsum_test(M, data)

	data = input_test()
	p_values = level_testing(data, statistical_test)

	output_list(p_values)
