import numpy as np
from scipy.stats import chi2
from typing import Callable


# Assuming k equal-sized categories
def chi_squared(M: float, k: int, data: list[int]) -> float:
	s = M / k										# category size
	X = np.array(data)
	C = np.floor(X / s)								# category assignment
	Y, _ = np.histogram(C, bins=k, range=(0, k))	# number of elements in each category
	nps = len(data) / k								# expected number of observations in each category (under H_0 assumption)

	chi_squared_statistic = np.sum(np.square(Y - nps) / nps)

	p_value = 1 - chi2.cdf(chi_squared_statistic, k - 1)
	return p_value


# Arbitrary categories with probabilities p(i) and category assignment by function f
def chi_squared_general(p: Callable[[int], float], f: Callable[[int], int], bins: list[int], data: list[int]) -> float:
	X = np.array(data)
	C = [f(x) for x in X]						# category assignment
	Y, _ = np.histogram(C, bins=bins)
	ps = np.array([p(i) for i in bins[:-1]])	# probabilities of bins
	nps = len(data) * ps						# expected number of observations in each bin

	chi_squared_statistic = np.sum(np.square(Y - nps) / nps)

	p_value = 1 - chi2.cdf(chi_squared_statistic, len(bins) - 2)
	return p_value
