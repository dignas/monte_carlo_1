from numpy import array, append, delete
from collections.abc import Generator


def glcg(M: int, ai: list[int], xi: list[int]) -> Generator[int, None, None]:
	ai_arr = array(ai)
	xi_arr = array(xi)
	while True:
		new_x = ai_arr.dot(xi_arr) % M
		xi_arr = append(xi_arr, new_x)[1:]
		# xi_arr = delete(xi_arr, 0)
		yield new_x
