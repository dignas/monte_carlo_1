import numpy as np
from scipy.stats import norm
import math


def frequency_monobit(data: list[int]) -> float:
	n = len(data)
	X = np.array(data)
	sn = np.sum(2 * X - 1) / math.sqrt(n)
	p_value = 2 * (1 - norm.cdf(abs(sn)))
	return p_value
