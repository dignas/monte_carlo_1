from collections.abc import Generator
import random
import math


def python(M: int) -> Generator[int, None, None]:
	while True:
		yield math.floor(random.random() * M)
