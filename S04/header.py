from pathlib import Path


file_c = Path("sequences/RNU6_269P.txt").read_text()


c = file_c.split("\n")[0]

print(c)