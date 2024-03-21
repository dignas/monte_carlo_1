from typing import Callable


def first_level_test(test: list[list[int]], statistical_test: Callable[[list[int]], float]) -> list[float]:
	return [statistical_test(data) for data in test]
