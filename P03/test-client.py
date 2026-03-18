
from Client0 import Client

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print(f"-----| Practice 3, Exercise 7 |------ \nConnection to SERVER at {IP}, PORT: {PORT}\n")

sequ = "AGTGCGTAGCTGACCCATGC"
lst = ["PING", "GET", "INFO" , "COMP", "REV", "GENE"]
for a in lst:
    print(f"* Testing {a}...")
    if a == "GET":
        for i in range(5):
            response = c.talk(a + " " + str(i))
            print(f"GET {i}: {response}")
        print("\n")

    elif a == "PING":
        response = c.talk(a)
        print(response + "\n")

    elif a == "GENE":
        for n in ["U5" , "ADA" , "FRAT1" , "FXN" , "RNU6_269P"]:
            response = c.talk(a + " " + n)
            print(f"GENE {n}: \n{response}")
        print("\n")

    elif a == "INFO":
        response = c.talk(a + " " + sequ)
        print(response + "\n")

    else:
        print(a + " " + sequ)
        response = c.talk(a + " " + sequ)
        print(response + "\n")


