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

def fun(x):
    return x*x + 2*x +5

def exp(x):
    return math.exp(x)

def kwadratura_2(a,b, f):
    wezly = [-math.sqrt(3)/3, math.sqrt(3)/3]
    wagi = [1,1]
    zmienne_t = []

    for i in wezly:
        zmienne_t.append(((a+b)/2)+((b-a)/2)*i)

    wynik = 0

    for i in range(len(zmienne_t)):
        wynik += wagi[i]*f(zmienne_t[i])

    wynik = wynik*((b-a)/2)
    return wynik

def kwadratura_3(a, b, f):
    wezly = [-math.sqrt(3/5), 0, math.sqrt(3/5)]
    wagi = [5/9, 8/9, 5/9]
    zmienne_t = []

    for i in wezly:
        zmienne_t.append(((a+b)/2)+((b-a)/2)*i)

    wynik = 0
    for i in range(len(zmienne_t)):
        wynik += wagi[i]*f(zmienne_t[i])

    wynik = wynik*((b-a)/2)
    return wynik

def kwadratura_4(a, b, f):
    wezly = [(-1/35)*math.sqrt(525+70*math.sqrt(30)), (-1/35)*math.sqrt(525-70*math.sqrt(30)), (1/35)*math.sqrt(525-70*math.sqrt(30)), (1/35)*math.sqrt(525+70*math.sqrt(30))]
    wagi = [(1/36)*(18-math.sqrt(30)), (1/36)*(18+math.sqrt(30)), (1/36)*(18+math.sqrt(30)), (1/36)*(18-math.sqrt(30))]
    zmienne_t = []

    for i in wezly:
        zmienne_t.append(((a+b)/2)+((b-a)/2)*i)

    wynik = 0
    for i in range(len(zmienne_t)):
        wynik += wagi[i] * f(zmienne_t[i])

    wynik = wynik * ((b - a) / 2)
    return wynik

def main():
    calka_sin_1 = kwadratura_2(0.5,2.5,sin)
    calka_sin_2 = kwadratura_3(0.5,2.5,sin)
    calka_sin_3 = kwadratura_4(0.5, 2.5, sin)
    calka_sin_prostokat = metoda_prostokatow(sin, [0.5,2.5], 20)
    calka_sin_trapez = metoda_trapezow(sin, [0.5, 2.5], 20)
    calka_sin_parabola = metoda_simpsona(sin, [0.5, 2.5], 20)
    print("sin(x)")
    print(f"Przedzial calkowania: {[0.5, 2.5]}")
    print("Wynik kwadratura wezly 2: ", calka_sin_1)
    print("Wynik kwadratura wezly 3: ", calka_sin_2)
    print("Wynik kwadratura wezly 4: ", calka_sin_3)
    print("Wynik metoda prostokatow: ", calka_sin_prostokat)
    print("Wynik metoda trapezow: ", calka_sin_trapez)
    print("Wynik metoda simpsona: ", calka_sin_parabola)

    calka_exp_1 = kwadratura_2(0.5, 5.0, exp)
    calka_exp_2 = kwadratura_3(0.5, 5.0, exp)
    calka_exp_3 = kwadratura_4(0.5, 5.0, exp)
    calka_exp_prostokat = metoda_prostokatow(exp, [0.5, 5.0], 20)
    calka_exp_trapez = metoda_trapezow(exp, [0.5, 5.0], 20)
    calka_exp_parabola = metoda_simpsona(exp, [0.5, 5.0], 20)
    print("\n\n\nexp(x)")
    print(f"Przedzial calkowania: {[0.5, 5.0]}")
    print("Wynik kwadratura wezly 2: ", calka_exp_1)
    print("Wynik kwadratura wezly 3: ", calka_exp_2)
    print("Wynik kwadratura wezly 4: ", calka_exp_3)
    print("Wynik metoda prostokatow: ", calka_exp_prostokat)
    print("Wynik metoda trapezow: ", calka_exp_trapez)
    print("Wynik metoda simpsona: ", calka_exp_parabola)

    calka_f_1 = kwadratura_2(0.5, 5.0, fun)
    calka_f_2 = kwadratura_3(0.5, 5.0, fun)
    calka_f_3 = kwadratura_4(0.5, 5.0, fun)
    calka_f_prostokat = metoda_prostokatow(fun, [0.5, 5.0], 20)
    calka_f_trapez = metoda_trapezow(fun, [0.5, 5.0], 20)
    calka_f_parabola = metoda_simpsona(fun, [0.5, 5.0], 20)
    print("\n\n\nx^2 +2x +5")
    print(f"Przedzial calkowania: {[0.5, 5.0]}")
    print("Wynik kwadratura wezly 2: ", calka_f_1)
    print("Wynik kwadratura wezly 3: ", calka_f_2)
    print("Wynik kwadratura wezly 4: ", calka_f_3)
    print("Wynik metoda prostokatow: ", calka_f_prostokat)
    print("Wynik metoda trapezow: ", calka_f_trapez)
    print("Wynik metoda simpsona: ", calka_f_parabola)

if __name__ == "__main__":
    main()