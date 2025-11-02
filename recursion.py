def factorial(n):
    if n == 0 or n == 1:   # Base case (stops recursion)
        return 1
    else:
        return n * factorial(n - 1)   # Recursive call

# Test the function
print("Factorial of 5 is:", factorial(5))

