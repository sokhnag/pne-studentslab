from dna_count import count_dna

with open("dna.txt.", "r") as f:
    lines = f.readlines()

for a in lines:
    print(a) , count_dna(a)

