class Seq:
    """A class for representing sequences"""
    def __init__(self , attribute1):
        self.attribute1 = attribute1
        for a in self.attribute1:
            if a not in "ACGT":
                self.attribute1 = "ERROR"
        if self.attribute1 == "ERROR":
            print("ERROR!")

    def __str__(self):
        return self.attribute1

    def len(self):
        return len(self.attribute1)

def print_seqs(seq_list):
    for a in seq_list:
        s = "Sequence " + str(seq_list.index(a)) + ": "
        print(f" {s }(length: {a.len()}) {a}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)