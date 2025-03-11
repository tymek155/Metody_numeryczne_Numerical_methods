# Ogólne informacje 

# Główny spis treści
* [MN_02](#MN_02)
* [MN_03_1](#MN_03_1)

## MN_02

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje prostą implementację interpolacji Newtona dla dowolnych, utworzonych według szablonu, danych tekstowych, wczytanych 
z pliku tektstowego. Użytkownik podaje punkt, w którym chciałby obliczyć wartość funkcji określonej za pomocą wezłów interpolacji w pliku tekstowym,
wynikowo otrzymuje wartość funkcji w punkcie oraz obliczony współczynnik różnicowy.

### Technologie
W kodzie użyto:
* Python 3.12
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Dla możliwości pełnego przetestowania kodu dodane zostały dwa pliki tekstowe z różną
ilością węzłów interpolacji oraz  z innymi wartościami. Struktura kodu składa się z funkcji wczytującej plik tekstowy `read_file` do odpowiednich
struktur danych, głównej funkcji obliczeniowej `interpolacja_newtona`, gdzie konstruowany jest wielomian Newtona oraz funkcji `main` odpowiadającej za warstwę
interakcji z użytkownikiem oraz podstawowe komunikaty w konsoli.



## MN_03_1
