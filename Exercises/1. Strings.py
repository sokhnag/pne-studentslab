


dna = "ATGCGATCGATCGATCGATCGA"
rna = dna.replace("T" , "U")
atc = 0
i = 0
while i < len(dna) - 2:
    if dna[i] == "A" :
        txt = dna[i] + dna[i+1] + dna[i+2]
        if txt == "ATC" :
            atc += 1
    i += 1
print(f"Length: {len(dna)} \n"
        f"First 5: {dna[:5]} \n" 
        f"Last 3: {dna[-3:]} \n"
        f"Lowercase: {dna.lower()} \n"
        f"ATC count: {atc}\n"
        f"RNA: {rna}")
