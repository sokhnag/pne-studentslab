from Client0 import Client
from Client0 import Seq


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

genes = ["U5", "FRAT1", "ADA"]
IP = "212.128.255.74"
PORT = 8080

c = Client(IP, PORT)
print(c)
for a in genes:
    s = Seq()
    b = s.read_fasta("sequences/" + a + ".txt")
    print(f"To server: Sending the {a} Gene to the server...\n"
    f"From server: {c.talk(f"Sending the {a} Gene to the server {c.ip}")}\n"
    f"To server: {b}\n"
    f"From server: {c.talk(b)}")

