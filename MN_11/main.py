def fun(x,y):
    return x**2 +y

def fun_2(x,y):
    return x+y

def euler(y_0, x_0,funk, x, n):
    h = (x-x_0)/n

    xp = x_0
    yp = y_0
    for i in range(n):
        yp = yp + h*funk(xp,yp)
        xp = xp + h
    return yp

def rk2(y_0, x_0, funk, x, n):
    h = (x-x_0)/n

    xp = x_0
    yp = y_0
    for i in range(n):
        k1 = funk(xp,yp)
        k2 = funk(xp+h, yp+h*k1)
        yp += 0.5*h*(k1+k2)
        xp+=h
    return yp

def rk4(y_0, x_0, funk, x, n):
    h = (x-x_0)/n

    xp = x_0
    yp = y_0
    for i in range(n):
        k1 = funk(xp,yp)
        k2 = funk(xp+0.5*h, yp+0.5*h*k1)
        k3 = funk(xp+0.5*h, yp+0.5*h*k2)
        k4 = funk(xp+h, yp+h*k3)
        yp += (h/6)*(k1+2*k2+2*k3+k4)
        xp+=h
    return yp



def main():
    x=1
    n=10
    print(euler(0.1, 0, fun, 0.3, 3))
    print(rk4(0.1, 0, fun, 0.3, 3))


if __name__ == '__main__':
    main()