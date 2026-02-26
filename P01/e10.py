from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

for a in ["U5", "ADA" , "FRAT1", "FXN"]:
    s = Seq()
    s = s.read_fasta("sequences/" + a + ".txt")
    bases = s.count()
    mx = 0
    base = None
    for b in bases:
        if bases[b] > mx:
            mx = bases[b]
            base = b
        elif bases[b] == mx:
            mx = bases[b]
            base = base + " and " + b
    print(f"Gene: {a} ---> Most frequent Base: {base}")