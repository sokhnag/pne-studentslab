from pathlib import Path

from sympy.codegen import Print

from Seq0 import seq_count

print("-----| Exercise 8 |------")
for a in ["U5", "ADA" , "FRAT1", "FXN"]:
    x = Path("/home/alumnos/sokhnag/PycharmProjects/pne-studentslab/S04/sequences/" + a + ".txt").read_text()
    x2 = x[x.find("\n"):]
    mx = 0
    base = None
    for b in ["A", "T" , "C", "G"]:
        if seq_count(x2)[b] > mx:
            mx = seq_count(x2)[b]
            base = b
        elif seq_count(x2)[b] == mx:
            mx = seq_count(x2)[b]
            base = base + " and " + b
    print(f"Gene: {a} ---> Most frequent Base: {base}")