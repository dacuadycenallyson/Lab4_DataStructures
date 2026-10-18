# IX. APPENDIX: ADDITIONAL EXERCISES

# 1. Engineering Test Data Organizer

from collections import defaultdict

# Student-specific inputs
LAST_NAME = "Dacua"
SEED_NUM = 1
FAVORITE_ARTIST = "MYMP"

# Measurement categories
categories = [
    "TEMPERATURE",
    "VOLTAGE",
    "CURRENT",
    "PRESSURE",
    "SPEED"
]

# Generate five test sources
sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]

# Generate measurement records
records = []

for i, source in enumerate(sources):
    category = categories[i]
    artist_char = FAVORITE_ARTIST[i % len(FAVORITE_ARTIST)]
    value = SEED_NUM + ord(artist_char) + (i * 10)

    records.append({
        "source": source,
        "category": category,
        "value": value
    })

# Add another measurement under VOLTAGE
records.append({
    "source": sources[0],
    "category": "VOLTAGE",
    "value": SEED_NUM + ord(FAVORITE_ARTIST[1]) + 5
})

# Add one repeated record
records.append(records[0].copy())

# 1. Generated Test Data
print("=== 1. GENERATED TEST DATA ===")
for record in records:
    print(record)

# 2. Organized Test Data
organized = defaultdict(lambda: defaultdict(list))

for record in records:
    organized[record["source"]][record["category"]].append(
        record["value"]
    )

print("\n=== 2. ORGANIZED TEST DATA ===")
for source in sorted(organized):
    print(source, dict(organized[source]))

# 3. Repeated and Distinct Data
unique_records = []
seen = set()

for record in records:
    key = (
        record["source"],
        record["category"],
        record["value"]
    )

    if key not in seen:
        seen.add(key)
        unique_records.append(record)

print("\n=== 3. REPEATED / DISTINCT DATA ===")
print("Original records:", len(records))
print("Distinct records:", len(unique_records))
print("Repeated records:", len(records) - len(unique_records))

# 4. Numerical and Categorical Summaries
values = [record["value"] for record in unique_records]

print("\n=== 4. NUMERICAL SUMMARY ===")
print("Count:", len(values))
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Average:", round(sum(values) / len(values), 2))

print("\n=== CATEGORICAL SUMMARY ===")
for category in categories:
    count = sum(
        1 for record in unique_records
        if record["category"] == category
    )
    print(f"{category}: {count}")

# 5 and 6. Processed and Ordered Results
ordered_records = sorted(
    unique_records,
    key=lambda record: (
        record["source"],
        record["category"],
        record["value"]
    )
)

print("\n=== 5. PROCESSED AND ORDERED RESULTS ===")
for record in ordered_records:
    print(record)

# 7. Final Summary
print("\n=== 6. FINAL SUMMARY ===")
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Test sources:", len(sources))
print("Original records:", len(records))
print("Distinct records:", len(unique_records))
print("Repeated records:", len(records) - len(unique_records))
print("Dataset organization completed.")