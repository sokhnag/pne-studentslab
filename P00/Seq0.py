from pathlib import Path

def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    x = Path(filename).read_text()
    x2 = x[x.find("\n"): (x.find("\n") + 20) ]
    print(f"Filename : {filename} \nThe first 20 bases are: {x2}")

def seq_len(seq):
    x = Path(seq).read_text()
    x2 = x[x.find("\n"):]
    return len(x2)

def seq_count_base(seq, base):
    count = 0
    for a in seq:
        if a == base:
            count += 1
    return count

def seq_count(seq):
    h = {}
    for a in ["A" , "C" , "G" , "T"]:
        h[a] = seq_count_base(seq , a)
    return h

def seq_reverse(seq, n):
    seq = seq[:n]
    reverse = seq[::-1]
    return "Sequence: " + seq + "\nReverse sequence: " + reverse

def seq_complement(seq, n):
    seqreverse = ""
    dct = {"A": "T" , "G":"C", "C": "G" , "T": "A"}
    for a in seq:
        seqreverse += dct[a]

    return "Sequence: " + seq[:n] + "\nReverse sequence: " + seqreverse[:n]

