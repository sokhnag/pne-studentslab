import socket
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    if req_line.split("/")[1] == "info":
        if req_line.split("/")[2].split(" ")[0] == "A":
            body = Path("html/info/A.html").read_text()
        elif req_line.split("/")[2].split(" ")[0] == "C":
            body = Path("html/info/C.html").read_text()
        elif req_line.split("/")[2].split(" ")[0] == "G":
            body = Path("html/info/G.html").read_text()
        elif req_line.split("/")[2].split(" ")[0] == "T":
            body = Path("html/info/T.html").read_text()
        else:
            body = Path("html/info/error.html").read_text()
    else:
        body = Path("html/info/error.html").read_text()

    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()


# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
