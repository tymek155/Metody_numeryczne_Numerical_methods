import numpy as py

def read_file(nazwa):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())
        macierz = []
        for line in odczyt:
            wiersz = [float(x) for x in line.split()]
            macierz.append(wiersz)
        return py.array(macierz), ilosc

def pivoting(macierz, kol):
    max = abs(macierz[kol][kol])
    max_ind = kol
    for i in range(kol, len(macierz)):
        if abs(macierz[i][kol])> max:
            max = abs(macierz[i][kol])
            max_ind = i

    if(max_ind != kol):
        for i in range(0, len(macierz[kol])):
            macierz[kol][i], macierz[max_ind][i] = macierz[max_ind][i], macierz[kol][i]

def postepowanie_proste(macierz, ilosc):
    for h in range(0, ilosc-1):
        pivoting(macierz, h)
        for i in range(h+1, ilosc):
            if macierz[h][h] == 0:
                print("Zero na przekatnej!")
                return macierz
            mnoznik = macierz[i][h]/macierz[h][h]
            for j in range(h, ilosc+1):
                macierz[i][j] = macierz[i][j]  - macierz[h][j]*mnoznik

    return macierz

def postepowanie_odwrotne(macierz, ilosc):
    x_n = macierz[ilosc-1][ilosc]/macierz[ilosc-1][ilosc-1]
    rozwiazania = []
    rozwiazania.append(x_n)

    i = ilosc - 2
    while i>=0:
        b_i = macierz[i][ilosc]
        a_ii = macierz[i][i]
        suma = 0
        j = ilosc - 1
        temp = ilosc - len(rozwiazania) - 1
        for x_k in rozwiazania:
            suma += macierz[temp][j]*x_k
            j = j-1
        x_i = (b_i - suma)/(a_ii)
        rozwiazania.append(x_i)
        i = i -1
    return rozwiazania


def edytuj_kolumny(macierz, wiersz, wektor_kolumny):
    max = macierz[wiersz][wektor_kolumny.index(wiersz)]
    max_ind = wektor_kolumny.index(wiersz)

    for i in range(len(macierz[wiersz])- 1):
        if abs(macierz[wiersz][i]) > max:
            max = abs(macierz[wiersz][i])
            max_ind = i

    wektor_kolumny[wektor_kolumny.index(wiersz)], wektor_kolumny[max_ind] = wektor_kolumny[max_ind], wektor_kolumny[wektor_kolumny.index(wiersz)]

def postepowanie_proste_crout(macierz, ilosc):
    wektor_kolumny = []
    for i in range(0, ilosc):
        wektor_kolumny.append(i)

    for h in range(0, ilosc-1):
        edytuj_kolumny(macierz, h, wektor_kolumny)
        for i in range(h+1, ilosc):
            if macierz[h][wektor_kolumny.index(h)] == 0:
                print("Zero na przekatnej!")
                return macierz, None
            mnoznik = macierz[i][wektor_kolumny.index(h)]/macierz[h][wektor_kolumny.index(h)]
            for j in range(0, ilosc+1):
                macierz[i][j] = macierz[i][j]  - macierz[h][j]*mnoznik

    return macierz, wektor_kolumny

def postepowanie_odwrotne_crout(macierz, ilosc, wektor_kolumny):
    x_n = macierz[ilosc-1][ilosc]/macierz[ilosc-1][wektor_kolumny.index(ilosc-1)]
    rozwiazania = []
    nr_rozw = []
    nr_rozw.append(wektor_kolumny.index(ilosc-1))
    rozwiazania.append(x_n)

    i = ilosc - 2
    while i>=0:
        b_i = macierz[i][ilosc]
        a_ii = macierz[i][wektor_kolumny.index(i)]
        suma = 0
        j = ilosc - 1
        temp = ilosc - len(rozwiazania) - 1
        for x_k in rozwiazania:
            suma += macierz[temp][wektor_kolumny.index(j)]*x_k
            j = j-1
        x_i = (b_i - suma)/(a_ii)
        rozwiazania.append(x_i)
        nr_rozw.append(wektor_kolumny.index(i))
        i = i -1
    d = 0
    return rozwiazania, nr_rozw


def main():
    macierz, ilosc = read_file("MN-4-2.txt")
    print("Macierz rozszerzona przed obliczeniami: ")
    print(macierz)
    print("Macierz rozszerzona po postepowaniu prostym: ")
    macierz, wektor_kolumny = postepowanie_proste_crout(macierz, ilosc)
    #macierz = postepowanie_proste(macierz, ilosc)
    print(macierz)
    print("Rozwiazania rownania: ")
    #rozwiazania = postepowanie_odwrotne(macierz, ilosc)
    #print(rozwiazania[::-1])
    rozwiazania, nr_rozw = postepowanie_odwrotne_crout(macierz, ilosc, wektor_kolumny)
    for i in range(len(nr_rozw)):
        print(rozwiazania[nr_rozw.index(i)], end=" ")

if __name__ == "__main__":
    main()