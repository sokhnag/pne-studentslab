from Seq0 import seq_count_base
from pathlib import Path

print("-----| Exercise 4 |------")
for a in ["U5", "ADA" , "FRAT1", "FXN"]:
    print(f"Gene: {a}")
    x = Path("/home/alumnos/sokhnag/PycharmProjects/pne-studentslab/S04/sequences/"+a+".txt").read_text()
    x2 = x[x.find("\n"):]
    for b in ["A" , "C" , "T" ,"G"]:
        print(f"{b} : {seq_count_base(x2 , b)}")
