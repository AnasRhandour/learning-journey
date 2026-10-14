numbers=[3,7,1,8,9,0]
print(sum(numbers)/len(numbers))
for p in numbers:
    if p>4:
        print(p)

count=0
for d in numbers:
    if d>4:
        count+=1

print(count)

idk= [
    {"name": "anas", "score":92},
    {"name": "adam", "score":45},
    {"name": "yahya", "score":56},
]

for p in idk:
    print(f"{p['name']} scored: {p['score']}")