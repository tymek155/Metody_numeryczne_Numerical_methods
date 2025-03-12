import numpy as py

def read_file(nazwa):
    with open(nazwa, "r") as plik:
        linie = plik.readlines()

    ilosc = int(linie[0])
    wektor_b = []
    macierz = []

    for linia in linie[1:]:
        wiersz = list(map(float, linia.split()))
        wektor_b.append(wiersz.pop())
        macierz.append(wiersz)

    #wektor_b = [wiersz[-1] for wiersz in macierz]
    return ilosc, py.array(macierz), wektor_b

def spr_diagonalnosc(macierz, ilosc):
    warunek_ostry = False
    for i in range(ilosc):
        suma = 0
        warunek_slaby = False
        for j in range(ilosc):
            if i != j:
                suma += abs(macierz[i][j])
        if abs(macierz[i][i]) >= suma:
            warunek_slaby = True
            if abs(macierz[i][i]) > suma:
                warunek_ostry = True
        if warunek_slaby == False:
            print("Macierz nie jest diagonalnie slabo dominująca!")
            return False
    if warunek_ostry == True:
        print("Macierz diagonalnie slabo dominujaca!")
        return True
    else:
        print("Macierz nie jest diagonalnie slabo dominująca!")
        return False

def stworz_macierz(ilosc):
    macierz = []
    for i in range(ilosc):
        wiersz = [0.0 for i in range(ilosc)]
        macierz.append(wiersz)
    return py.array(macierz)

def stworz_wektor(ilosc):
    wektor = []
    for i in range(ilosc):
        wektor.append(0.0)
    return wektor

def rozklad_LDU(macierz, ilosc):
    macierz_LU = stworz_macierz(ilosc)
    macierz_D = stworz_macierz(ilosc)

    for i in range(ilosc):
        for j in range(ilosc):
            if i > j:
                macierz_LU[i][j] = macierz[i][j]
            elif i == j:
                macierz_D[i][j] = macierz[i][j]
            else:
                macierz_LU[i][j] = macierz[i][j]

    return macierz_LU, macierz_D

def zmniejsz_macierz(macierz, w, k, rozmiar):
    nowa_macierz = []
    for i in range(rozmiar):
        wiersz = []
        for j in range(rozmiar):
            if i != w and j != k:
                wiersz.append(macierz[i][j])
        if wiersz:
            nowa_macierz.append(wiersz)
    return py.array(nowa_macierz)

def oblicz_wyznacznik(macierz, ilosc):
    if ilosc == 1:
        return macierz[0][0]
    if ilosc == 2:
        return macierz[0][0]*macierz[1][1] - macierz[1][0]*macierz[0][1]
    wyznacznik = 0
    for i in range(ilosc):
        wyznacznik += ((-1)**i)*macierz[0][i]*oblicz_wyznacznik(zmniejsz_macierz(macierz,0, i, ilosc), ilosc-1)
    return wyznacznik

def oblicz_doplenienie(macierz, ilosc, w, k):
    if ilosc == 2:
        for i in range(ilosc):
            for j in range(ilosc):
                if i != w and j != k:
                    return ((-1) ** (i + j))*macierz[i][j]
    else:
        doplenienie = 0
        doplenienie += ((-1)**(w+k))*oblicz_wyznacznik(zmniejsz_macierz(macierz,w, k, ilosc), ilosc-1)
        return doplenienie


def macierz_odwrotna(macierz, ilosc):
    wyznacznik = oblicz_wyznacznik(macierz, ilosc)
    if wyznacznik != 0:
        macierz_odwd = stworz_macierz(ilosc)
        for i in range(ilosc):
            for j in range(ilosc):
                macierz_odwd[i][j] = oblicz_doplenienie(macierz, ilosc, i, j)
        #macierz_tr = stworz_macierz(ilosc)
        for i in range(ilosc):
            for j in range(ilosc):
                macierz_odwd[i][j] = macierz_odwd[i][j]/wyznacznik
        return py.array(macierz_odwd)

def pomnoz_macierz_wektor(M, b, ilosc):
    wektor = stworz_wektor(ilosc)
    for i in range(ilosc):
        for j in range(ilosc):
            wektor[i] += b[j]*M[i][j]
    return wektor

def suma_wektorow(wek1,wek2, ilosc):
    for i in range(ilosc):
        wek1[i] = wek1[i] + wek2[i]
    return wek1

def macierz_liczba(macierz,liczba,ilosc):
    for i in range(ilosc):
        for j in range(ilosc):
            macierz[i][j] = macierz[i][j]*liczba
    return macierz

def mnoz_macierze(macierz1, macierz2, ilosc):
    ret_mac = stworz_macierz(ilosc)
    for i in range(ilosc):
        for j in range(ilosc):
            for k in range(ilosc):
                ret_mac[i][j] += macierz1[i][k]*macierz2[k][j]
    return ret_mac

def rozwiazania(ilosc, macierz_LU, macierz_odw, wektor_b, wektor_x, iter):
    wektor_2 = pomnoz_macierz_wektor(macierz_odw, wektor_b, ilosc)
    macierz_minus = macierz_liczba(macierz_odw, -1, ilosc)
    macierz_mnoz = mnoz_macierze(macierz_minus, macierz_LU, ilosc)

    for i in range(iter):
        wektor_x = pomnoz_macierz_wektor(macierz_mnoz, wektor_x, ilosc)
        wektor_x = suma_wektorow(wektor_x, wektor_2, ilosc)
    return wektor_x

def spr_wart(kopia, wektor, warunek):
    iter = 0
    for i in range(len(wektor)):
        if abs(wektor[i] - kopia[i]) <= warunek:
            iter += 1
    if iter == len(wektor):
        return True
    else:
        return False

def rozwiazanie_2(ilosc, macierz_LU, macierz_odw, wektor_b, wektor_x, iter_max, warunek):
    wektor_2 = pomnoz_macierz_wektor(macierz_odw, wektor_b, ilosc)
    macierz_minus = macierz_liczba(macierz_odw, -1, ilosc)
    macierz_mnoz = mnoz_macierze(macierz_minus, macierz_LU, ilosc)
    roz = 1.0
    iter = 0
    while True:
        kopia_wek = wektor_x.copy()
        wektor_x = pomnoz_macierz_wektor(macierz_mnoz, wektor_x, ilosc)
        wektor_x = suma_wektorow(wektor_x, wektor_2, ilosc)
        iter += 1
        if spr_wart(kopia_wek, wektor_x, warunek):
            break
    print(iter)
    return wektor_x

def main():
    ilosc, macierz, wektor_b = read_file("Dane.txt")
    if spr_diagonalnosc(macierz, ilosc):
        macierz_LU, macierz_D = rozklad_LDU(macierz, ilosc)
        print(macierz)
        print(macierz_LU)
        print(wektor_b)
        print(macierz_D)
        macierz_odw = macierz_odwrotna(macierz_D, ilosc)
        print(macierz_odw)
        wektor_x = stworz_wektor(ilosc)
        rozw = rozwiazania(ilosc, macierz_LU, macierz_odw, wektor_b, wektor_x, 5)
        #rozw = rozwiazanie_2(ilosc, macierz_LU, macierz_odw, wektor_b, wektor_x, 200, 0.000001)
        print(rozw)
        x= 0



if __name__ == '__main__':
    main()