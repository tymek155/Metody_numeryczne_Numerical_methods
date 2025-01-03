import numpy as py

def read_file(nazwa):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())
        macierz = []
        for line in odczyt:
            wiersz = [float(x) for x in line.split()]
            macierz.append(wiersz)
        return py.array(macierz), ilosc

def postepowanie_proste(macierz, ilosc):
    for h in range(0, ilosc-1):
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


def main():
    macierz, ilosc = read_file("RURL_2.txt")
    print("Macierz rozszerzona przed obliczeniami: ")
    print(macierz)
    print("Macierz rozszerzona po postepowaniu prostym: ")
    macierz = postepowanie_proste(macierz, ilosc)
    print(macierz)
    print("Rozwiazania rownania: ")
    rozwiazania = postepowanie_odwrotne(macierz, ilosc)
    print(rozwiazania[::-1])

if __name__ == "__main__":
    main()