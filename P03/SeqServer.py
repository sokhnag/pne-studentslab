import socket

import termcolor

from Seq1 import Seq

PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")
seqs = ["AGTGCGTAGCTGACCCATGC", "AGTGATGATAGTAGAT", "GTAGCGGCGCGC", "GTGTCGTGGC" , "GTAGATAGGGCCCCCC"]

while True:

    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:

        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()

        if msg == "PING":
            response = "OK!"
            termcolor.cprint("PING command!", "green")

        elif msg.startswith("GET"):
            if int(msg.strip()[-1]) in range(5):
                termcolor.cprint("GET", "green")
                response = seqs[int(msg.strip()[-1])]


        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            s = Seq(msg.split(" ")[1])
            n = {}
            bases = ""

            for j in s.count() :
                n[j] = str(round(s.count()[j] / s.len() * 100, 2 )) + " %"
                bases += j + ": " + str(s.count()[j]) + "  (" + n[j] + ")\n"

            response = f"Sequence: {s} \nTotal length: {s.len()} \n{bases}"


        elif msg.startswith("COMP"):
            termcolor.cprint("COMP", "green")
            s = Seq(msg.split(" ")[1])
            response = s.complement()

        elif msg.startswith("REV"):
            termcolor.cprint("REV", "green")
            s = Seq(msg.split(" ")[1])
            response = s.reverse()

        elif msg.startswith("GENE")  :
            if "U5" or "ADA" or "FRAT1" or "FXN" or "RNU6_269P" in msg:
                termcolor.cprint("GENE", "green")
                s = Seq()
                s.read_fasta("sequences/" + msg.split(" ")[1] + ".txt")
                response = str(s)
        else:
            response = "Invalid command"

        cs.send(response.encode())
        print(response)
        cs.close()
