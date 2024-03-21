import math
from numpy import reshape


def to_bit_string(m: int, data: list[int]) -> str:
	lg = math.ceil(math.log(m, 2))
	bit_string = ''.join([bin(x)[2:].zfill(lg) for x in data])
	return bit_string


def from_bit_string(word: int, data: str) -> list[int]:
	leftover = len(data) % word
	used_bits = list(data)
	if leftover > 0:
		used_bits = used_bits[:-leftover]
	new_bit_repr = reshape(used_bits, (-1, 25))
	return [int(''.join(s), 2) for s in new_bit_repr]
