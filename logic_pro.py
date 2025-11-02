from functools import reduce

# ----- CASE DATA -----
# Daily sales in ₹
sales = [500, 1200, 800, 1500, 2500, 400, 1800]

# 1️⃣ Step 1: Apply 10% GST using map()
# Formula: new_price = old_price * 1.10
sales_with_gst = list(map(lambda s: s * 1.10, sales))

# 2️⃣ Step 2: Filter out sales below ₹1000 using filter()
high_sales = list(filter(lambda s: s >= 1000, sales_with_gst))

# 3️⃣ Step 3: Calculate total revenue using reduce()
total_revenue = reduce(lambda a, b: a + b, high_sales)

# ----- OUTPUT -----
print("Original Sales: ", sales)
print("Sales after adding GST: ", sales_with_gst)
print("High Sales (>=1000): ", high_sales)
print("Total Revenue: ₹", total_revenue)
