import numpy as np
import matplotlib.pyplot as plt


def compare_p_values(generators: list[str], tests: list[str], p_values: list[list[str]], title: str, filename: str):
	n_generators = len(generators)
	n_tests = len(tests)

	pv = np.array(p_values)

	x = np.arange(n_tests)
	bar_width = 0.2
	m = 0

	_, ax = plt.subplots(layout="constrained")

	for i in range(n_generators):
		offset = bar_width * m
		rects = ax.bar(x + offset, pv[i,:], bar_width, label=generators[i])
		ax.bar_label(rects, padding=3, fmt="%.2f", fontsize=8)
		m += 1

	ax.set_ylabel("p-wartość")
	ax.set_title(title)
	ax.set_xticks(x + bar_width, tests)
	ax.legend(loc='upper left', ncols=3)
	ax.set_ylim(0, 1.2)

	plt.savefig(f'visualize/out/{filename}')
