from collections.abc import Generator
import urllib.request
from numpy import array


def digit_generator(url: str) -> Generator[int, None, None]:
	digits = _read_digits(url)
	dl = len(digits)
	x0 = 0
	while True:
		yield digits[x0]
		x0 = x0 + 1 if x0 + 1 < dl else 0


def _read_digits(url):

	data = []
	with urllib.request.urlopen(url) as f:
		for line in f:
			data.append(line.strip())
	datastring = []


	for line in data:
		datastring.append(line.decode("utf-8"))

	datastring = ''.join(datastring)
	datastring = list(map(int, list(datastring)))

	return(array(datastring))
