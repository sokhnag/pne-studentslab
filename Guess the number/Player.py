import termcolor

from Client0 import Client

IP = "212.128.255.74"
PORT = 8080

c = Client(IP, PORT)
guess = False
while not guess:
    msg = int(input("Enter a guess:"))
    response = c.talk(msg)
    termcolor.cprint(response , "blue")
    if response.startswith("You"):
        guess = True
