import numpy as np
from scipy.stats import chi2


# Poker test. Data length should be divisible by 5. Otherwise, spare values at the end will be ignored.
def poker_test(m: int, data: list[int]) -> float:
	X = np.array(data)
	n = len(X)
	if n % 5 != 0:
		n -= (n % 5)
		X = X[:n]
	fives = X.reshape((-1, 5))

	r = np.apply_along_axis(lambda v: len(np.unique(v)), 1, fives)
	pr = np.array([__count_pr(m, r) for r in range(1, 6)])
	npr = (n / 5) * pr

	Y, _ = np.histogram(r, bins=[1, 2, 3, 4, 5, 6])
	chi_squared_statistic = np.sum(np.square(Y - npr) / npr)

	p_value = 1 - chi2.cdf(chi_squared_statistic, 4)
	return p_value


def __count_pr(m, r) -> float:
	prod = 1
	for i in range(1, r + 1):
		prod *= (m - i + 1)

	return prod / m**5 * __stirling_number(r)


# Stirling numbers of second kind for 5-tuples of elements
def __stirling_number(r: int) -> int:
	res = [1, 15, 25, 10, 1]
	return res[r - 1]
