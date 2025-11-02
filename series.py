from sympy import series, exp

x = symbols('x')

# Taylor series expansion of e^x around x = 0 up to x^5
s = series(exp(x), x, 0, 6)
print("Series expansion of e^x:", s)
