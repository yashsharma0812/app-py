from sympy import limit, sin

x = symbols('x')

# Example: limit of sin(x)/x as x → 0
result = limit(sin(x)/x, x, 0)
print("Limit:", result)
