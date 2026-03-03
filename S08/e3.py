import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.75" # depends on the computer the server is running

while True:
  # -- Ask the user for the message
    message = str.encode(input("Enter message:"))
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(message)
  # -- Close the socket
    s.close()