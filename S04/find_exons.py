from pathlib import Path

x = Path("sequences/ADA_EXONS.txt").read_text()
x2 = (Path("sequences/ADA.txt").read_text())

x = x.split(">")

for a in x:
    if a != "":
        exon  = (a[a.find("\n"):])
        start = x2.find(exon)
        end = 1
        print(f"{exon} \n Long. : {len(exon)} \n Start : {start} \n End : {end}")