# numerical-methods-python
Implementation of classical numerical methods using Python for scientific computing.

# Numerical Methods using Python

This project contains Python implementations of basic numerical methods
used in scientific computing and applied mathematics.

## Methods Included
- Bisection Method
- Newton–Raphson Method
- Secant Method

## Tools & Libraries
- Python
- NumPy (optional for extension)

## Academic Use
This project is created as part of MSc Mathematics & Computing coursework
and NPTEL Scientific Computing using Python (IIT Delhi).

## Author
Vimal Kumar  
MSc Mathematics & Computing, BHU

Add file - creat file
bisection.py
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


# Example
f = lambda x: x**3 - x - 1
root = bisection(f, 1, 2)
print("Root =", root)

second file 
newton_raphson.py

def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x


f = lambda x: x**3 - x - 1
df = lambda x: 3*x**2 - 1

print("Root =", newton(f, df, 1.5))



