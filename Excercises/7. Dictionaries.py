from dask.array import average

student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

lst = []
for a in student["grades"]:
    lst.append(student["grades"][a])

print(f"Name: {student["name"]} \n"
f"Number of subjects: {len(student["subjects"])} \n"
f"Enrolled in PNE: {"PNE" in student["subjects"]} \n"
f"Databases grade: {student["grades"]["Databases"]} \n"
f"Average grade: {round(sum(lst) / len(lst), 2)} \n"
"Subject grades: \n"
  f"   PNE: {student["grades"]["PNE"]}\n"
  f"   Networks: {student["grades"]["Networks"]} \n"
  f"   Databases: {student["grades"]["Databases"]} \n")