students = [
    {"name": "anas",  "score": 92},
    {"name": "adam",  "score": 45},
    {"name": "yahya", "score": 56},
]

def average(students):
    total = 0
    for s in students:
        total += s["score"]
    return round(total / len(students), 2)

def passing_students(students):
    result = []
    for s in students:
        if s["score"] >= 50:
            result.append(s)
    return result

print(average(students))            
print(passing_students(students))   