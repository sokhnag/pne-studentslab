from Seq0 import seq_complement
from pathlib import Path

print("-----| Exercise 7 |------ \nGene U5:")
x = Path("sequences/U5.txt").read_text()
x2 = x[x.find("\n"):].replace("\n" , "")
print(seq_complement(x2[:20]))