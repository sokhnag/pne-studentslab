from Seq1 import Seq


print("-----| Practice 1, Exercise 8 |------")

s = Seq()
s = s.read_fasta("sequences/U5.txt")


print(f"Sequence 1: (length: {s.len()}) {s} \n Bases: {s.count()} \n Reverse: {s.reverse()} \n Complement: {s.complement()}")


