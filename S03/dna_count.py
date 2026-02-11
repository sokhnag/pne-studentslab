

def count_dna(seq):
    seq = seq.upper()
    print(f"Length of the sequence: {len(seq)}")
    s = "ACTG"
    for m in s:
        count = 0
        for n in seq:
            if n == m:
                count += 1
        print(f"{m} : {count}")

if __name__ == "__main__":
    sequ = input("Introduce the sequence: ")
    count_dna(sequ)


