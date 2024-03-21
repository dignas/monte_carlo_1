from tests.generic.chi_squared import chi_squared
from tests.level_test.first_level_test import first_level_test

from typing import Callable


def second_level_test(test: list[list[int]], statistical_test: Callable[[list[int]], float]) -> list[float]:
	p_values = first_level_test(test, statistical_test)

	M = 1
	k = 10
	second_lev_p_value = chi_squared(M, k, p_values)
	return [second_lev_p_value]
