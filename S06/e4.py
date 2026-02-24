import termcolor



class Seq:
    """A class for representing sequences"""
    def __init__(self , attribute1):
        self.attribute1 = attribute1
        for a in self.attribute1:
            if a not in "ACGT":
                self.attribute1 = "ERROR"
        if self.attribute1 == "ERROR":
            print("ERROR!")
        print("New sequence created!")

    def __str__(self):
        return self.attribute1

    def len(self):
        return len(self.attribute1)

def print_seqs(seq_list , color):
    for a in seq_list:
        s = "Sequence " + str(seq_list.index(a)) + ": "
        termcolor.cprint(f" {s }(length: {a.len()}) {a}", color)


def generate_seqs(pattern, number):
    lst = []
    for i in range(1, number + 1):
        lst.append(Seq(pattern * i))
    return lst

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1 , "blue")

print()
print("List 2:" , "")
print_seqs(seq_list2 , "yellow")