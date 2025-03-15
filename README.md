Go to [English version](#english-version)
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

# English version

# General Information
The above repository is a collection of various programs (here numerical methods), implemented as part of the Numerical Methods course, which is part of the Computational Engineering program at AGH University.

# Main Table of Contents
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

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements a simple Newton interpolation for any text data created according to a template, loaded 
from a text file. The user provides a point at which they want to calculate the value of the function defined by 
the interpolation nodes in the text file. As a result, the user receives the value of the function at the point 
and the calculated divided difference coefficient.

### Technologies
The code uses:
* Python 3.12

### Usage
The code was run and written in the PyCharm environment. To fully test the code, two text files with different 
numbers of interpolation nodes and different values were added. The code structure consists of a `read_file` 
function that loads the text file into appropriate data structures, the main computational function 
`interpolacja_newtona`, where the Newton polynomial is constructed, and the `main` function responsible for user 
interaction and basic console messages.

## MN_03_1

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements the Gaussian elimination method for solving systems of linear equations read from a text 
file. The idea of the program focuses on transforming the matrix into an upper triangular matrix, then using back 
substitution to obtain the desired unknown values. As a result, we get a list of coefficients that are the 
solutions to the given system of equations.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. To test the program, two text files with example 
matrices (systems) and their dimensions at the beginning of the file were added. The code structure consists of 
the `read_file` function, which is responsible for loading the augmented matrix of the system from the file, 
`postepowanie_proste`, which implements Gaussian elimination - transforming the matrix into a triangular form, 
`postepowanie_odwrotne`, which determines the unknowns through back substitution, and `main`, where all component 
functions are used, and the result is printed.

## MN_04_1

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements an extended version of the previous project, where we deal with an extended Gaussian 
elimination method that includes pivot selection - pivoting - and Crout elimination. The program, as before, 
solves systems of linear equations based on a text file.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. For testing, three text files with example matrices 
(systems) and their dimensions at the beginning of the file were added. The code structure consists of the 
`read_file` function, which loads the augmented matrix of the system of equations from the file, `pivoting`, 
which implements partial pivot selection in Gaussian elimination, `postepowanie_proste`, which standardly 
performs Gaussian elimination, `postepowanie_odwrotne`, which generates solutions to the system through 
substitution, `edytuj_kolumny`, which implements dynamic column swapping in Crout's method, 
`postepowanie_proste_crout`, which performs Gaussian elimination with dynamic column swapping, 
`postepowanie_odwrotne_crout`, which generates solutions to the system of equations considering column swapping, 
and `main`, which is responsible for the overall logic of the program, the appropriate use of the designed 
functions, and generating printouts for the user.

## MN_05_01

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements the LU decomposition method for solving systems of linear equations by decomposing the 
coefficient matrix into the product of a lower triangular matrix L and an upper triangular matrix U. The program 
works by first loading data from text files, performing LU decomposition, and then solving the system of 
equations by solving two triangular systems.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. For testing, two files were added: one with matrix A 
(the coefficient matrix) and the other with vector B (the vector of free terms). The code structure consists of 
the `read_file_macierz` function, which loads matrix A from the file, `read_file_wektor`, which loads vector B 
from the file, `utworz_macierz`, which creates a zero matrix, `utworz_macierz_L_U`, which performs LU 
decomposition of matrix A, `wektor_y`, which solves the system L*Y=B, `wektor_x`, which solves the system U*X=Y, 
and `main`, which manages the overall program flow and prints the obtained results.

## MN_06

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements the LDU decomposition method for solving systems of linear equations by decomposing the 
coefficient matrix into the product of a lower triangular matrix L, an upper triangular matrix U, and a diagonal 
matrix D. The program works by first loading data from a text file (including the coefficient matrix A and the 
vector of free terms B), checking if the matrix is diagonally dominant, decomposing matrix A into L, D, and U 
components, calculating the diagonal matrix D, and iteratively solving the system of linear equations through 
simple iteration. Additionally, a second version of the algorithm is added, which generates iterations until a 
given error tolerance is reached.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. For testing, a file with the augmented matrix of the 
system of equations was added, along with the dimension of matrix A (the number of unknowns). The code structure 
consists of the `read_file_macierz` function, which loads data from the file, `spr_diagonalnosc`, which checks 
the diagonal dominance condition, `rozklad_LDU`, which decomposes the matrix into L, D, and U matrices, 
`macierz_odwrotna`, which calculates the inverse of the diagonal matrix D, `pomnoz_macierz_wektorz`, which 
multiplies a matrix by a vector, `mnoz_macierze`, which performs matrix multiplication, `rozwiazania`, which 
solves the system iteratively for a fixed number of iterations, `rozwiazanie_2`, which solves the system 
iteratively until a given stopping condition is met, and `main`, which manages the overall program logic and 
prints basic information.

## MN_07

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements three different methods of integrating a function of one variable over a given interval. 
The implemented methods are the rectangle method (approximating the integral by summing the function values at 
the midpoints of the intervals), the trapezoidal method (calculating the area under the graph using trapezoids), 
and Simpson's method (estimating the function value by parabolic approximation). The user can specify the 
integration interval and the number of subintervals for the methods.

### Technologies
The code uses:
* Python 3.12
* math

### Usage
The code was run and written in the PyCharm environment. For testing, three different function formulas were 
added to the functions. The code structure consists of the `metoda_prostokatow` function, which implements the 
rectangle method, `metoda_trapezow`, which implements the trapezoidal method, `metoda_simpsona`, which implements 
the parabolic method, three test variants `sin`, `exp`, and `fun_x`, and the standard `main` function, which is 
responsible for user interaction, the use of appropriate functions, and printing the resulting information.

## MN_08

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements, like the previous project, three basic integration methods and an additional, more 
advanced method - the Gaussian quadrature method for 2, 3, and 4 nodes. Tests of the effectiveness of these 
methods on various mathematical functions were also conducted.

### Technologies
The code uses:
* Python 3.12
* math

### Usage
The code was run and written in the PyCharm environment. For testing, three different function formulas were 
added to the functions. The code structure consists of the (previous three functions) `metoda_prostokatow`, 
`metoda_trapezow`, and `metoda_simpsona`, added functions `kwadratura_2`, which implements Gaussian quadrature 
for 2 nodes, `kwadratura_3`, which implements Gaussian quadrature for 3 nodes, `kwadratura_4`, which implements 
Gaussian quadrature for 4 nodes, test functions, and the main `main` function.

## MN_09

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements polynomial approximation using the least squares method. The required data is loaded from 
a text file, the normal matrix of the normal equations system is created, the system is solved using Gaussian 
elimination, and finally, the coefficients of the approximating polynomial are determined.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. For testing, a file with example two columns of data (x, 
y) and the number of data rows marked at the beginning was added. The code structure consists of the `read_file` 
function, which is responsible for loading data from the file, `approx`, which creates the normal matrix and the 
corresponding vector `f` from the input data, `scal_gf`, which combines the matrix and vector into an augmented 
matrix, `postepowanie_proste`, which transforms the matrix into a triangular form, `postepowanie_odwrotne`, which 
determines the solutions to the system of equations, `new_y`, which calculates new values of the approximating 
polynomial for given x values, and the main `main` function.

## MN_10

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements function approximation using orthogonal Gram polynomials. Gram polynomials provide 
significantly better numerical stability in this method than in the methods presented earlier. The program, as 
before, uses data loaded from a text file.

### Technologies
The code uses:
* Python 3.12
* NumPy 2.2.2

### Usage
The code was run and written in the PyCharm environment. For testing, a file with example two columns of data (x, 
y) and the number of data rows marked at the beginning was added. The code structure consists of the `read_file` 
function, which is responsible for loading data from the file, `silnia`, which calculates the binomial 
coefficient, `wartosc_wielomianu`, which calculates the value of the specified product in orthogonal Gram 
polynomials, `funkcja_f`, which calculates the value of the Gram polynomial for a given degree, number of points, 
and the corresponding coefficient, `gram`, which implements interpolation using Gram polynomials, and the `main` 
function, where the general logic of the code and user interaction takes place.

## MN_11

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements three basic numerical methods for solving first-order differential equations - the Euler 
method, the second-order Runge-Kutta method, and the fourth-order Runge-Kutta method.

### Technologies
The code uses:
* Python 3.12

### Usage
The code was run and written in the PyCharm environment. The code structure consists of the `fun`, `fun_2` 
functions defining the formulas of differential functions, `euler`, which implements the Euler method based on 
the approximation of the tangent to the function graph, `rk2`, which implements the second-order Runge-Kutta 
method, where the average of two approximations of the function value is used, `rk4`, which implements the fourth-
order Runge-Kutta method (with high accuracy), and `main`, which is responsible for the general logic and 
organization of the program.

## MN_12

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements tangent and secant methods (Newton's method and the difference quotient) for finding the 
roots of functions.

### Technologies
The code uses:
* Python 3.12

### Usage
The code was run and written in the PyCharm environment. The code structure consists of the `fun` and `fun2` 
functions, whose roots are being sought, `funp` and `funp2` - the derivatives of the previously mentioned 
functions, `metoda_stycznych`, where the approximation of the root is calculated according to the formula for 
this method until the maximum number of iterations is reached, `metoda_siecznych`, which is essentially a variant 
of the previous function, but here we use the approximation of the difference quotient, `iloraz_roznicowy`, which 
calculates the approximation of the derivative in the secant method, and the main `main` function, where 
calculations are performed for both test functions, and in each iteration, we have information about the current 
position of the point and the value of the function.

## MN_13

### Table of Contents
* [General Information](#general-information)
* [Technologies](#technologies)
* [Usage](#usage)

### General Information
The project implements additional methods for finding the roots of functions, in this case, the bisection method 
and the false position method (regula falsi).

### Technologies
The code uses:
* Python 3.12
* math

### Usage
The code was run and written in the PyCharm environment. The code structure consists of the `fun1` function, 
whose roots are being sought in the program, `alg_bisekcji`, which implements the algorithm for finding the root 
in a given interval (the interval is halved in each iteration, and the interval where the function changes sign 
is selected - the function must change sign at the ends of the interval), `metoda_fal_linii`, which implements 
the false position method, where the root is sought by determining the intersection of the line connecting points 
on the function graph (here also the sign must change between the ends of the interval), and `main`, which is 
responsible for the general logic and organization of the code.





