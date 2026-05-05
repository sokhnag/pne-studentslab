from pathlib import Path

class Seq:
    def __init__(self , attribute1 = None):
        self.attribute1 = attribute1
        if self.attribute1 is None:
            self.attribute1 = "NULL"
            print("NULL sequence created.")
        else:
            for a in self.attribute1:
                if a not in "ACGT":
                    self.attribute1 = "ERROR"
            if self.attribute1 == "ERROR":
                print("INVALID SEQUENCE!")

            else:
                print("New sequence created!")

    def __str__(self):
        return self.attribute1

    def len(self):
        if self.attribute1 != "NULL" and self.attribute1 != "ERROR":
            return len(self.attribute1)
        else:
            return 0

    def count(self):
        d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for b in d:
            for a in self.attribute1:
                if b == a:
                    d[b] += 1
        return d

    def count_base(self):
        b1 = ""
        for b in "ACGT":
            count = 0
            for a in self.attribute1:
                if b == a:
                    count += 1
            b1 += b + " : " + str(count) + ", "
        return b1[:len(b1) - 2]

    def reverse(self):
        if self.attribute1 != "NULL" and self.attribute1 != "ERROR":
            return self.attribute1[::-1]
        else:
            return self.attribute1

    def complement(self):
        if self.attribute1 != "NULL" and self.attribute1 != "ERROR":
            d = {"A" : "T" , "T" : "A" , "C" : "G" , "G" : "C"}
            c = ""
            for a in self.attribute1:
                c += d[a]
            return c
        else:
            return self.attribute1

    def read_fasta(self , filename):
        if self.attribute1 == "NULL":
            x = Path(filename).read_text()
            self.attribute1 = x[x.find("\n"):].replace("\n" , "")
            return Seq(self.attribute1)
        else:
            return "Not a NULL sequence"