from collections.abc import Generator


def rc4(m: int, k: list[int]) -> Generator[int, None, None]:
	S = __init_rc4(m, k)
	i, j = 0, 0
	while True:
		i = i + 1 if i + 1 < m else 0
		j = (j + S[i]) % m
		S[i], S[j] = S[j], S[i]
		t = (S[i] + S[j]) % m
		yield S[t]


def __init_rc4(m: int, k: list[int]) -> list[int]:
	S = list(range(m))
	L = len(k)

	j = 0
	for i in range(m):
		j = (j + S[i] + k[i % L]) % m
		S[i], S[j] = S[j], S[i]

	return S
