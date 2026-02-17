from pathlib import Path

x = Path("sequences/ADA.txt").read_text()

x2 = "".join(x[x.find("\n"):].split("\n"))

print(len(x2))