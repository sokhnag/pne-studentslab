from Seq0 import seq_count
from pathlib import Path

print("-----| Exercise 5 |------")
for a in ["U5", "ADA" , "FRAT1", "FXN" ]:
    x = Path("sequences/" + a + ".txt").read_text()
    x2 = x[x.find("\n"):]
    print(f"Gene: {a} \n {seq_count(x2)}")
