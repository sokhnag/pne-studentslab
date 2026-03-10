import socket

import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.74" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

number_of_connections = 0

ip_and_ports = {}

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        number_of_connections += 1

        print(f"CONNECTION {number_of_connections}: Client IP, PORT: {client_ip_port}")

        ip_and_ports[number_of_connections] = client_ip_port

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = termcolor.colored(msg_raw.decode() , "green")

        # -- Print the received message

        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = "ECHO: " + msg + "\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        if number_of_connections == 5:
            print("The following clients have connected to de server:")
            for a in ip_and_ports:
                print(f"CLIENT {a - 1}: Client IP, PORT: {ip_and_ports[a]}")
            # -- Close the data socket
            cs.close()

            exit()

