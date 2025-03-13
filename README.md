# Ogólne informacje 
Powyższe repozytorium jest zbiorem różnych programów (tu metod numerycznych), implementowanych w ramach 
przedmiotu Metody Numeryczne, będącego częścią kursu Inżynierii Obliczeniowej AGH.

# Główny spis treści
* [MN_02](#MN_02)
* [MN_03_1](#MN_03_1)
* [MN_04_1](#MN_04_1)
* [MN_05_01](#MN_05_01)
* [MN_06](#MN_06)
* [MN_07](#MN_07)
* [MN_08](#MN_08)
* [MN_09](#MN_09)
* [MN_10](#MN_10)
* [MN_11](#MN_11)
* [MN_12](#MN_12)
* [MN_13](#MN_13)

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
* NumPy 2.2.2
	
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
* NumPy 2.2.2
	
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
* NumPy 2.2.2
	
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
* NumPy 2.2.2
	
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
Projekt realizuje implementację 3 różnych metod całkowania funkcji jednej zmiennej w zadanym przedziale.
Zaimplementowane metody to metoda prostokątów (aporksymowanie całki przez sumowanie wartości funkcji 
w środkach przedziałów), metoda trapezów (obliczanie obszaru pod wykresem za pomocą trapezów) oraz 
metoda Simpsona (szacowanie wartości funkcji przez przybliżenie paraboliczne). Użytkownik może zadać 
przedział całkowania oraz liczbę podprzedziałów dla metod.

### Technologie
W kodzie użyto:
* Python 3.12
* math
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany w funkcjach dodano 3 wzory różnych
funkcji. Struktura kodu składa się z funkcji `metoda_prostokatow` implementującej metodę prostokątów, 
`metoda_trapezow` implementującej metodę trapezów, `metoda_simpsona` implementującej metodę parabol, 3 
wariantów testowych `sin`, `exp` oraz `fun_x`, a także standardowo funkcji `main` odpowiadającej za
interakcję z użytkownikiem, użycie odpowiednich funkcji oraz wydruk informacji wynikowych.


## MN_08

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację, tak jak projekt poprzedzający, 3 podstawowych metod całkowania oraz
dodatkowej, bardziej zaawansowanej metody - metody kwadratur Gaussa dla 2, 3 oraz 4 węzłów. 
Przeprowadzone zostały także testy skuteczności wspomnianych metod na różnych funkcjach matematycznych.

### Technologie
W kodzie użyto:
* Python 3.12
* math
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany w funkcjach dodano 3 wzory różnych
funkcji. Struktura kodu składa się z funkcji (poprzednich 3 funkcji) `metoda_prostokatow`, 
`metoda_trapezow` oraz `metoda_simpsona`, dodane zostały funkcje `kwadratura_2` implementująca 
kwadraturę Gaussa dla 2 węzłów, `kwadratura_3` implementująca kwadraturę Gaussa dla 3 węzłów, 
`kwadratura_4` implementującej kwadraturę Gaussa dla 4 węzłów, funkcji testowych oraz scalającej 
funkcji `main`.

## MN_09

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację aproksymacji wielomianowej metodą najmniejszych kwadratów. Z pliku 
tekstowego wczytywane są wymagane dane, tworozna jest macierz normalna układu równań normlanych, 
układ rozwiązywany jest metodą eliminacji Gaussa, końcowo wyznaczane są współczynniki wielomainu
aproksymującego dane.

### Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany został plik z przykładowymi dwoma
kolumnami danych (x, y) oraz z oznaczoną na wstępie ilościa wierszy danych. Struktura kodu składa się 
z funkcji `read_file` odpowiadającej za wczytanie danych z pliku, `approx` tworzącej macierz normalną 
oraz odpowiedni wektor `f` z danych wejściowych, `scal_gf` łączącej macierz i wektor w macierz 
rozszerzoną, `postepowanie_proste` przekształcającej macierz do postaci trójkątnej, 
`postepowanie_odwrotne` wyznaczającej rozwiązania układu równań, `new_y` wyliczającej nowe wartości 
wielomianu aproksymującego dla zadanych wartości x oraz głównej funkcji `main`.


## MN_10

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację aproksymacji funkcji za pomocą ortogonalnych wielomianów Grama. 
Wielomiany Grama zapewniają w tej metodzie zdecydowanie lepszą stabilność numeryczną, niż w metodach
prezentowanych wcześniej. Program podobnie jak poprzednio korzysta z danych wczytanych z pliku 
tekstowego.

### Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Do testów dodany został plik z przykładowymi dwoma
kolumnami danych (x, y) oraz z oznaczoną na wstępie ilościa wierszy danych. Struktura kodu składa się 
z funkcji `read_file` odpowiadającej za wczytanie danych z pliku, `silnia` obliczającej współczynnik 
dwumianowy, `wartosc_wielomianu` obliczającej wartość wskazanego iloczynu w ortogonalnych wielomianach
Grama, `funkcja_f` obliczającej wartość wielomianu Grama dla zadanego stopnia, liczby punktów oraz 
odpowiedniego współczynnika, `gram` implementującej interpolację z użyciem wielomianów Grama, a także 
funkcji `main` gdzie zachodzi ogólna logika kodu oraz interakcja z użytkownikiem.


## MN_11

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację 3 podstawowych metod numerycznych rozwiązujących równania różniczkowe I 
rzędu - metodę Eulera, metodę Rungeo-Kutty II rzędu oraz metodę Rungego-Kutty IV rzędu.

### Technologie
W kodzie użyto:
* Python 3.12
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się z funkcji `fun`, `fun_2` 
definiujących wzory funkcji różniczkowych, `euler` implementującej metodę Eulera bazującą na przybliżeniu 
stycznej do wykresu funkcji, `rk2` realizującej metodę Rungego-Kutty II rzędu, gdzie wykorzystywana jest 
średnia z dwóch przybliżeń wartości funkcji, `rk4` implementującej metodę Rungego_Kutty IV rzędu (o 
wysokiej dokładności) oraz `main` odpowiadajćej za ogólną logike i organizację programu.


## MN_12

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację metod stycznych oraz siecznych (Newtona oraz ilorazu różnicowego), 
służących do znajdowania miejsc zerowych funkcji.

### Technologie
W kodzie użyto:
* Python 3.12
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się z funkcji `fun`
i `fun2`, których miejsca zerowe będą poszukiwane, `funp` oraz `funp2` - pochodnych wcześniej 
wspomnianych funkcji, `metoda_stycznych` gdzie przybliżenie miejsca zerowego obliczane jest zgodnie 
z zadanym dla tej metody wzorem, aż do osiągnięcia maksymalnej ilości iteracji, `metoda_siecznych`, 
która właściwie jest wariantem poprzedniej funkcji, wykorzystujemy tu jednak przybliżenie ilorazu 
różnicowego, `iloraz_roznicowy` obliczającej przybliżenie pochodnej w metodzie siecznych oraz 
głównej funkcji `main` gdzie dla obu funkcji testowych przeprowadzane są obliczenia, w każdej iteracji 
mamy informację o aktualnym położeniu punktu i wartości funkcji.


## MN_13

### Spis treści
* [Ogólne informacje](#ogólne-informacje)
* [Technologie](#technologie)
* [Wykorzystanie](#wykorzystanie)

### Ogólne informacje
Projekt realizuje implementację kolejnych metod służących do znajdowania miejsc zerowych funkcji, 
w tym przypadku metody bisekcji oraz metody fal linii (reguła falsi).

### Technologie
W kodzie użyto:
* Python 3.12
* math
	
### Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się z funkcji `fun1`, 
której pierwiastki są poszukiwane w programie, `alg_bisekcji`, która implementuję algorytm poszukiwania 
miejsca zerowego w zadanym przedziale (przedział jest w kazdej iteracji na pół i wybierany jest ten 
przedział, dla którego funkcja zmienia znak - funkcja na końcach przedziału musi zmieniać znak), 
`metoda_fal_linii`, która implementuje regułę falsi, gdzie miesjce zerowe jest poszukiwane poprzez 
wyznaczenie przecięcia linii łączącej punkty na wykresie funkcji (tutaj również musi zachodzic zmiana 
znaku między końcami przedziałów) oraz `main` odpowiadającej za ogólną logikę i organizację kodu.





























 








