from common.stdin import input_p_values

import matplotlib.pyplot as plt
from numpy import linspace
import argparse


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--title', required=True, type=str, help='histogram title')
	parser.add_argument('--file', required=True, type=str, help='output file name')
	args = parser.parse_args()

	p_values = input_p_values()

	_, ax = plt.subplots()
	ax.set_xlabel("p-wartość")

	bins = linspace(0, 1, 101)
	ax.hist(p_values, bins=bins)
	ax.set_title(args.title)

	plt.savefig(f'visualize/out/{args.file}')
