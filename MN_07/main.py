import math

def metoda_prostokatow(f, przedzial, liczba_przedz):
    b = przedzial[1]
    a = przedzial[0]
    elem_s = ((b-a)/liczba_przedz)

    wynik = 0
    x = a
    for i in range(liczba_przedz):
        wynik += f(x+0.5*elem_s)
        x+=elem_s

    return elem_s*wynik

def metoda_trapezow(f, przedzial, liczba_przedz):
    b = przedzial[1]
    a = przedzial[0]
    elem_s = ((b-a)/liczba_przedz)
    kroki = []
    kroki.append(a)
    for i in range(liczba_przedz):
        a += elem_s
        kroki.append(a)

    wynik = 0
    for n in range(liczba_przedz):
        h = kroki[n+1] - kroki[n]
        podstawy = (f(kroki[n]) + f(kroki[n+1]))
        wynik += h*podstawy*0.5
    return wynik

def metoda_simpsona(f, przedzial, liczba_przedz):
    elem_s = ((przedzial[1]-przedzial[0])/liczba_przedz)
    b = przedzial[1]
    a = przedzial[0]

    wynik = 0
    for i in range(liczba_przedz):
        if i != 0:
            a += elem_s
        b1 = a+elem_s
        mnoz = (b1-a)/6
        naw = f(a)+4*f((a+b1)/2)+f(b1)
        wynik += mnoz*naw
    return wynik


def sin(x):
    return math.sin(x)

def exp(x):
    return math.exp(x)

def fun_x(x):
    return x*x + 2*x + 5

def main():
    przedzial_calk = [0.5, 5.0]
    liczba_przedz = 1
    f = fun_x
    if f == sin:
        print("sin(x)")
    elif f == exp:
        print("exp(x)")
    else:
        print("x^2 +2x +5")
    print(f"Przedzial calkowania: {przedzial_calk}")
    print(f"Liczba przedzialow: {liczba_przedz}")
    print(f"Wynik metoda prostokatow: {metoda_prostokatow(f, przedzial_calk, liczba_przedz)}")
    print(f"Wynik metoda trapezow: {metoda_trapezow(f, przedzial_calk, liczba_przedz)}")
    print(f"Wynik metoda Simpsona: {metoda_simpsona(f, przedzial_calk, liczba_przedz)}")


if __name__ == "__main__":
    main()