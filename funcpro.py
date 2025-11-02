from functools import reduce

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# 1️⃣ map(): apply a function to every item
# Example: square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# 2️⃣ filter(): filter elements based on a condition
# Example: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# 3️⃣ reduce(): apply a function to pairs to get a single result
# Example: find product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
