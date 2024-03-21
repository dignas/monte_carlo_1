from tests.generic.convert import to_bit_string

import numpy as np
from scipy.stats import norm
import math


def cumsum_test(m: int, data: list[int]) -> float:
	bit_string = to_bit_string(m, data)
	n = len(bit_string)
	transformed_bits = np.array([2 * int(b) - 1 for b in bit_string])
	S = np.cumsum(transformed_bits)
	z = np.amax(np.abs(S))

	k_end = math.floor((n/z - 1) / 4)
	k_start_1 = math.ceil((-n/z + 1) / 4)
	k_start_2 = math.ceil((-n/z - 3) / 4)

	p_value = 1
	sq_n = math.sqrt(n)
	
	for k in range(k_start_1, k_end+1):
		p_value -= (norm.cdf((4*k + 1) * z / sq_n) - norm.cdf((4*k - 1) * z / sq_n))

	for k in range(k_start_2, k_end+1):
		p_value += (norm.cdf((4*k + 3) * z / sq_n) - norm.cdf((4*k + 1) * z / sq_n))

	return p_value
