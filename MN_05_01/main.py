import numpy as py

def read_file_macierz(nazwa):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())
        macierz = []
        for line in odczyt:
            wiersz = [float(x) for x in line.split()]
            macierz.append(wiersz)
        return py.array(macierz), ilosc

def read_file_wektor(nazwa):
    with open(nazwa, "r") as odczyt:
        wektor = []
        for line in odczyt:
            wektor.append(float(line.strip()))
        return wektor

def utworz_macierz(ilosc):
    macierz = []
    for i in range(ilosc):
        wiersz = [float(0) for j in range(ilosc)]
        macierz.append(wiersz)
    return py.array(macierz)

def utworz_macierz_L_U(macierz_A, ilosc):
    macierz_L = utworz_macierz(ilosc)
    macierz_U = utworz_macierz(ilosc)
    for i in range(ilosc):
        for j in range(ilosc):
            if (i == j):
                macierz_L[i][j] = 1


    for i in range(ilosc):
        for j in range(ilosc):
            if i <= j :
                suma_mnoz = 0
                for k in range(0, i):
                    suma_mnoz += macierz_L[i][k]*macierz_U[k][j]
                macierz_U[i][j] = macierz_A[i][j] - suma_mnoz
            if i > j:
                suma_mnoz = 0
                for k in range(0, j):
                    suma_mnoz += macierz_L[i][k]*macierz_U[k][j]
                x = (1/macierz_U[j][j])
                y = (macierz_A[i][j] - suma_mnoz)
                macierz_L[i][j] = ((1/macierz_U[j][j])*(macierz_A[i][j] - suma_mnoz))
    return macierz_L, macierz_U

def wektor_y(macierz_L, wektor_B):
    wektor_Y = []
    wektor_Y.append(wektor_B[0])

    for i in range(1, len(wektor_B)):
        suma_mnoz = 0
        for j in range(0,i):
            suma_mnoz += macierz_L[i][j]*wektor_Y[j]
        wektor_Y.append(wektor_B[i] - suma_mnoz)
    return wektor_Y

def wektor_x(macierz_U, wektor_Y):
    wektor_X = []
    n = len(wektor_Y) - 1
    wektor_X.append(wektor_Y[n]/ macierz_U[n][n])

    i = n-1
    while i >= 0:
        suma_mnoz = 0
        k = len(wektor_X) - 1
        for j in range(i+1, len(wektor_Y)):
            suma_mnoz += macierz_U[i][j]*wektor_X[k]
            k = k -1
        x_i = ((1/macierz_U[i][i])*(wektor_Y[i] - suma_mnoz))
        wektor_X.append(x_i)
        i = i -1
    return wektor_X


def main():
    macierz_A, ilosc = read_file_macierz("A.txt")
    wektor_B = read_file_wektor("B.txt")

    print(macierz_A)
    print(wektor_B)

    macierz_L, macierz_U = utworz_macierz_L_U(macierz_A, ilosc)
    print(macierz_L)
    print(macierz_U)



    wektor_Y = wektor_y(macierz_L, wektor_B)
    print(wektor_Y)

    wektor_X = wektor_x(macierz_U, wektor_Y)
    print(wektor_X)

if __name__ == "__main__":
    main()

