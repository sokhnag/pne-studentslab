import random
import socket

import termcolor


class NumberGuesser:
    def __init__(self):
        self.number = random.randint(1,100)
        self.attempts = []
    def __int__(self):
        return self.number

    def guess(self, n ):
        self.attempts.append(n)
        if n == self.number:
            return  termcolor.colored(f"You won after {len(self.attempts)} attempts" , "green")
        elif n > self.number:
            return termcolor.colored("Lower" , "blue")
        else:
            return termcolor.colored("Higher" , "red")

IP = "212.128.255.74"
PORT = 8080

number = NumberGuesser()
attempts = []

def process_player(s):
    guess_raw = s.recv(2000)
    guess = int(guess_raw.decode())
    print(f"Message FROM CLIENT: {guess} ")
    response_msg = number.guess(guess)
    players.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

while True:
    print("Waiting for players....")
    try:
        (players, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        process_player(players)
        players.close()
