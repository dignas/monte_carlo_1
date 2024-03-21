from tests.generic.chi_squared import chi_squared_general
from tests.generic.convert import from_bit_string, to_bit_string

import numpy as np
import math


__desired_m_exp = 25


def birthday_spacing_test_l1(m: int, data: list[list[int]]) -> [float]:
	return [__birthday_spacing_test_l1_one_list(m, d) for d in data]


def birthday_spacing_test_l2(m: int, data: list[list[int]]) -> [float]:
	K_obs = [__number_equal_spacing(m, __convert_data(m, d)) for d in data]

	def p(i):
		if i == 0:
			return 0.368801
		elif  i == 1:
			return 0.369035
		elif i == 2:
			return 0.183471
		elif i == 3:
			return 0.078692
		else:
			return 0
		
	def f(i):
		return min(i, 3)
	
	return [chi_squared_general(p, f, [0, 1, 2, 3, 4], K_obs)]


def __birthday_spacing_test_l1_one_list(m: int, data: list[int]) -> float:
	data = __convert_data(m, data)
	K_obs = __number_equal_spacing(m, data)
	n = len(data)
	M = 2**__desired_m_exp
	lamb = n**3 / (4 * M)

	eps = 1e-6
	p_value = 1
	for j in range(K_obs):
		p_value -= math.exp(-lamb) * (lamb**j / math.factorial(j))
		if p_value < eps:	# This condition was added because for some generators the number of collisions is large and the value j factorial would overflow.
			break			# Exact value doesn't matter for the purpose of testing. If it's less than 1e-6, we can assume it's almost 0.

	return p_value


def __number_equal_spacing(m: int, data: list[int]) -> int:
	n = len(data)
	Y = np.sort(data)
	S = np.diff(Y)
	S = np.append(S, [Y[1] - Y[n - 1] + m])
	S_sorted = np.sort(S)
	
	last_spacing = -1
	K = 0
	for s in S_sorted:
		if s != last_spacing:
			last_spacing = s
		else:
			K += 1

	return K


# Ideally, we want the converted data to be a list of 2**9 integers, each from range [0, 1, ..., 2**25 - 1], which is 12,800 bits in total
# Implemented integer generators give us 5 or 10 bit numbers.
# For a 5-bit generator, we need 2560 numbers per test and for 10-bit generator 1280 numbers per test.
def __convert_data(m: int, data: list[int]) -> list[int]:
	bit_string = to_bit_string(m, data)
	return from_bit_string(__desired_m_exp, bit_string)
