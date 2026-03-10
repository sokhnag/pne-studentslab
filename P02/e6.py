from Client0 import Client
from Client0 import Seq


PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "212.128.255.74"
PORT1 = 8080

PORT2 = 8081

c = Client(IP, PORT1)
c2 = Client(IP, PORT2)
s = Seq()
b = str(s.read_fasta("sequences/FRAT1.txt"))


n = [c, c2]
for j in n:
    print(j)
    j.talk("Sending FRAT1 gene to the server, in fragments of 10 bases...  ")

print(f"Gene FRAT1: {b}")
fragments = 1

f = ""
for a in b:
    if fragments <= 10:
        f += a
        if len(f) == 10:
            print(f"Fragment {fragments}: {f}")
            if fragments % 2 == 0:
                c2.talk(f"Fragment {fragments}: {f}")
            else:
                c.talk(f"Fragment {fragments}: {f}")
            fragments += 1
            f = ""


