import numpy as py

def read_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()

        points = int(lines[0].strip())
        x = []
        y = []

        for line in lines[1:points + 1]:
            x1, y1 = map(int, line.split())
            x.append(x1)
            y.append(y1)
    return points, x, y

def approx(amount, x, y, stp, w):
    f = py.zeros(stp+1)
    g = py.zeros((stp+1, stp+1))

    for i in range(stp+1):
        for j in range(stp+1):
            sum1 = 0
            for k in range(amount):
                sum1 += (x[k]**i)*(x[k]**j)*w[k]
            g[i,j] = sum1

    for i in range(stp+1):
        sum2 = 0
        for k in range(amount):
            sum2 += (x[k]**i)*y[k]*w[k]
        f[i] = sum2

    return f,g

def scal_gf(g,f):
    col_f = py.reshape(f,(-1,1))
    mat_ext = py.hstack((g,col_f))
    return mat_ext

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

def new_y(a, x):
    new_y = []
    for i in range(len(x)):
        sum1 = 0
        for j in range(len(a)):
            sum1 += a[j]*(x[i]**j)
        new_y.append(sum1)
    return new_y

def main():
    points, x, y = read_file("MN_09.txt")
    print("Liczba węzłów aproksymacji: ", points)
    stp = 1
    w = [1.0 for i in range(len(x))]
    f,g = approx(points, x, y, stp, w)
    macierz = scal_gf(g, f)
    ilosc = stp +1
    print("Macierz rozszerzona przed obliczeniami: ")
    print(macierz)
    print("Macierz rozszerzona po postepowaniu prostym: ")
    macierz = postepowanie_proste(macierz, ilosc)
    print(macierz)
    print("Rozwiazania rownania: ")
    rozwiazania = postepowanie_odwrotne(macierz, ilosc)
    print("a =")
    rozwiazania = rozwiazania[::-1]
    print(rozwiazania)
    print("F(x) = ", f)
    print("Wezly aproksymacji: ")
    for i in range(len(x)):
        print("x = ", x[i], " y = ", y[i])
        #print("y = ", y[i])
    newY= new_y(rozwiazania, x)
    print(newY)

if __name__ == "__main__":
    main()