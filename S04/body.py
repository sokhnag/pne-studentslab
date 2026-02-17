from pathlib import Path

x = Path("sequences/U5.txt").read_text()

x2 = x[x.find("\n"):]

print(x2)