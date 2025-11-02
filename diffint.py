from sympy import symbols, diff, integrate

x = symbols('x')

# Define an expression
expr = x**3 + 2*x**2 + x

# Differentiate
derivative = diff(expr, x)
print("Derivative:", derivative)

# Integrate
integral = integrate(expr, x)
print("Integral:", integral)
