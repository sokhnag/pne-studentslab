def average(lst):
    return round(sum(lst) / len(lst) , 1)

def get_status(avg):
    if avg >= 5:
        return "Pass"
    else:
        return "Fail"

students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

lst1 = []
lst2 = []
for a in students:
    print(f"{a["name"]} : {average(a["grades"])} --> {get_status(average(a["grades"]))}")
    if get_status(average(a["grades"])) == "Pass":
        lst1.append(get_status(average(a["grades"])))
    else:
        lst2.append(get_status(average(a["grades"])))
print(f"Results: {len(lst1)} passed, {len(lst2)} failed")