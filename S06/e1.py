from wx.lib.pydocview import Print


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



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
