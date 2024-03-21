#!/bin/bash

export PYTHONPATH="`pwd`"

INT_GENERATORS=("lcg" "glcg" "msws" "python" "rc4_32_i" "rc4_32_ii")
INT_MS=("1024" "1024" "1024" "1024" "32" "32")
INT_TESTS=("chi2" "poker" "cumsum" birthday_spacing)
INT_NO=${#INT_GENERATORS[@]}

BIT_GENERATORS=("pi" "e" "sqrt2")
BIT_MS=("2" "2" "2")
BIT_TESTS=("frequency_monobit" "cumsum")
BIT_NO=${#BIT_GENERATORS[@]}

generate_data() {
	GENERATOR=$1
	N=$2
	T=$3

	python3.12 generators/$GENERATOR.py -n $N -t $T >out.txt
}

test_data() {
	TEST=$1
	M=$2
	L=$3

	P_VALUE="`python3.12 tests/run_test.py --test $TEST -m $M -l $L <out.txt`"
	echo "p-value: $P_VALUE"
}

run_level_test() {
	GENERATOR=$1
	M=$2
	TEST=$3
	LEVEL=$4

	if [[ "$TEST" == "birthday_spacing" ]]; then

		if [[ $M -eq 32 ]]; then
			N=2560
		elif [[ $M -eq 1024 ]]; then
			N=1280
		fi

		if [[ $LEVEL -eq 1 ]]; then
			T=1
		else
			T=1000
		fi


	elif [[ $LEVEL -eq 2 ]]; then
		N=1000
		T=1000
	elif [[ $LEVEL -eq 1 ]]; then
		N=100000
		T=1
	fi

	echo "Level $LEVEL test $TEST for $GENERATOR"

	generate_data $GENERATOR $N $T
	test_data $TEST $M $LEVEL

}

generate_histograms() {

	python3.12 generators/lcg.py -n 1000 -t 1000 >out.txt
	python3.12 tests/run_test.py -m 1024 -l 1 --test chi2 <out.txt >p_vals.txt
	python3.12 visualize/generate_histograms.py --title "p-wartości dla LCG na teście χ²" --file hist_lcg_chi2.png <p_vals.txt

	python3.12 generators/python.py -n 1000 -t 1000 >out.txt
	python3.12 tests/run_test.py -m 1024 -l 1 --test chi2 <out.txt >p_vals.txt
	python3.12 visualize/generate_histograms.py --title "p-wartości dla generatora Python na teście χ²" --file hist_python_chi2.png <p_vals.txt

	python3.12 generators/msws.py -n 1000 -t 1000 >out.txt
	python3.12 tests/run_test.py -m 1024 -l 1 --test poker <out.txt >p_vals.txt
	python3.12 visualize/generate_histograms.py --title "p-wartości dla generatora MSWS na teście pokerowym" --file hist_msws_poker.png <p_vals.txt

	python3.12 generators/python.py -n 1000 -t 1000 >out.txt
	python3.12 tests/run_test.py -m 1024 -l 1 --test poker <out.txt >p_vals.txt
	python3.12 visualize/generate_histograms.py --title "p-wartości dla generatora Python na teście pokerowym" --file hist_python_poker.png <p_vals.txt

}

for LEVEL in $(seq 1 2); do

	echo "Running level $LEVEL tests..."

	for I in $(seq 0 $(( $INT_NO - 1 ))); do

		GENERATOR=${INT_GENERATORS[$I]}
		M=${INT_MS[$I]}

		for TEST in "${INT_TESTS[@]}"; do

			run_level_test $GENERATOR $M $TEST $LEVEL

		done

	done

	for I in $(seq 0 $(( $BIT_NO - 1 ))); do

		GENERATOR=${BIT_GENERATORS[$I]}
		M=${BIT_MS[$I]}

		for TEST in "${BIT_TESTS[@]}"; do

			run_level_test $GENERATOR $M $TEST $LEVEL

		done

	done

done


echo "Generating plots..."
python3.12 visualize/generate_plots.py

echo "Generating histograms..."
generate_histograms
