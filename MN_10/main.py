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

def silnia(n):
    if n == 0:
        return 1
    mnoz = 1
    for i in range(1, n+1):
        mnoz*=i

    return mnoz

def dwumian(n,k):
    return silnia(n)/(silnia(k)*silnia(n-k))

def funkcja_f(k,n,q):
    if q == 0:
        return 1
    suma = 0
    for s in range(k+1):
        suma += ((-1)**s)*dwumian(k,s)*dwumian(k+s,s)*(wartosc_wielomianu(q,s)/wartosc_wielomianu(n,s))
    return suma

def wartosc_wielomianu(x,n):
    if n == 0:
        return 1
    mnoz = 1
    for i in range(n):
        mnoz*=(x-i)
    return mnoz

def gram(x,y,stp,ilosc,szuk):
    q = ((szuk-x[0])/(abs(x[1]-x[0])))
    ym =0

    for n in range(stp+1):
        ck=0
        sk=0
        for i in range(ilosc):
            wart_f = funkcja_f(n,ilosc-1,i)
            sk += wart_f**2
            ck +=y[i]*wart_f
        #print("sk: ", sk)
        #print("ck: ", ck)
        ym += (ck/sk)*funkcja_f(n, ilosc-1, q)
    return ym


def main():
    ck = []
    sk = []
    ilosc, x, y = read_file("MN_10.txt")
    print("Liczba węzłów wynosi: ", ilosc)
    stopien = 2
    for i in range(ilosc):
        wynik = gram(x, y, stopien, ilosc, x[i])
        print("x = ", x[i], " y = ", y[i], " -> ", "ym = ", wynik)

    podane = float(input("Podaj wybrany węzeł do aproksymacji: "))
    wynik = gram(x,y, stopien, ilosc,podane)
    print("\n\nx = ", podane, "ym = ", wynik)


main()