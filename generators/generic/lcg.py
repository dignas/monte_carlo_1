from collections.abc import Generator


def lcg(M: int, a: int, c: int, x0: int) -> Generator[int, None, None]:
	while True:
		x0 = (a * x0 + c) % M
		yield x0
