def fun(x):
    return -x**3+10*x+5

def funp(x):
    return -3*x**2+10

def fun2(x):
    return x**3+2*x+3

def funp2(x):
    return 3*(x**2)+2

def metoda_stycznych(x,n, func, poch):
    for i in range(n):
        x = x - ((func(x))/(poch(x)))
        print("Nr interacji: ", i)
        print("Punkt: ", x)
        print("Wartość funkcji: ", func(x))

def iloraz_roznicowy(xw, xm, func):
    return ((func(xw)-func(xm))/(xw-xm))

def meotda_siecznych(x,n, func, poch):
    xstart = x-0.1
    for i in range(n):
        xnext = x - func(x)/poch(x,xstart,func)
        xstart = x
        x = xnext
        print("Nr interacji: ", i)
        print("Punkt: ", x)
        print("Wartość funkcji: ", func(x))


def main():
    print("Funkcja -x^3 +10x+5")
    metoda_stycznych(6,5, fun, funp)
    meotda_siecznych(6,5,fun,iloraz_roznicowy)
    metoda_stycznych(3,8,fun2,funp2)
    meotda_siecznych(3,8,fun2, iloraz_roznicowy)

if __name__ == "__main__":
    main()