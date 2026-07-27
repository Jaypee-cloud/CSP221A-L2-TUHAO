roster = {
    "Amara": {"Math": 92, "English": 95, "Science": 85},
    "Leo": {"AP": 96, "AI": 90, "Filipino": 90},
}

def add_students(roster, name, scores):
    roster[name] = scores

add_students(roster, "Mia", {"Math": 85, "English": 90, "Science": 88})
add_students(roster, "Jopher", {"Math": 90, "English": 90, "Science": 85})

for name, scores in roster.items():
    average = sum(scores.values()) / len(scores)
    if average > 80:
        print(name, "-", average)