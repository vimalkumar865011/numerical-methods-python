def f(x):
    return x**3 - x - 2

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None

    for i in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        
        if abs(f(c)) < tol:
            print("Iterations:", i+1)
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c
