from Seq0 import seq_complement
from pathlib import Path

x = Path("/home/alumnos/sokhnag/PycharmProjects/pne-studentslab/S04/sequences/U5.txt").read_text()
x2 = x[x.find("\n"):].replace("\n" , "")
print(seq_complement(x2[:20]))