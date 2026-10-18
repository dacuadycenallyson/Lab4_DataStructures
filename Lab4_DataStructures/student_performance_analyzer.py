from collections import defaultdict

LAST_NAME = "Dacua"
SEED_NUM = 1
FAVORITE_ARTIST = "MYMP"

students = [f"{LAST_NAME}_S{i}" for i in range(1, 6)]
subjects = [
    "PROGRAMMING",
    "MATHEMATICS",
    "ELECTRONICS",
    "PHYSICS",
    "ENGLISH"
]

records = []

for i, student in enumerate(students):
    for j, subject in enumerate(subjects):
        char = FAVORITE_ARTIST[(i + j) % len(FAVORITE_ARTIST)]
        score = (SEED_NUM + ord(char) + i * 7 + j * 3) % 51 + 50

        records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# Add one repeated student-subject record
records.append(records[0].copy())

# Add one incomplete record
records.append({
    "student": students[0],
    "subject": "ENGLISH",
    "score": None
})

def category(score):
    if score is None:
        return "INCOMPLETE"
    elif score >= 90:
        return "EXCELLENT"
    elif score >= 80:
        return "VERY GOOD"
    elif score >= 75:
        return "PASSED"
    else:
        return "FAILED"

print("=== 1. GENERATED PERFORMANCE RECORDS ===")
for record in records:
    print(record)

organized = defaultdict(dict)
for record in records:
    organized[record["student"]].setdefault(
        record["subject"], []
    ).append(record["score"])

print("\n=== 2. ORGANIZED STUDENT/SUBJECT DATA ===")
for student in sorted(organized):
    print(student, dict(organized[student]))

seen = set()
unique_records = []
repeated = []

for record in records:
    key = (
        record["student"],
        record["subject"],
        record["score"]
    )
    if key in seen:
        repeated.append(record)
    else:
        seen.add(key)
        unique_records.append(record)

incomplete = [
    r for r in unique_records
    if r["score"] is None
]

print("\n=== 3. REPEATED/INCOMPLETE RECORDS ===")
print("Original records:", len(records))
print("Repeated records:", len(repeated))
print("Incomplete records:", len(incomplete))
print("Repeated entries:", repeated)
print("Incomplete entries:", incomplete)

print("\n=== 4. PERFORMANCE CATEGORIES ===")
for record in unique_records:
    print(
        record["student"],
        record["subject"],
        record["score"],
        category(record["score"])
    )

print("\n=== 5. STUDENT AND SUBJECT SUMMARIES ===")
for student in students:
    scores = [
        r["score"] for r in unique_records
        if r["student"] == student and r["score"] is not None
    ]
    average = round(sum(scores) / len(scores), 2) if scores else 0
    print(student, "Average:", average, "Valid scores:", len(scores))

for subject in subjects:
    scores = [
        r["score"] for r in unique_records
        if r["subject"] == subject and r["score"] is not None
    ]
    average = round(sum(scores) / len(scores), 2) if scores else 0
    print(subject, "Average:", average, "Valid scores:", len(scores))

ordered = sorted(
    unique_records,
    key=lambda r: (r["student"], r["subject"])
)

print("\n=== 6. ORDERED RESULTS ===")
for record in ordered:
    print(record, "Category:", category(record["score"]))

print("\n=== FINAL STUDENT PERFORMANCE REPORT ===")
print("Student:", LAST_NAME)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Students:", len(students))
print("Subjects:", len(subjects))
print("Original records:", len(records))
print("Repeated records:", len(repeated))
print("Incomplete records:", len(incomplete))
print("Valid unique records:", sum(
    1 for r in unique_records if r["score"] is not None
))
print("Report generated successfully.")