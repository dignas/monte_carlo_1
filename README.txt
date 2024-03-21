Skrypt, który uruchamia wszystkie kody, oblicza p-wartości i generuje wykresy można uruchomić w systemie Linux poleceniem "bash run_all.sh".
Żeby wszystkie kody poprawnie się importowały, ścieżka robocza powinna być w głównym katalogu tej paczki, czyli w tym samym, w którym znajduje się plik README.txt.
Kod używa Pythona w wersji 3.12 (nowa składnia type parameters).

Wykresy w formacie .png zostaną zapisane w folderze visualize/out.

W pliku doc/result.txt znajdują się obliczone wcześniej wyniki. Ziarna wszystkich generatorów są ustalone w kodzie, zatem oczekiwane są te same deterministyczne rezultaty.


---- ENG -----

Run 'bash run_all.sh' in the terminal to run all tests, compute p-values and generate plots.
Working directory should be in the root of this repository. Python 3.12 required.

Png plots are saved to visualize/out.

File doc/result.txt contains the expected output (seeds are predefined so it should not change). 
File doc/papers.txt contains links to papers the project is based on.
