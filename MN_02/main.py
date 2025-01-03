def read_file(nazwa, tab1, tab2):
    with open(nazwa, "r") as odczyt:
        ilosc = int(odczyt.readline())

        for i in range(ilosc):
            wart1, wart2 = map(float, odczyt.readline().split())
            tab1.append(wart1)
            tab2.append(wart2)

        return ilosc

def interpolacja_netwona(xi, fxi, ilosc, punkt, wspolczynnik_b):
    wspolczynnik_b.append(fxi[0])

    wspolczynnik_p = []
    wspolczynnik_p.append(1)

    for h in range(1, ilosc):
        b_k = 0
        for i in range(0, h+1):
            licznik = fxi[i]
            mianownik = 1
            for j in range(0, h+1):
                if i!=j:
                    mianownik *= (xi[i]-xi[j])

            b_k += (licznik/mianownik)

        wspolczynnik_b.append(b_k)

    for h in range(1, ilosc):
        p_k = 1
        for i in range(0, h):
            p_k *= (punkt - xi[i])

        wspolczynnik_p.append(p_k)

    wynik = 0
    for h in range(0, ilosc):
        wynik += wspolczynnik_p[h]*wspolczynnik_b[h]

    return wynik




def main():
    xi = []
    fxi = []
    wspolczynnik_b = []
    ilosc = read_file("MN_in_2.txt", xi, fxi)
    print(f"Liczba węzłów to: {ilosc}")
    print(f"Węzły interpolacji: {xi}")
    print(f"Wartosci w wezlach: {fxi}")
    punkt = float(input("Podaj punkt: "))
    wynik = interpolacja_netwona(xi, fxi, ilosc, punkt, wspolczynnik_b)
    print(f"Wynik: {wynik}")
    print(f"Wspolczynniki b: {wspolczynnik_b}")




if __name__ == '__main__':
    main()