# Ogólne informacje 

# Główny spis treści
* [MN_02](#MN_02)
* [MN_03_1](#MN_03_1)
* [MN_04_1](#MN_04_1)
* [MN_05_01](#MN_05_01)
* [MN_06](#MN_06)
* [MN_07](#MN_07)

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

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację mteody eliminacji Gaussa, służącą do rozwiązywania liniowych układów równań,
odczytywnaych z pliku tekstowego. Idea porgramu skupia się na przekształceniu macierzy w macierz trójkątną górną,
potem wykorzystywane jest podstawianie wstecz, aby uzyskać szukane wartości niewiadome. W wyniku otrzmujemy listę
współczynników, które są rozwiązaniami zadanego układu równań.

### Technologie
W kodzie użyto:
* Python 3.12
* NumPY 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Dla możliwości przetestowania programu dodane zostały dwa 
pliki tekstowe z przykładowymi macierzami (układami) oraz ich wymiarami na początku pliku. Struktura kodu składa się 
z funkcji `read_file`, która odpowiada za wczytywanie macierzy rozszerzonej układu z pliku, `postepowanie_proste`, 
która implementuje eliminację Gaussa - przekształca macierz do postaci trójkątnej, `postepowanie_odwrotne`, która 
poprzez podstawianie wstecz wyznacza niewiadome oraz `main`, gdzie następuje użycie wszystkich funkcji składowych i 
otrzymujemy wydrukowany wynik.


## MN_04_1

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje rozbudowaną implementację projektu poprzedniego, mamy w tym przypadku do czynienia z roszerzoną 
metodą eliminacji Gaussa, która uwzględnia wybór elementu głównego - pivoting - oraz 
eliminację Crouta. Program, tak jak poprzednio, rozwiązuje układy równań liniowych na 
podstawie pliku tekstowego.

### Technologie
W kodzie użyto:
* Python 3.12
* NumPY 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodane zostały 3 pliki 
tesktowe z przykładowymi macierzami (układami) oraz ich wymiarami na początku pliku. 
Struktura kodu składa się z funkcji `read_file`, wczytującej macierz rozszerzoną układu równań z pliku, 
`pivoting` implementującej wybór częściowy elementu głównego w eliminacji Gaussa,
`postepowanie_proste` standardowo realizującej eliminację Gaussa,
`postepowanie_odwrotne` generującej rozwiązania układu poprzez podstawianie, 
`edytuj_kolumny` implementującej dynamiczną zamianę kolumn Coruta,
`postepowanie_proste_crout` realizującej eliminację Gaussa z dynamiczną zamianą kolumn, 
`postepowanie_odwrotne_crout` generującej roziwązania układu równań z uwzględnieniem 
zamiany kolumn oraz `main`, która odpowiada za ogólną logikę pogramu, odpowiednie użycie 
zaprojektowanych funkcji oraz generowanie wydruków dla użytkownika.


## MN_05_01

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację metody LU do rozwiązywania układów równań liniowych za pomocą
dekompozycji macierzy współczynników na iloczyn macierzy dolnej, trójkątnej L oraz górnej, 
trójkątnej U. Program działa kolejno poprzez wczytanie danych z plików tekstowych, dokonanie 
dekompozycji LU oraz rozwiązanie układu równań przez rozwiązanie dwóch układów trójkątnych.

### Technologie
W kodzie użyto:
* Python 3.12
* NumPY 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodane zostały 2 pliki z 
macierzą A (macierz współczynników) oraz wektorem B (wektro wyrazów wolnych). Struktura kodu
składa się z funkcji `read_file_macierz` wczytującej macierz A z pliku, `read_file_wektor` 
wczytującej wektor B z pliku, `utworz_macierz` tworzącej macierz zerową, `utworz_macierz_L_U`
 dokonującej dekompozycji LU macierzy A, `wektor_y` rozwiązującej układ postaci L*Y=B, 
`wektor_x` rozwiązującej układ U*X=Y oraz `main` zarządzającej ogólnym przepływem programu 
oraz wydrukiem uzyskanych wyników.

## MN_06

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację metody LDU do rozwiązywania układów równań liniowych za pomocą
dekompozycji macierzy współczynników na iloczyn macierzy dolnej, trójkątnej L, górnej, 
trójkątnej U oraz diagonalnej D. Program działa kolejno poprzez wczytanie danych z pliku tekstowego (w 
tym macierzy współczynników A oraz wektora wyrazów wolnych B), sprawdzenie czy macierz jest diagonalnie
dominująca, dekompozycję macierzy A na składowe L, D oraz U, obliczenie macierzy diagonalnej D, 
iteracyjne rozwiązanie układu równań liniowych rpzez iterację prostą, dodatkowo jest także dodana druga
wersja algorytmu generująca iteracje, aż do osiągnięcia zadanego błędu tolerancji.


### Technologie
W kodzie użyto:
* Python 3.12
* NumPY 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany został plik z 
macierzą rozszerzoną układu równań, wraz z wymiarem macierzy A (ilość szukanych zmiennych). Struktura kodu
składa się z funkcji `read_file_macierz` wczytującej dane z pliku, `spr_diagonalnosc` sprawdzającej 
spełnienie warunku diagonalności, `rozklad_LDU` dokonującej dekompozycji macierzy na macierze L, D oraz U,
`macierz_odwrotna` obliczającej macierz odwrotną macierzy diagonalnej D, `pomnoz_macierz_wektorz` mnożącej
 macierz przez wektor, `mnoz_macierze` wykonującej iloczyn macierzy, `rozwiazania` rozwiązującej układ 
równań iteracyjnie dla ustalonej liczby iteracji, `rozwiazanie_2` rozwiązującej układ iteracyjnie, aż do 
osiągnięcia zadanego warunku stopu oraz `main` zarządzającej ogólną logiką programu i wydrukiem 
podstawowych informacji.


## MN_07

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację metody LDU do rozwiązywania układów równań liniowych za pomocą
dekompozycji macierzy współczynników na iloczyn macierzy dolnej, trójkątnej L, górnej, 
trójkątnej U oraz diagonalnej D. Program działa kolejno poprzez wczytanie danych z pliku tekstowego (w 
tym macierzy współczynników A oraz wektora wyrazów wolnych B), sprawdzenie czy macierz jest diagonalnie
dominująca, dekompozycję macierzy A na składowe L, D oraz U, obliczenie macierzy diagonalnej D, 
iteracyjne rozwiązanie układu równań liniowych rpzez iterację prostą, dodatkowo jest także dodana druga
wersja algorytmu generująca iteracje, aż do osiągnięcia zadanego błędu tolerancji.


### Technologie
W kodzie użyto:
* Python 3.12
* NumPY 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany został plik z 
macierzą rozszerzoną układu równań, wraz z wymiarem macierzy A (ilość szukanych zmiennych). Struktura kodu
składa się z funkcji `read_file_macierz` wczytującej dane z pliku, `spr_diagonalnosc` sprawdzającej 
spełnienie warunku diagonalności, `rozklad_LDU` dokonującej dekompozycji macierzy na macierze L, D oraz U,
`macierz_odwrotna` obliczającej macierz odwrotną macierzy diagonalnej D, `pomnoz_macierz_wektorz` mnożącej
 macierz przez wektor, `mnoz_macierze` wykonującej iloczyn macierzy, `rozwiazania` rozwiązującej układ 
równań iteracyjnie dla ustalonej liczby iteracji, `rozwiazanie_2` rozwiązującej układ iteracyjnie, aż do 
osiągnięcia zadanego warunku stopu oraz `main` zarządzającej ogólną logiką programu i wydrukiem 
podstawowych informacji.



 








