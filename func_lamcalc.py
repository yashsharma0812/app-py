# Normal function
def add(x, y):
    return x + y

# Equivalent lambda expression
add_lambda = lambda x, y: x + y

# Using it
print(add_lambda(5, 3))  # Output: 8

# Lambda with map()
nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # Output: [2, 4, 6]
