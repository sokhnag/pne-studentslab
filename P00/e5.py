from Seq0 import seq_count
from pathlib import Path

for a in ["ADA" , "FRAT1", "FXN", "U5"]:
    x = Path("/home/alumnos/sokhnag/PycharmProjects/pne-studentslab/S04/sequences/" + a + ".txt").read_text()
    x2 = x[x.find("\n"):]
    print(f"Gene: {a} \n {seq_count(x2)}")
