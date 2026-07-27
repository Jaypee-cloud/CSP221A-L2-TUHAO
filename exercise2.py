orders = [
    ("Laptop", 2, 350),
    ("Mouse", 5, 20),
    ("Monitor", 3, 220),
]

high_value_items = []

def find_high_value_items(orders, high_value_items):
    overall_total = 0
    for item, quantity, price in orders:
        cost = quantity * price
        overall_total += cost
        if cost > 500:
            high_value_items.append(item)
    return overall_total

overall_total_cost = find_high_value_items(orders, high_value_items)

print("High value items:", high_value_items)
print("Overall total cost:", overall_total_cost)