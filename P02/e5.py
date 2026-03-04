from Client0 import Client
from Client0 import Seq


PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "212.128.255.74"
PORT = 8080

c = Client(IP, PORT)
print(c)
s = Seq()
b = str(s.read_fasta("sequences/FRAT1.txt"))
c.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...")
fragments = 1
f = ""
while fragments in range(6):
    for a in b:
        f += a
        if len(f) == 10:
            print(fragments)
            print(f"Fragment {fragments}: {f}")
            c.talk(f"Fragment {fragments}: {f}")
            fragments += 1
            f = ""