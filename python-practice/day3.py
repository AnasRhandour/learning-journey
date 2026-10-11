'so this is block one of today'
ids = [91283, 91823, 46378, 98218, 93779, 93874, 99281, 77821, 82622, 87392]

# --- stats (original list) ---
print("First:", ids[0])
print("Last:", ids[-1])
print("Slice [1:3]:", ids[1:3])
print("Count:", len(ids))
print("Sum:", sum(ids))
print("Max:", max(ids))
print("Average:", round(sum(ids) / len(ids), 2))
'to exercise, we need to filter the list of ids in two ways: see IDs starting with 9 and IDs above 90000    '
# --- filter: start with 9 ---
print("\nIDs starting with 9:")
for student_id in ids:
    if str(student_id).startswith("9"):
        print(" ", student_id)

# --- filter: above 90000 ---
print("\nIDs > 90000:")
for student_id in ids:
    if student_id > 90000:
        print(" ", student_id)
'Bonus' 'The easiest way to filter a list is with a list comprehension. Here are the two filters above, but in one line each:'
starts_with_9 = [x for x in ids if str(x).startswith("9")]
above_90k = [x for x in ids if x > 90000]

print(starts_with_9)
print(above_90k)

'now starting block two of today'
ali = {"id": 91283, "name": "ali", "score": 88}

print(ali["name"])         # ali
print(ali["score"])        # 88

ali["score"] = 92          # update
ali["city"] = "Rabat"      # add new key

for key, value in ali.items():
    print(key, "=>", value)
'exercise'
people = [
    {"id": 91283, "name": "ali",     "score": 88},
    {"id": 91823, "name": "anas",    "score": 92},
    {"id": 46378, "name": "ahmed",   "score": 75},
    {"id": 98218, "name": "khadija", "score": 100},
    {"id": 93779, "name": "abdo",    "score": 63},
    {"id": 93874, "name": "khawla",  "score": 81},
    {"id": 99281, "name": "bogar",   "score": 79},
    {"id": 77821, "name": "iterbi",  "score": 88},
    {"id": 82622, "name": "tanjaoui","score": 94},
    {"id": 87392, "name": "werdani", "score": 70},
]
'print everyones name and score, then print the average score of all people'

for p in people:
    print(f"{p['name']} ({p['id']}): {p['score']}")
for grade in people:
    if grade['score'] > 75:
        print("students who pass", grade['name'])
moyenne = sum(p['score'] for p in people )/len(people)
print(moyenne)
