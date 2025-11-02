def square(x):
    return x * x

def cube(x):
    return x * x * x

# Higher-Order Function
def apply_function(func, value):
    return func(value)

# Using HOF
print(apply_function(square, 3))  # Output: 9
print(apply_function(cube, 2))    # Output: 8
