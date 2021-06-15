# SW_compare
Program do porównywania wyników swojego programu z prawidłowymi wynikami

Wywoływanie programu jest identyczne jak projektu, w terminalu stostujemy komendę:

python3 compare.py <our_results_dir> <results_OK_dir>

Np.

python3 comapre.py results/results.txt results/results_OK.txt

Wynikiem jest informacja w terminalu o:
1. Prawidłowych wynikach na zdjęciu, 
2. Wskazaniu, która wartość i o ile różni się od prawidłowej, 
3. Skuteczność wskazania na zdjęciu oraz % błędu, 
4. Całkowitą liczbę błędów i skuteczność
5. Zestawienie skuteczności odczytu poszczególnych żelków w skali danego typu i wszystkich błędów
