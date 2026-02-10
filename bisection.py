def bisection(f, a, b, tol=1e-6):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    while abs(b - a) > tol:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


f = lambda x: x**3 - x - 1
print("Root =", bisection(f, 1, 2))
