import math

def fun1(x):
    return math.cos(x**3-2*x)

def alg_bisekcji(a,b,f,blad):
    if f(a) * f(b) < 0:
        while True:
            print('a: ', a)
            print('b: ', b)
            print('f(a): ', f(a))
            print('f(b): ', f(b))

            x_0 = (a+b)/2
            print('x0: ', x_0)
            print('f(x0): ', f(x_0))
            print('f(a)*f(x0): ', f(a)*f(x_0))
            if abs(f(x_0))<blad:
                return x_0
            elif f(a)*f(x_0) < 0:
                b = x_0
            else:
                a = x_0

def metoda_fal_linii(a,b,f,blad):
    if f(a) * f(b) < 0:
        while True:
            print('a: ', a)
            print('b: ', b)
            print('f(a): ', f(a))
            print('f(b): ', f(b))

            x_1 = a - ((f(a)*(b-a))/(f(b)-f(a)))

            print('x1: ', x_1)
            print('f(x1): ', f(x_1))
            print('f(a)*f(x1): ', f(a) * f(x_1))
            if abs(f(x_1))<blad:
                return x_1
            elif f(x_1)*f(a)<0:
                b = x_1
            else:
                a = x_1




def main():
    print(alg_bisekcji(0,2,fun1, 0.01))
    print(metoda_fal_linii(0,2,fun1, 0.01))


if __name__ == '__main__':
    main()