from collections.abc import Generator


# Middle-Square Weyl Sequence generator
# In general, it generates a pseudo-random number from {0, 1, ..., 2^32 - 1}
# Here, it takes an additional parameter m and returns a pseudo-random number from {0, ..., m - 1} - simply x mod m, therefore m should be a divisor of 2^32.
# The original generator is described in https://arxiv.org/pdf/1704.00358.pdf

def msws(m: int) -> Generator[int, None, None]:
	x0 = 0
	w = 0
	M = 2**64
	s = 0xb5ad4eceda1ce2a9
	while True:
		x0 = (x0 * x0) % M
		w = (w + s) % M
		x0 = (x0 + w) % M
		x0 = ((x0 >> 32) | (x0 << 32)) % M
		yield x0 % m
