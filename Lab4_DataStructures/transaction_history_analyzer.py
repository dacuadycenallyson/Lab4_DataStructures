from collections import defaultdict

LAST_NAME = "Dacua"
SEED_NUM = 1
FAVORITE_ARTIST = "MYMP"

customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]

products = {
    "NOTEBOOK": 50,
    "PEN": 15,
    "USB": 250,
    "HEADPHONES": 500,
    "CALCULATOR": 300
}

transactions = []

for i, customer in enumerate(customers):
    for j, (product, price) in enumerate(products.items()):
        char = FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        quantity = (SEED_NUM + ord(char) + i + j) % 5 + 1

        transactions.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": price,
            "total": quantity * price
        })

# Add one repeated customer-product transaction
transactions.append(transactions[0].copy())

print("=== 1. GENERATED TRANSACTION RECORDS ===")
for transaction in transactions:
    print(transaction)

organized = defaultdict(dict)

for transaction in transactions:
    customer = transaction["customer"]
    product = transaction["product"]
    organized[customer].setdefault(product, []).append(
        transaction["quantity"]
    )

print("\n=== 2. ORGANIZED TRANSACTION DATA ===")
for customer in sorted(organized):
    print(customer, dict(organized[customer]))

seen = set()
unique_transactions = []
repeated = []

for transaction in transactions:
    key = (transaction["customer"], transaction["product"])

    if key in seen:
        repeated.append(transaction)
    else:
        seen.add(key)
        unique_transactions.append(transaction)

print("\n=== 3. REPEATED/DISTINCT TRANSACTIONS ===")
print("Original records:", len(transactions))
print("Repeated transactions:", len(repeated))
print("Distinct transactions:", len(unique_transactions))
print("Distinct customers:", len(set(t["customer"] for t in transactions)))
print("Distinct products:", len(set(t["product"] for t in transactions)))

print("\n=== 4. TRANSACTION VALUES ===")
for transaction in transactions:
    print(
        transaction["customer"],
        transaction["product"],
        "Total:",
        transaction["total"]
    )

print("Overall transaction value:", sum(t["total"] for t in transactions))

print("\n=== 5. CUSTOMER SUMMARIES ===")
for customer in customers:
    records = [t for t in transactions if t["customer"] == customer]
    total_quantity = sum(t["quantity"] for t in records)
    total_value = sum(t["total"] for t in records)
    print(customer, "Quantity:", total_quantity, "Value:", total_value)

print("\n=== 6. PRODUCT SUMMARIES ===")
for product in products:
    records = [t for t in transactions if t["product"] == product]
    total_quantity = sum(t["quantity"] for t in records)
    total_value = sum(t["total"] for t in records)
    print(product, "Quantity:", total_quantity, "Value:", total_value)

ordered = sorted(
    transactions,
    key=lambda t: (t["customer"], t["product"])
)

print("\n=== 7. ORDERED RESULTS ===")
for transaction in ordered:
    print(transaction)

print("\n=== 8. OVERALL TRANSACTION SUMMARY ===")
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Customers:", len(customers))
print("Products:", len(products))
print("Original records:", len(transactions))
print("Repeated transactions:", len(repeated))
print("Distinct transactions:", len(unique_transactions))
print("Overall transaction value:", sum(t["total"] for t in transactions))
print("Final consolidated transaction report generated successfully.")