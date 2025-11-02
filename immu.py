# Strings in Python are immutable
name = "Yash"
print("Original:", name)

# Try to change one character
# name[0] = "R"   # ❌ This will cause an error

# Instead, create a new string
new_name = "R" + name[3:]
print("New:", new_name)
