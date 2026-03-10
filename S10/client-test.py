import termcolor

from Client0 import Client

IP = "212.128.255.74"
PORT = 8080

c = Client(IP, PORT)

i = 0
while i < 5:
    msg = termcolor.colored(f"Message {i}" , "blue")
    print(f"To Server: {msg} ")
    response = termcolor.colored(c.talk(f"Message {i}") , "green" )
    print(f"From server {response}")
    i += 1